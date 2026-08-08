from unittest.mock import Mock

import pytest

from hobby_tracker.application.hobbies import GetHobby
from hobby_tracker.exceptions import HobbyNotFound


def test_get_hobby_returns_hobby(
    hobby_repository: Mock,
    hobby,
) -> None:
    hobby_repository.get.return_value = hobby

    use_case = GetHobby(hobby_repository)

    result = use_case(hobby.id)

    hobby_repository.get.assert_called_once_with(hobby.id)
    assert result is hobby


def test_get_hobby_propagates_hobby_not_found(
    hobby_repository: Mock,
    hobby_id,
) -> None:
    error = HobbyNotFound(hobby_id)
    hobby_repository.get.side_effect = error

    use_case = GetHobby(hobby_repository)

    with pytest.raises(HobbyNotFound) as exc_info:
        use_case(hobby_id)

    hobby_repository.get.assert_called_once_with(hobby_id)
    assert exc_info.value is error
