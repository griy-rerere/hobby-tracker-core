import re
from datetime import datetime, timezone
from unittest.mock import MagicMock, Mock, patch
from uuid import UUID

import pytest

from hobby_tracker.application import commands
from hobby_tracker.application.unit_of_work import UnitOfWork
from hobby_tracker.domain.activity import ActivityRepository
from hobby_tracker.domain.exceptions import (
    ActivityAttributeDuplicate,
    HobbyAttributeDuplicate,
    HobbyNotFound,
)
from hobby_tracker.domain.hobby import HobbyRepository


@pytest.fixture
def uow() -> UnitOfWork:
    return MagicMock(spec=UnitOfWork)


@pytest.fixture
def hobby_repo() -> HobbyRepository:
    return Mock(spec=HobbyRepository)


@pytest.fixture
def activity_repo() -> ActivityRepository:
    return Mock(spec=ActivityRepository)


@pytest.mark.parametrize("name_exists", [True, False])
@pytest.mark.parametrize("hobby_exists", [True, False])
@patch("hobby_tracker.application.commands.add_hobby.HobbyName")
@patch("hobby_tracker.application.commands.add_hobby.Hobby")
def test_add_hobby(
    mock_Hobby,
    mock_HobbyName,
    uow: UnitOfWork,
    hobby_repo: HobbyRepository,
    hobby_id: UUID,
    hobby_name_str: str,
    name_exists: bool,
    hobby_exists: bool,
):
    hobby_repo.exists.return_value = hobby_exists
    hobby_repo.name_exists.return_value = name_exists
    mock_name = Mock()
    mock_hobby = Mock()
    mock_HobbyName.return_value = mock_name
    mock_Hobby.return_value = mock_hobby

    handler = commands.AddHobbyHandler(uow=uow, hobby_repo=hobby_repo)
    cmd = commands.AddHobbyCommand(id=hobby_id, name=hobby_name_str)

    if name_exists:
        with pytest.raises(HobbyAttributeDuplicate, match=re.escape(repr(mock_name))):
            handler(cmd)
        return

    if hobby_exists:
        with pytest.raises(HobbyAttributeDuplicate, match=hobby_id):
            handler(cmd)
        return

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    mock_HobbyName.assert_called_once_with(hobby_name_str)
    mock_Hobby.assert_called_once_with(id=hobby_id, name=mock_name)
    hobby_repo.add.assert_called_once_with(mock_hobby)


@patch("hobby_tracker.application.commands.rename_hobby.HobbyName")
def test_rename_hobby(
    mock_HobbyName, uow: UnitOfWork, hobby_repo: HobbyRepository, hobby_id: UUID
):
    mock_name = Mock()
    mock_hobby = Mock()
    mock_HobbyName.return_value = mock_name
    hobby_repo.get_by_id.return_value = mock_hobby
    new_name = "Drawing"

    cmd = commands.RenameHobbyCommand(hobby_id=hobby_id, new_name=new_name)
    handler = commands.RenameHobbyHandler(uow=uow, hobby_repo=hobby_repo)

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    mock_HobbyName.assert_called_once_with(new_name)
    hobby_repo.get_by_id.assert_called_once_with(hobby_id)
    mock_hobby.rename.assert_called_once_with(mock_name)


def test_delete_hobby(uow: UnitOfWork, hobby_repo: HobbyRepository, hobby_id: UUID):
    mock_hobby = Mock()
    hobby_repo.get_by_id.return_value = mock_hobby

    cmd = commands.DeleteHobbyCommand(hobby_id=hobby_id)
    handler = commands.DeleteHobbyHandler(uow=uow, hobby_repo=hobby_repo)

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    hobby_repo.get_by_id.assert_called_once_with(hobby_id)
    hobby_repo.delete.assert_called_once_with(mock_hobby)


