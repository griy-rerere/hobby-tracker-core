from datetime import date
from unittest.mock import Mock

from hobby_tracker.application.activities import GetActivityStatistics
from hobby_tracker.domain.date_range import DateRange
from hobby_tracker.queries import ActivityStatisticsQuery


def test_get_activities_statistics_returns_repository_result(
    activity_repository: Mock,
    activity_statistics,
    hobby_id,
) -> None:
    activity_repository.calculate_statistics.return_value = activity_statistics

    query = ActivityStatisticsQuery(
        hobby_ids=[hobby_id],
        date_range=DateRange(
            start=date(2026, 8, 1),
            end=date(2026, 8, 8),
        ),
    )

    use_case = GetActivityStatistics(activity_repository)

    result = use_case(query)

    activity_repository.calculate_statistics.assert_called_once_with(query)
    assert result is activity_statistics


def test_get_activities_statistics_passes_query_without_modification(
    activity_repository: Mock,
    hobby_id,
) -> None:
    query = ActivityStatisticsQuery(
        hobby_ids=[hobby_id],
        date_range=DateRange(
            start=date(2026, 8, 1),
            end=date(2026, 8, 8),
        ),
    )

    activity_repository.calculate_statistics.return_value = None

    use_case = GetActivityStatistics(activity_repository)

    use_case(query)

    activity_repository.calculate_statistics.assert_called_once_with(query)
