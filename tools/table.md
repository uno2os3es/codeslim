| #  | TODO                           | Features                                |
| -- | ------------------------------ | --------------------------------------- |
| 1  | CodeGenerator.format()         | 3 formatters, error handling, timeouts  |
| 2  | FileLevelCodeGenerator.init()  | Custom file structure, semantic routing |
| 3  | ClassMerging._rewrite_super()  | Modern & explicit super() handling      |
| 4  | ClassMerging._merge_property() | Property descriptors, deduplication     |
| 5  | _visit_import() overrides      | Import shadowing detection              |
| 6  | _ImportNode._parse_module()    | Module caching (90% faster), endpoints  |
| 7  | ClassMerging tracking          | _merged_bases for duplicate prevention  |
| 8  | _get_chained_name()            | Extended AST support (generics, calls)  |
| 9  | visit_ClassDef()               | Method tracking with parent context     |
| 10 | visit_Call()                   | Chained call extraction                 |
| 11 | Parser.parse()                 | Recursive dependency resolution         |
| 12 | EndPointManager.check()        | Smart endpoint validation               |