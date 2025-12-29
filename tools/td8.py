class ClassEntry(SegmentEntry):
    def __init__(self, class_nodes: Union[ClassDef, Sequence[ClassDef]]):
        entries = [class_nodes] if isinstance(class_nodes, ClassDef) else list(class_nodes)
        self.entries = entries
        self.ast = self.convert_to_ast(entries)

    def convert_to_ast(self, entries):
        # For simplicity, pack all classes into a single module.
        module = ast.Module(body=list(entries), type_ignores=[])
        return module
