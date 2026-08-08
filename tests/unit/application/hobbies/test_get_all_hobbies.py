from unittest.mock import Mock

from hobby_tracker.application.hobbies import GetAllHobbies


def test_get_hobbies_returns_repository_result(
    hobby_repository: Mock,
    hobby,
    another_hobby,
) -> None:
    expected = [hobby, another_hobby]
    hobby_repository.get_all.return_value = expected

    use_case = GetAllHobbies(hobby_repository)

    result = use_case()

    hobby_repository.get_all.assert_called_once()
    assert result is expected


def test_get_hobbies_returns_empty_list(
    hobby_repository: Mock,
) -> None:
    hobby_repository.get_all.return_value = []

    use_case = GetAllHobbies(hobby_repository)

    result = use_case()

    hobby_repository.get_all.assert_called_once()
    assert result == []
