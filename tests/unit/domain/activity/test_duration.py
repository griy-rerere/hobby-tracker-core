from datetime import timedelta

import pytest

from hobby_tracker.domain.activity import ActivityDuration


@pytest.mark.parametrize("minutes", [0, -10])
def test_must_be_positive(minutes: int):
    with pytest.raises(ValueError, match="ActivityDuration must be positive"):
        ActivityDuration(minutes)


@pytest.mark.parametrize("minutes", [24 * 60, 24 * 60 + 1])
def test_cannot_be_day_or_more(minutes: int):
    with pytest.raises(
        ValueError, match="ActivityDuration cannot be the whole day or more"
    ):
        ActivityDuration(minutes)


def test_hours(activity_duration_minutes: int, activity_duration: ActivityDuration):
    assert activity_duration.hours() == activity_duration_minutes / 60


def test_timedelta(activity_duration_minutes: int, activity_duration: ActivityDuration):
    assert activity_duration.timedelta() == timedelta(minutes=activity_duration_minutes)
