from unittest.mock import Mock

import pytest

from hobby_tracker.application.hobbies import CreateHobby
from hobby_tracker.application.requests import CreateHobbyRequest
from hobby_tracker.exceptions import HobbyTrackerException


def test_create_hobby_saves_hobby(
    hobby_repository: Mock,
) -> None:
    use_case = CreateHobby(hobby_repository)
    request = CreateHobbyRequest(name="Guitar")

    result = use_case(request)

    hobby_repository.save.assert_called_once()

    saved_hobby = hobby_repository.save.call_args.args[0]

    assert saved_hobby.name == "Guitar"
    assert result is saved_hobby


def test_create_hobby_generates_hobby_id(
    hobby_repository: Mock,
) -> None:
    use_case = CreateHobby(hobby_repository)
    request = CreateHobbyRequest(name="Guitar")

    result = use_case(request)

    assert result.id is not None
    assert hobby_repository.save.call_args.args[0] is result


def test_create_hobby_propagates_repository_error(
    hobby_repository: Mock,
) -> None:
    error = HobbyTrackerException()
    hobby_repository.save.side_effect = error

    use_case = CreateHobby(hobby_repository)
    request = CreateHobbyRequest(name="Guitar")

    with pytest.raises(HobbyTrackerException) as exc_info:
        use_case(request)

    assert exc_info.value is error
