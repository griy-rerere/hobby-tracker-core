from unittest.mock import Mock

import pytest

from hobby_tracker.application.hobbies import CreateHobby
from hobby_tracker.application.requests import CreateHobbyRequest
from hobby_tracker.domain import Hobby


def test_create_hobby_creates_hobby(
    hobby_repository: Mock,
) -> None:
    use_case = CreateHobby(hobby_repository)

    result = use_case(
        CreateHobbyRequest(
            name="Guitar",
        )
    )

    assert isinstance(result, Hobby)
    assert result.name == "Guitar"


def test_create_hobby_saves_created_hobby(
    hobby_repository: Mock,
) -> None:
    use_case = CreateHobby(hobby_repository)

    result = use_case(
        CreateHobbyRequest(
            name="Drawing",
        )
    )

    hobby_repository.save.assert_called_once_with(result)


def test_create_hobby_returns_created_hobby(
    hobby_repository: Mock,
) -> None:
    use_case = CreateHobby(hobby_repository)

    result = use_case(
        CreateHobbyRequest(
            name="Programming",
        )
    )

    saved_hobby = hobby_repository.save.call_args.args[0]

    assert result is saved_hobby


def test_create_hobby_rejects_empty_name(
    hobby_repository: Mock,
) -> None:
    use_case = CreateHobby(hobby_repository)

    with pytest.raises(ValueError):
        use_case(
            CreateHobbyRequest(
                name="   ",
            )
        )

    hobby_repository.save.assert_not_called()


def test_create_hobby_trims_name(
    hobby_repository: Mock,
) -> None:
    use_case = CreateHobby(hobby_repository)

    result = use_case(
        CreateHobbyRequest(
            name="  Guitar  ",
        )
    )

    assert result.name == "Guitar"
    hobby_repository.save.assert_called_once_with(result)
