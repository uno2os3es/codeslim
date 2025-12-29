    # TODO
    def _rewrite_super(self):
        # For now, do nothing. A correct implementation would:
        # 1. Walk methods moved from base classes.
        # 2. Rewrite `super(Base, self)` or bare `super()` to refer to the
        #    new merged class hierarchy, preserving semantics.
        # This requires knowing the full MRO and is non-trivial, so it is
        # intentionally left as a no-op.
        return
