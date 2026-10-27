
import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating_normal():
    assert module.first_non_repeating_char("swiss") == "w"


def test_first_non_repeating_first_character():
    assert module.first_non_repeating_char("apple") == "a"


def test_no_non_repeating_character():
    assert module.first_non_repeating_char("aabb") is None


def test_empty_string():
    assert module.first_non_repeating_char("") is None


# Python test code
