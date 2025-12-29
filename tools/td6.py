class StringEntry(Entry):
    def __init__(self, source: Union[str, Sequence[str]]) -> None:
        entries = [source] if isinstance(source, str) else list(source)
        self.entries = entries
        self.asts = self.convert_to_ast(self.entries)

    def convert_to_ast(self, entries):
        return [ast.parse(s) for s in entries]

    def get_cache(self):
        # No filesystem cache for strings.
        return []
