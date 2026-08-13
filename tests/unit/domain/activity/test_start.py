from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pytest

from hobby_tracker.domain.activity import ActivityStart


def test_cannot_accept_non_utc(activity_start_datetime: datetime):
    dt = activity_start_datetime.astimezone(ZoneInfo("Asia/Tokyo"))
    with pytest.raises(ValueError, match="ActivityStart must UTC datetime"):
        ActivityStart(dt)


def test_cannot_accept_future():
    dt = datetime.now(timezone.utc) + timedelta(10)
    with pytest.raises(ValueError, match="Activity cannot start in the future"):
        ActivityStart(dt)
