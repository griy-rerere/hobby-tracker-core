import pytest

from hobby_tracker.domain.hobby import HobbyName


def test_strips_name(hobby_name_str: str):
    name_string = "  \n\n\t\t " + hobby_name_str + "   \n\n\n\t\t\t       "
    name = HobbyName(name_string)

    assert name.value == hobby_name_str


def test_cannot_accept_empty():
    with pytest.raises(ValueError, match="Hobby name cannot be empty"):
        HobbyName("")


def test_cannot_accept_too_long():
    with pytest.raises(ValueError, match="Hobby name is too long"):
        HobbyName("A" * 51)


def test___str__(hobby_name_str: str, hobby_name: HobbyName):
    assert str(hobby_name) == hobby_name_str
