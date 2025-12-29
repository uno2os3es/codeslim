class SegmentEntry(Entry):
    def __init__(self, nodes: Union[AST, Sequence[AST]]) -> None:
        entries = [nodes] if isinstance(nodes, AST) else list(nodes)
        self.entries = entries
        self.asts = self.convert_to_ast(self.entries)

    def convert_to_ast(self, entries):
        # Assume each entry is already an AST node; wrap each in a Module.
        return [ast.Module(body=[n], type_ignores=[]) for n in entries]

    def get_cache(self):
        return []
