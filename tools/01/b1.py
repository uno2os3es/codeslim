def rewrite_defs(self, node: Union[FunctionDef, ClassDef]):
    if node.name not in self.extern_used and node.name not in self.local_used:
        return REMOVE_NODE
    return node
