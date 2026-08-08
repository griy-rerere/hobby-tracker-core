from datetime import date, datetime

import pytest

from hobby_tracker.domain import DateRange


def test_date_range_creates_with_valid_boundaries() -> None:
    date_range = DateRange(
        start=date(2026, 1, 1),
        end=date(2026, 1, 31),
    )

    assert date_range.start == date(2026, 1, 1)
    assert date_range.end == date(2026, 1, 31)


def test_date_range_allows_same_start_and_end_date() -> None:
    same_date = date(2026, 1, 1)

    date_range = DateRange(
        start=same_date,
        end=same_date,
    )

    assert date_range.start == date_range.end


def test_date_range_rejects_start_after_end() -> None:
    with pytest.raises(
        ValueError,
        match="Start date cannot be after end date",
    ):
        DateRange(
            start=date(2026, 2, 1),
            end=date(2026, 1, 31),
        )


def test_date_range_is_immutable() -> None:
    date_range = DateRange(
        start=date(2026, 1, 1),
        end=date(2026, 1, 31),
    )

    with pytest.raises(AttributeError):
        date_range.start = date(2026, 2, 1)


def test_date_range_checks_containing() -> None:
    date_range = DateRange(
        start=date(2026, 8, 7),
        end=date(2026, 8, 9),
    )
    assert datetime(2026, 8, 8, 12, 30) in date_range
    assert datetime(2026, 8, 10, 0, 0) not in date_range

    test_day = date(2026, 8, 8)
    date_range_oneday = DateRange(test_day, test_day)
    test_datetime = datetime(2026, 8, 8, 12, 30)

    assert test_datetime in date_range_oneday
