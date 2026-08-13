from unittest.mock import Mock
from uuid import UUID

from hobby_tracker.domain.activity import (
    Activity,
    ActivityDuration,
    ActivityNote,
    ActivityStart,
)


def test___init__(
    activity_id: UUID,
    hobby_id: UUID,
    activity_start: ActivityStart,
    activity_duration: ActivityDuration,
    activity_note: ActivityNote,
    activity: Activity,
):
    assert activity.id == activity_id
    assert activity.hobby_id == hobby_id
    assert activity.started_at == activity_start
    assert activity.duration == activity_duration
    assert activity.note == activity_note


def test_change_start(activity: Activity):
    new_start = Mock(spec=ActivityStart)
    activity.change_start(new_start)
    assert activity.started_at is new_start


def test_change_duration(activity: Activity):
    new_duration = Mock(spec=ActivityDuration)
    activity.change_duration(new_duration)
    assert activity.duration is new_duration


def test_set_note(activity: Activity):
    note = Mock(spec=ActivityNote)
    activity.set_note(note)
    assert activity.note is note


def test_delete_note(activity: Activity):
    activity.delete_note()
    assert activity.note is None
