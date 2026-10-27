import importlib

module = importlib.import_module("32_count_words")


def test_count_normal_sentence():
    assert module.count_words("Python is easy to learn") == 5


def test_count_empty_sentence():
    assert module.count_words("") == 0


def test_count_extra_spaces():
    assert module.count_words("  Hello   world  ") == 2