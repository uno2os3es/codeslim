    # Do we need to format generated code?
    def format(self, file_path):
        """Optionally format generated code in-place."""
        try:
            # Example: use `black` if installed.
            import subprocess

            subprocess.run(
                ["black", file_path],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception:
            # Formatting is best-effort; ignore any failures.
            pass
