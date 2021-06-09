"""bot util functions and variables"""

import os


def data_path():
    """get the bot data path"""
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(file_path)
    return os.path.join(path, "..", "..", "data")
