import os


def get_path(filename):
    return os.path.join(
        os.path.dirname(__file__),
        "../fixtures",
        filename
    )
