from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid7

import pytest

from hobby_tracker.domain import Activity, Hobby


@pytest.fixture
def hobby_name() -> str:
    return "Guitar"


@pytest.fixture
def hobby(hobby_name: str) -> Hobby:
    return Hobby(name=hobby_name)


@pytest.fixture
def hobby_id() -> UUID:
    return uuid7()


@pytest.fixture
def activity(hobby_id: UUID) -> Activity:
    return Activity(
        hobby_id=hobby_id,
        duration=timedelta(minutes=30),
        note="Practice scales",
    )


@pytest.fixture
def fixed_datetime() -> datetime:
    return datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
