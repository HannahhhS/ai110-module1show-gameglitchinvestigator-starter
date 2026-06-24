# Placing an (empty) conftest.py at the project root tells pytest to add the
# root directory to sys.path, so tests in tests/ can `import logic_utils`
# regardless of where pytest is launched from.
