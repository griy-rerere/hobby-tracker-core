from uuid import uuid7

import pytest
from hobby_tracker.domain import Hobby


def test_hobby_creates_with_name(hobby: Hobby, hobby_name: str) -> None:
    assert hobby.name == hobby_name
    assert hobby.id is not None


def test_hobby_generates_uuid() -> None:
    hobby = Hobby(name="Guitar")

    assert hobby.id.version == 7


def test_hobby_strips_name_whitespace() -> None:
    hobby = Hobby(name="  Guitar  ")

    assert hobby.name == "Guitar"


@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "     ",
    ],
)
def test_hobby_rejects_empty_names(name: str) -> None:
    with pytest.raises(
        ValueError,
        match="Hobby name cannot be empty",
    ):
        Hobby(name=name)


def test_hobby_rejects_long_name() -> None:
    with pytest.raises(
        ValueError,
        match="Hobby name is too long",
    ):
        Hobby(name="a" * 51)


def test_hobby_can_be_reconstructed() -> None:
    hobby_id = uuid7()

    hobby = Hobby(
        id=hobby_id,
        name="Guitar",
    )

    assert hobby.id == hobby_id
    assert hobby.name == "Guitar"


def test_hobby_is_immutable(hobby: Hobby) -> None:
    with pytest.raises(AttributeError):
        hobby.name = "Drawing"


def test_hobby_equality_depends_on_all_fields() -> None:
    hobby_id = uuid7()

    hobby_1 = Hobby(
        id=hobby_id,
        name="Guitar",
    )

    hobby_2 = Hobby(
        id=hobby_id,
        name="Guitar",
    )

    assert hobby_1 == hobby_2
