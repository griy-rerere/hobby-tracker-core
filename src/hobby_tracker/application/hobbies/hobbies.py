from hobby_tracker.ports import HobbyRepository

from .create import CreateHobby
from .get import GetHobby
from .get_all import GetAllHobbies


class Hobbies:
    def __init__(self, hobby_repo: HobbyRepository) -> None:
        self.create = CreateHobby(hobby_repo)
        self.get = GetHobby(hobby_repo)
        self.get_all = GetAllHobbies(hobby_repo)
