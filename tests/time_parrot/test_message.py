from time_parrot.message import time


def test_time():
    """
    TODO
    """
    result = time()
    assert result.startswith("Hello! The time is ")
