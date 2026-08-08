from unittest.mock import Mock

import pytest

from hobby_tracker.application.activities import GetActivity
from hobby_tracker.exceptions import ActivityNotFound


def test_get_activity_returns_activity(
    activity_repository: Mock,
    activity,
) -> None:
    activity_repository.get.return_value = activity

    use_case = GetActivity(activity_repository)

    result = use_case(activity.id)

    activity_repository.get.assert_called_once_with(activity.id)
    assert result is activity


def test_get_activity_propagates_activity_not_found(
    activity_repository: Mock,
    activity_id,
) -> None:
    error = ActivityNotFound(activity_id)
    activity_repository.get.side_effect = error

    use_case = GetActivity(activity_repository)

    with pytest.raises(ActivityNotFound) as exc_info:
        use_case(activity_id)

    activity_repository.get.assert_called_once_with(activity_id)
    assert exc_info.value is error
