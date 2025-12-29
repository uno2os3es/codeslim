    def get_target_import_names(self):
        return [name for name, v in self._imports.items() if v.is_target]
