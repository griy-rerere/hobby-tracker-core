from datetime import datetime, timedelta, timezone
from unittest.mock import Mock
from uuid import uuid7

import pytest

from hobby_tracker.application.activities import CreateActivity
from hobby_tracker.application.requests import CreateActivityRequest
from hobby_tracker.domain import Activity


def test_create_activity_creates_activity(
    activity_repository: Mock,
) -> None:
    use_case = CreateActivity(activity_repository)

    hobby_id = uuid7()

    result = use_case(
        CreateActivityRequest(
            hobby_id=hobby_id,
            duration=timedelta(minutes=30),
        )
    )

    assert isinstance(result, Activity)
    assert result.hobby_id == hobby_id
    assert result.duration == timedelta(minutes=30)


def test_create_activity_saves_created(
    activity_repository: Mock,
) -> None:
    use_case = CreateActivity(activity_repository)

    result = use_case(
        CreateActivityRequest(
            hobby_id=uuid7(),
            duration=timedelta(hours=1),
        )
    )

    activity_repository.save.assert_called_once_with(result)


def test_create_activity_returns_saved(
    activity_repository: Mock,
) -> None:
    use_case = CreateActivity(activity_repository)

    result = use_case(
        CreateActivityRequest(
            hobby_id=uuid7(),
            duration=timedelta(minutes=45),
        )
    )

    saved = activity_repository.save.call_args.args[0]

    assert result is saved


def test_create_activity_uses_provided_started_at(
    activity_repository: Mock,
) -> None:
    use_case = CreateActivity(activity_repository)

    started_at = datetime(
        2026,
        8,
        5,
        18,
        30,
        tzinfo=timezone.utc,
    )

    result = use_case(
        CreateActivityRequest(
            hobby_id=uuid7(),
            duration=timedelta(minutes=40),
            started_at=started_at,
        )
    )

    assert result.started_at == started_at


def test_create_activity_sets_current_time_when_started_at_missing(
    activity_repository: Mock,
) -> None:
    use_case = CreateActivity(activity_repository)

    before = datetime.now(timezone.utc)

    result = use_case(
        CreateActivityRequest(
            hobby_id=uuid7(),
            duration=timedelta(minutes=20),
        )
    )

    after = datetime.now(timezone.utc)

    assert before <= result.started_at <= after


@pytest.mark.parametrize(
    "duration",
    [
        timedelta(0),
        timedelta(seconds=-1),
        timedelta(minutes=-10),
    ],
)
def test_create_activity_rejects_invalid_duration(
    activity_repository: Mock,
    duration: timedelta,
) -> None:
    use_case = CreateActivity(activity_repository)

    with pytest.raises(
        ValueError,
        match="Activity duration must be positive",
    ):
        use_case(
            CreateActivityRequest(
                hobby_id=uuid7(),
                duration=duration,
            )
        )

    activity_repository.save.assert_not_called()


@pytest.mark.parametrize(
    "note",
    [
        "a" * 501,
        "b" * 1000,
    ],
)
def test_create_activity_rejects_too_long_note(
    activity_repository: Mock,
    note: str,
) -> None:
    use_case = CreateActivity(activity_repository)

    with pytest.raises(
        ValueError,
        match="Note is too long",
    ):
        use_case(
            CreateActivityRequest(
                hobby_id=uuid7(),
                duration=timedelta(minutes=30),
                note=note,
            )
        )

    activity_repository.save.assert_not_called()
