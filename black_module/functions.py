import os


def open_up_this_here_file(
    filepath: os.PathLike,
    read_method: str = "w",
    verbose: bool = True,
    debug: bool = False,
):
    """Does a whole bunch of things this one function does right here."""
    with open(filepath, read_method) as f:
        print(f.read())
