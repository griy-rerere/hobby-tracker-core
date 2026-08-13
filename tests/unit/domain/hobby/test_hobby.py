from uuid import UUID

from hobby_tracker.domain.hobby import Hobby, HobbyName


def test___init__(hobby_name: HobbyName, hobby_id: UUID, hobby: Hobby):
    assert hobby._name == hobby_name
    assert hobby._id == hobby_id


def test_properites(hobby: Hobby):
    assert hobby.id == hobby._id
    assert hobby.name == hobby._name


def test_rename(hobby: Hobby):
    new_name = HobbyName("Drawing")
    hobby.rename(new_name)

    assert hobby.name == new_name
