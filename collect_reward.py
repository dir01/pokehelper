# -*- coding: utf-8 -*-
import time
from datetime import datetime
from random import randint

from POGOProtos.Networking.Requests import (
    Request_pb2 as Request,
    RequestType_pb2 as RequestType
)


def collect_reward(session):
    profile = session.getProfile()
    next_collect = profile.player_data.daily_bonus.next_defender_bonus_collect_timestamp_ms
    next_collect = datetime.fromtimestamp(next_collect / 1000)
    now = datetime.now()
    if next_collect > now:
        sleep_seconds = int((next_collect - now).total_seconds())
        sleep_seconds += randint(60, 60 * 17)
        print 'Reward collect time is {}, sleeping for {} seconds'.format(next_collect, sleep_seconds)
        time.sleep(sleep_seconds)
    payload = [Request.Request(
        request_type=RequestType.COLLECT_DAILY_DEFENDER_BONUS,
    )]
    session.wrapAndRequest(payload, defaults=False)
