class UnusedRemoval:
    """
    Conservative, per-file dead-code eliminator.

    It uses DefaultASTParser's _local_defs and _calls to find definitions
    (functions, classes) that are never referenced in this file and not
    explicitly marked as exported.

    This is intentionally conservative:
        - Only top-level FunctionDef/ClassDef are considered.
        - Any name seen in the call table or in the exported list is kept.
        - Methods are never removed here; they are owned by their classes.
    """

    def __init__(
        self,
        parser: DefaultASTParser,
        exported: Optional[Sequence[str]] = None,
    ) -> None:
        self.parser = parser
        # Names that must not be removed (public API, tests, entry points, etc.).
        self.exported: set[str] = set(exported or [])
        # Populated by build_live_set()
        self.live_defs: set[str] = set()

    def build_live_set(self) -> None:
        """
        Compute the set of "live" definitions.

        A definition is considered live if:
            - Its name appears in _calls keys (direct or chained usage),
            - Or it is explicitly exported.
        """
        live = set(self.exported)

        # Any called name is considered live.  For a chained name like
        # "self.func", we also consider the last segment "func" as a candidate.
        for full_name, call in self.parser._calls.items():
            live.add(full_name)
            # Try to derive a simple base name; this is a heuristic.
            if '.' in full_name:
                simple = full_name.split('.')[-1]
                live.add(simple)

        self.live_defs = live

    def _is_removable_def(self, name: str, def_node: _DefNode) -> bool:
        """
        Decide whether a particular definition can be removed.

        Rules:
            - Never remove exported names.
            - Never remove names in the live set.
            - Only consider top-level functions and classes here.
            - Methods (_DefType.Method) are not removed by this pass.
        """
        if name in self.exported:
            return False
        if name in self.live_defs:
            return False
        # Only handle top-level Function and Class.
        if def_node.def_type not in (_DefType.Function, _DefType.Class):
            return False
        return True

    def transform(self) -> AST:
        """
        Return a modified AST where removable definitions are dropped
        from the module body.
        """
        # Build live set once.
        self.build_live_set()

        removable: set[str] = set()
        for name, def_node in self.parser._local_defs.items():
            if self._is_removable_def(name, def_node):
                removable.add(name)

        if not removable:
            return self.parser.ast

        class _DropUnusedTopLevel(NodeTransformer):
            def __init__(self, removable_names: set[str]) -> None:
                self._removable = removable_names

            def visit_Module(self, node: ast.Module) -> ast.AST:
                new_body = []
                for stmt in node.body:
                    if isinstance(stmt, (FunctionDef, ClassDef)):
                        if stmt.name in self._removable:
                            # Drop this top-level definition.
                            continue
                    new_body.append(stmt)
                node.body = new_body
                return node

        rewriter = _DropUnusedTopLevel(removable)
        return rewriter.visit(self.parser.ast)