@pytest.mark.parametrize("activity_exists", [True, False])
@pytest.mark.parametrize("hobby_exists", [True, False])
@pytest.mark.parametrize("note_text", ["Writing unit tests", None])
@patch("hobby_tracker.application.commands.add_activity.Activity")
@patch("hobby_tracker.application.commands.add_activity.ActivityDuration")
@patch("hobby_tracker.application.commands.add_activity.ActivityNote")
@patch("hobby_tracker.application.commands.add_activity.ActivityStart")
def test_add_activity(
    mock_ActivityStart,
    mock_ActivityNote,
    mock_ActivityDuration,
    mock_Activity,
    uow: UnitOfWork,
    hobby_repo: HobbyRepository,
    activity_repo: ActivityRepository,
    activity_id: UUID,
    hobby_id: UUID,
    activity_start_datetime: datetime,
    activity_duration_minutes: int,
    note_text: str | None,
    hobby_exists: bool,
    activity_exists: bool,
):
    activity_repo.exists.return_value = activity_exists
    hobby_repo.exists.return_value = hobby_exists
    mock_start, mock_duration, mock_note, mock_activity = Mock(), Mock(), Mock(), Mock()
    (
        mock_ActivityStart.return_value,
        mock_ActivityDuration.return_value,
        mock_ActivityNote.return_value,
        mock_Activity.return_value,
    ) = (mock_start, mock_duration, mock_note, mock_activity)

    cmd = commands.AddActivityCommand(
        activity_id=activity_id,
        hobby_id=hobby_id,
        started_at=activity_start_datetime,
        duration_minutes=activity_duration_minutes,
        note=note_text,
    )
    handler = commands.AddActivityHandler(
        uow=uow, hobby_repo=hobby_repo, activity_repo=activity_repo
    )

    if not hobby_exists:
        with pytest.raises(HobbyNotFound, match=hobby_id):
            handler(cmd)
        return

    if activity_exists:
        with pytest.raises(ActivityAttributeDuplicate, match=activity_id):
            handler(cmd)
        return

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    hobby_repo.exists.assert_called_once_with(hobby_id)

    mock_ActivityStart.assert_called_once_with(activity_start_datetime)
    mock_ActivityDuration.assert_called_once_with(activity_duration_minutes)
    if note_text is not None:
        mock_ActivityNote.assert_called_once_with(note_text)
        mock_Activity.assert_called_once_with(
            id=activity_id,
            hobby_id=hobby_id,
            started_at=mock_start,
            duration=mock_duration,
            note=mock_note,
        )
    else:
        mock_Activity.assert_called_once_with(
            id=activity_id,
            hobby_id=hobby_id,
            started_at=mock_start,
            duration=mock_duration,
            note=None,
        )
    activity_repo.add.assert_called_once_with(mock_activity)


@patch("hobby_tracker.application.commands.change_activity_start.ActivityStart")
def test_change_activity_start(
    mock_ActivityStart,
    uow: UnitOfWork,
    activity_repo: ActivityRepository,
    activity_id: UUID,
):
    mock_start = Mock()
    mock_activity = Mock()
    mock_ActivityStart.return_value = mock_start
    activity_repo.get_by_id.return_value = mock_activity

    new_start = datetime(2026, 8, 13, 15, 1, tzinfo=timezone.utc)
    cmd = commands.ChangeActivityStartCommand(
        activity_id=activity_id, new_start=new_start
    )
    handler = commands.ChangeActivityStartHandler(uow=uow, activity_repo=activity_repo)

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    activity_repo.get_by_id.assert_called_once_with(activity_id)
    mock_ActivityStart.assert_called_once_with(new_start)
    mock_activity.change_start.assert_called_once_with(mock_start)


@patch("hobby_tracker.application.commands.change_activity_duration.ActivityDuration")
def test_change_activity_duration(
    mock_ActivityDuration,
    uow: UnitOfWork,
    activity_repo: ActivityRepository,
    activity_id: UUID,
):
    mock_duration = Mock()
    mock_activity = Mock()
    mock_ActivityDuration.return_value = mock_duration
    activity_repo.get_by_id.return_value = mock_activity

    new_duration = 45
    cmd = commands.ChangeActivityDurationCommand(
        activity_id=activity_id, new_duration_minutes=new_duration
    )
    handler = commands.ChangeActivityDurationHandler(
        uow=uow, activity_repo=activity_repo
    )

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    activity_repo.get_by_id.assert_called_once_with(activity_id)
    mock_ActivityDuration.assert_called_once_with(new_duration)
    mock_activity.change_duration.assert_called_once_with(mock_duration)


@patch("hobby_tracker.application.commands.set_activity_note.ActivityNote")
def test_set_activity_note(
    mock_ActivityNote,
    uow: UnitOfWork,
    activity_repo: ActivityRepository,
    activity_id: UUID,
):
    mock_note, mock_activity = Mock(), Mock()
    mock_ActivityNote.return_value = mock_note
    activity_repo.get_by_id.return_value = mock_activity

    note = "Writing and writing my favorite unit tests :)"
    cmd = commands.SetActivityNoteCommand(activity_id=activity_id, note=note)
    handler = commands.SetActivityNoteHandler(uow=uow, activity_repo=activity_repo)

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    activity_repo.get_by_id.assert_called_once_with(activity_id)
    mock_ActivityNote.assert_called_once_with(note)
    mock_activity.set_note.assert_called_once_with(mock_note)


def test_delete_activity_note(
    uow: UnitOfWork,
    activity_repo: ActivityRepository,
    activity_id: UUID,
):
    mock_activity = Mock()
    activity_repo.get_by_id.return_value = mock_activity

    cmd = commands.DeleteActivityNoteCommand(activity_id=activity_id)
    handler = commands.DeleteActivityNoteHandler(uow=uow, activity_repo=activity_repo)

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    activity_repo.get_by_id.assert_called_once_with(activity_id)
    mock_activity.delete_note.assert_called_once_with()


def test_delete_activity(
    uow: UnitOfWork,
    activity_repo: ActivityRepository,
    activity_id: UUID,
):
    mock_activity = Mock()
    activity_repo.get_by_id.return_value = mock_activity

    cmd = commands.DeleteActivityCommand(activity_id=activity_id)
    handler = commands.DeleteActivityHandler(uow=uow, activity_repo=activity_repo)

    handler(cmd)

    uow.__enter__.assert_called_once_with()
    activity_repo.get_by_id.assert_called_once_with(activity_id)
    activity_repo.delete.assert_called_once_with(mock_activity)
