from unittest.mock import Mock

import pytest

from hobby_tracker.ports import ActivityEntryRepository, HobbyRepository


@pytest.fixture
def hobby_repository() -> Mock:
    return Mock(spec=HobbyRepository)


@pytest.fixture
def activity_entry_repository() -> Mock:
    return Mock(spec=ActivityEntryRepository)
