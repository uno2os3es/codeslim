    def _merge_property(self, node):
        # Copy over property-related functions that don't already exist.
        if not isinstance(node, FunctionDef):
            return node

        # Detect @property and @x.setter / @x.getter decorators.
        is_prop_like = False
        for deco in node.decorator_list:
            # @property
            if isinstance(deco, Name) and deco.id == "property":
                is_prop_like = True
                break
            # @x.setter / @x.getter / @x.deleter
            if isinstance(deco, Attribute) and isinstance(deco.value, Name):
                is_prop_like = True
                break

        if not is_prop_like:
            return node

        if node.name not in self.methods:
            # Append property-defining function to the merged class body.
            self.cls_node.body.append(node)
            self.methods[node.name] = node

        return node
