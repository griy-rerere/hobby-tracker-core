from unittest.mock import Mock

import pytest

from hobby_tracker.ports import ActivityRepository, HobbyRepository


@pytest.fixture
def hobby_repository() -> Mock:
    return Mock(spec=HobbyRepository)


@pytest.fixture
def activity_repository() -> Mock:
    return Mock(spec=ActivityRepository)
