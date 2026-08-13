import pytest

from hobby_tracker.domain.activity import ActivityNote


def test_cannot_accept_empty():
    with pytest.raises(
        ValueError,
        match="Note cannot be empty string. Maybe you wanted to set note=None?",
    ):
        ActivityNote("")


@pytest.mark.parametrize("text", ["A" * 501, "TEXT" * 501])
def test_cannot_accept_too_long(text: str):
    with pytest.raises(ValueError, match="Note is too long"):
        ActivityNote(text)


def test___str__(activity_note_text: str, activity_note: ActivityNote):
    assert str(activity_note) == activity_note_text
