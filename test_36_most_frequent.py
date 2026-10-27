import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent():
    assert module.most_frequent([1, 3, 2, 3, 4, 3]) == 3


def test_tied_frequency():
    assert module.most_frequent([1, 2, 1, 2]) == 1


def test_single_element():
    assert module.most_frequent([7]) == 7


def test_empty_list():
    assert module.most_frequent([]) is None