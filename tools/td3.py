class UnusedRemoval:
    """Simple unused symbol removal based on parser metadata."""

    def __init__(self, parser: DefaultASTParser):
        self.parser = parser

    def __call__(self, tree: AST) -> AST:
        # Very conservative: only remove local defs that are never called
        # and never imported externally (per parser metadata).
        used_names = set(self.parser._calls.keys())
        local_defs = self.parser._local_defs

        class _Remover(NodeTransformer):
            def visit_FunctionDef(self, node):
                if node.name in local_defs and node.name not in used_names:
                    return REMOVE_NODE
                return self.generic_visit(node)

        return _Remover().visit(tree)
