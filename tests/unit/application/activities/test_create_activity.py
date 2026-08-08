from datetime import timedelta
from unittest.mock import Mock

import pytest

from hobby_tracker.application.activities import CreateActivity
from hobby_tracker.application.requests import CreateActivityRequest
from hobby_tracker.exceptions import HobbyNotFound


def test_create_activity_saves_activity(
    activity_repository: Mock,
    hobby_id,
    started_at,
) -> None:
    use_case = CreateActivity(activity_repository)

    request = CreateActivityRequest(
        hobby_id=hobby_id,
        duration=timedelta(minutes=45),
        started_at=started_at,
        note="Practiced scales",
    )

    result = use_case(request)

    activity_repository.save.assert_called_once()

    saved_activity = activity_repository.save.call_args.args[0]

    assert saved_activity.hobby_id == hobby_id
    assert saved_activity.duration == timedelta(minutes=45)
    assert saved_activity.started_at == started_at
    assert saved_activity.note == "Practiced scales"
    assert result is saved_activity


def test_create_activity_generates_activity_id(
    activity_repository: Mock,
    hobby_id,
    started_at,
) -> None:
    use_case = CreateActivity(activity_repository)

    request = CreateActivityRequest(
        hobby_id=hobby_id,
        duration=timedelta(minutes=45),
        started_at=started_at,
    )

    result = use_case(request)

    assert result.id is not None


def test_create_activity_uses_current_time_when_started_at_is_none(
    activity_repository: Mock,
    hobby_id,
) -> None:
    use_case = CreateActivity(activity_repository)

    request = CreateActivityRequest(
        hobby_id=hobby_id,
        duration=timedelta(minutes=45),
        started_at=None,
    )

    result = use_case(request)

    assert result.started_at is not None
    assert result.started_at.tzinfo is not None
    assert result.started_at.utcoffset() is not None


def test_create_activity_propagates_hobby_not_found(
    activity_repository: Mock,
    hobby_id,
) -> None:
    error = HobbyNotFound(hobby_id)
    activity_repository.save.side_effect = error

    use_case = CreateActivity(activity_repository)

    request = CreateActivityRequest(
        hobby_id=hobby_id,
        duration=timedelta(minutes=45),
    )

    with pytest.raises(HobbyNotFound) as exc_info:
        use_case(request)

    assert exc_info.value is error
