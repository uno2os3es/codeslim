# After building a DefaultASTParser `p` for a file:
unused = UnusedRemoval(p, exported=['main', '__all__'])
new_ast = unused.transform()
p.ast = new_ast  # if you want downstream passes to see the pruned AST
