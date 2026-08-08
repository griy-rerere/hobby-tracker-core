from datetime import date, datetime, timedelta, timezone
from unittest.mock import Mock
from uuid import UUID

import pytest

from hobby_tracker.domain import Activity, ActivityStatistics, DateRange, Hobby
from hobby_tracker.ports import ActivityRepository, HobbyRepository


@pytest.fixture
def hobby_repository() -> Mock:
    return Mock(spec=HobbyRepository)


@pytest.fixture
def activity_repository() -> Mock:
    return Mock(spec=ActivityRepository)


@pytest.fixture
def hobby_id() -> UUID:
    return UUID("0190c0de-0000-7000-8000-000000000001")


@pytest.fixture
def another_hobby_id() -> UUID:
    return UUID("0190c0de-0000-7000-8000-000000000002")


@pytest.fixture
def activity_id() -> UUID:
    return UUID("0190c0de-0000-7000-8000-000000000003")


@pytest.fixture
def another_activity_id() -> UUID:
    return UUID("0190c0de-0000-7000-8000-000000000004")


@pytest.fixture
def started_at() -> datetime:
    return datetime(2026, 8, 8, 10, 30, tzinfo=timezone.utc)


@pytest.fixture
def hobby(hobby_id: UUID) -> Hobby:
    return Hobby(
        id=hobby_id,
        name="Guitar",
    )


@pytest.fixture
def another_hobby(another_hobby_id: UUID) -> Hobby:
    return Hobby(
        id=another_hobby_id,
        name="Drawing",
    )


@pytest.fixture
def activity(
    activity_id: UUID,
    hobby_id: UUID,
    started_at: datetime,
) -> Activity:
    return Activity(
        id=activity_id,
        hobby_id=hobby_id,
        duration=timedelta(minutes=45),
        started_at=started_at,
        note="Practiced scales",
    )


@pytest.fixture
def another_activity(
    another_activity_id: UUID,
    hobby_id: UUID,
    started_at: datetime,
) -> Activity:
    return Activity(
        id=another_activity_id,
        hobby_id=hobby_id,
        duration=timedelta(minutes=30),
        started_at=started_at + timedelta(hours=1),
        note=None,
    )


@pytest.fixture
def date_range() -> DateRange:
    return DateRange(
        start=date(2026, 8, 1),
        end=date(2026, 8, 8),
    )


@pytest.fixture
def activity_statistics() -> ActivityStatistics:
    return ActivityStatistics(
        total_duration=timedelta(hours=2),
        activity_count=4,
        avg_duration=timedelta(minutes=30),
    )
