import os.path as path
from pathlib import Path


def abs_curdir_path(file):
    """Fetches the absolute path of the directory containing a file."""
    return str(Path(file).parent.resolve())


def abs_curdirfile_path(file, file_path):
    """Fetches the absolute path of a another file in the current directory."""
    return path.join(abs_curdir_path(file), file_path)
