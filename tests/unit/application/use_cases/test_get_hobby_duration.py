from datetime import date, timedelta
from unittest.mock import Mock
from uuid import uuid7

from hobby_tracker.application.requests import GetHobbyDurationRequest
from hobby_tracker.application.use_cases import GetHobbyDuration
from hobby_tracker.domain import DateRange


def test_get_hobby_duration_returns_repository_result(
    activity_entry_repository: Mock,
) -> None:
    expected_duration = timedelta(hours=5)

    activity_entry_repository.get_hobby_sum.return_value = expected_duration

    use_case = GetHobbyDuration(activity_entry_repository)

    request = GetHobbyDurationRequest(
        hobby_id=uuid7(),
        date_range=DateRange(
            start=date(2026, 8, 1),
            end=date(2026, 8, 6),
        ),
    )

    result = use_case(request)

    assert result == expected_duration


def test_get_hobby_duration_calls_repository_with_request_data(
    activity_entry_repository: Mock,
) -> None:
    hobby_id = uuid7()

    date_range = DateRange(
        start=date(2026, 8, 1),
        end=date(2026, 8, 6),
    )

    use_case = GetHobbyDuration(activity_entry_repository)

    request = GetHobbyDurationRequest(
        hobby_id=hobby_id,
        date_range=date_range,
    )

    use_case(request)

    activity_entry_repository.get_hobby_sum.assert_called_once_with(
        hobby_id,
        date_range,
    )


def test_get_hobby_duration_returns_zero_when_repository_returns_zero(
    activity_entry_repository: Mock,
) -> None:
    activity_entry_repository.get_hobby_sum.return_value = timedelta(0)

    use_case = GetHobbyDuration(activity_entry_repository)

    result = use_case(
        GetHobbyDurationRequest(
            hobby_id=uuid7(),
            date_range=DateRange(
                start=date(2026, 8, 1),
                end=date(2026, 8, 6),
            ),
        )
    )

    assert result == timedelta(0)
