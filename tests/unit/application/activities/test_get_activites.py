from datetime import date
from unittest.mock import Mock

from hobby_tracker.application.activities import GetActivities
from hobby_tracker.domain.date_range import DateRange
from hobby_tracker.queries import ActivityQuery


def test_get_activities_returns_repository_result(
    activity_repository: Mock,
    activity,
    another_activity,
    hobby_id,
) -> None:
    expected = [activity, another_activity]
    activity_repository.get_many.return_value = expected

    query = ActivityQuery(
        hobby_ids=[hobby_id],
        date_range=DateRange(
            start=date(2026, 8, 1),
            end=date(2026, 8, 8),
        ),
    )

    use_case = GetActivities(activity_repository)

    result = use_case(query)

    activity_repository.get_many.assert_called_once_with(query)
    assert result is expected


def test_get_activities_returns_empty_list(
    activity_repository: Mock,
) -> None:
    activity_repository.get_many.return_value = []

    query = ActivityQuery()

    use_case = GetActivities(activity_repository)

    result = use_case(query)

    activity_repository.get_many.assert_called_once_with(query)
    assert result == []
