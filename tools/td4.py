class InLine:
    """Placeholder for inlining support."""

    def __call__(self, tree: AST) -> AST:
        # Future work: inline simple functions based on DefaultASTParser
        # call graph. For now this is a no-op.
        return tree
