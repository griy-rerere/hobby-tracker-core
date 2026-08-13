from datetime import datetime, timezone
from uuid import UUID

import pytest

from hobby_tracker.domain.activity import (
    Activity,
    ActivityDuration,
    ActivityNote,
    ActivityStart,
)
from hobby_tracker.domain.hobby import Hobby, HobbyName


@pytest.fixture
def hobby_id() -> UUID:
    return "019ffafc-b87d-7329-b62a-814bf092d5f1"


@pytest.fixture
def hobby_name_str() -> str:
    return "Guitar"


@pytest.fixture
def hobby_name(hobby_name_str: str) -> HobbyName:
    return HobbyName(hobby_name_str)


@pytest.fixture
def hobby(hobby_name: HobbyName, hobby_id: UUID) -> Hobby:
    return Hobby(id=hobby_id, name=hobby_name)


@pytest.fixture
def activity_id() -> UUID:
    return "019ffb14-49cd-7082-9642-0e320272aa9a"


@pytest.fixture
def activity_start_datetime() -> datetime:
    return datetime(2026, 8, 13, 12, 18, tzinfo=timezone.utc)


@pytest.fixture
def activity_start(activity_start_datetime: datetime) -> ActivityStart:
    return ActivityStart(activity_start_datetime)


@pytest.fixture
def activity_duration_minutes() -> int:
    return 90


@pytest.fixture
def activity_duration(activity_duration_minutes: int) -> ActivityDuration:
    return ActivityDuration(activity_duration_minutes)


@pytest.fixture
def activity_note_text() -> str:
    return "Writing Hobby tracker tests"


@pytest.fixture
def activity_note(activity_note_text: str) -> str:
    return ActivityNote(activity_note_text)


@pytest.fixture
def activity(
    activity_id: UUID,
    hobby_id: UUID,
    activity_start: ActivityStart,
    activity_duration: ActivityDuration,
    activity_note: ActivityNote,
) -> Activity:
    return Activity(
        id=activity_id,
        hobby_id=hobby_id,
        started_at=activity_start,
        duration=activity_duration,
        note=activity_note,
    )
