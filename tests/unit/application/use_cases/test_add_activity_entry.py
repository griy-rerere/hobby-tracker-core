from datetime import datetime, timedelta, timezone
from unittest.mock import Mock
from uuid import uuid7

import pytest

from hobby_tracker.application.requests import AddActivityEntryRequest
from hobby_tracker.application.use_cases import AddActivityEntry
from hobby_tracker.domain import ActivityEntry


def test_add_activity_entry_creates_entry(
    activity_entry_repository: Mock,
) -> None:
    use_case = AddActivityEntry(activity_entry_repository)

    hobby_id = uuid7()

    result = use_case(
        AddActivityEntryRequest(
            hobby_id=hobby_id,
            duration=timedelta(minutes=30),
        )
    )

    assert isinstance(result, ActivityEntry)
    assert result.hobby_id == hobby_id
    assert result.duration == timedelta(minutes=30)


def test_add_activity_entry_saves_created_entry(
    activity_entry_repository: Mock,
) -> None:
    use_case = AddActivityEntry(activity_entry_repository)

    result = use_case(
        AddActivityEntryRequest(
            hobby_id=uuid7(),
            duration=timedelta(hours=1),
        )
    )

    activity_entry_repository.save.assert_called_once_with(result)


def test_add_activity_entry_returns_saved_entry(
    activity_entry_repository: Mock,
) -> None:
    use_case = AddActivityEntry(activity_entry_repository)

    result = use_case(
        AddActivityEntryRequest(
            hobby_id=uuid7(),
            duration=timedelta(minutes=45),
        )
    )

    saved_entry = activity_entry_repository.save.call_args.args[0]

    assert result is saved_entry


def test_add_activity_entry_uses_provided_started_at(
    activity_entry_repository: Mock,
) -> None:
    use_case = AddActivityEntry(activity_entry_repository)

    started_at = datetime(
        2026,
        8,
        5,
        18,
        30,
        tzinfo=timezone.utc,
    )

    result = use_case(
        AddActivityEntryRequest(
            hobby_id=uuid7(),
            duration=timedelta(minutes=40),
            started_at=started_at,
        )
    )

    assert result.started_at == started_at


def test_add_activity_entry_sets_current_time_when_started_at_missing(
    activity_entry_repository: Mock,
) -> None:
    use_case = AddActivityEntry(activity_entry_repository)

    before = datetime.now(timezone.utc)

    result = use_case(
        AddActivityEntryRequest(
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
def test_add_activity_entry_rejects_invalid_duration(
    activity_entry_repository: Mock,
    duration: timedelta,
) -> None:
    use_case = AddActivityEntry(activity_entry_repository)

    with pytest.raises(
        ValueError,
        match="Activity duration must be positive",
    ):
        use_case(
            AddActivityEntryRequest(
                hobby_id=uuid7(),
                duration=duration,
            )
        )

    activity_entry_repository.save.assert_not_called()


@pytest.mark.parametrize(
    "note",
    [
        "a" * 501,
        "b" * 1000,
    ],
)
def test_add_activity_entry_rejects_too_long_note(
    activity_entry_repository: Mock,
    note: str,
) -> None:
    use_case = AddActivityEntry(activity_entry_repository)

    with pytest.raises(
        ValueError,
        match="Note is too long",
    ):
        use_case(
            AddActivityEntryRequest(
                hobby_id=uuid7(),
                duration=timedelta(minutes=30),
                note=note,
            )
        )

    activity_entry_repository.save.assert_not_called()
