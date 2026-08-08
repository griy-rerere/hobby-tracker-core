from datetime import datetime, timedelta, timezone
from uuid import uuid7

import pytest

from hobby_tracker.domain import Activity


def test_activity_creates(activity: Activity) -> None:
    assert activity.duration == timedelta(minutes=30)
    assert activity.note == "Practice scales"


def test_activity_generates_uuid(
    hobby_id,
) -> None:
    activity = Activity(
        hobby_id=hobby_id,
        duration=timedelta(minutes=30),
    )

    assert activity.id.version == 7


@pytest.mark.parametrize(
    "duration",
    [
        timedelta(0),
        timedelta(seconds=-1),
        timedelta(minutes=-10),
    ],
)
def test_activity_rejects_invalid_duration(
    hobby_id,
    duration: timedelta,
) -> None:
    with pytest.raises(
        ValueError,
        match="Activity duration must be positive",
    ):
        Activity(
            hobby_id=hobby_id,
            duration=duration,
        )


def test_activity_rejects_long_note(hobby_id) -> None:
    with pytest.raises(
        ValueError,
        match="Note is too long",
    ):
        Activity(
            hobby_id=hobby_id,
            duration=timedelta(minutes=30),
            note="a" * 501,
        )


def test_activity_can_be_reconstructed(
    hobby_id,
    fixed_datetime,
) -> None:
    activity_id = uuid7()

    activity = Activity(
        id=activity_id,
        hobby_id=hobby_id,
        started_at=fixed_datetime,
        duration=timedelta(minutes=45),
        note="Training",
    )

    assert activity.id == activity_id
    assert activity.hobby_id == hobby_id
    assert activity.started_at == fixed_datetime
    assert activity.duration == timedelta(minutes=45)
    assert activity.note == "Training"


def test_activity_is_immutable(
    activity: Activity,
) -> None:
    with pytest.raises(AttributeError):
        activity.duration = timedelta(hours=2)


def test_activity_equality_depends_on_all_fields(
    hobby_id,
) -> None:
    activity_id = uuid7()
    started_at = datetime(2026, 1, 1, tzinfo=timezone.utc)

    activity_1 = Activity(
        id=activity_id,
        hobby_id=hobby_id,
        started_at=started_at,
        duration=timedelta(minutes=30),
    )

    activity_2 = Activity(
        id=activity_id,
        hobby_id=hobby_id,
        started_at=started_at,
        duration=timedelta(minutes=30),
    )

    assert activity_1 == activity_2
