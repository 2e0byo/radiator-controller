import logging
import time
from sys import print_exception

import network
import ntptime
import uasyncio as asyncio
import uurequests as requests
from machine import RTC

rtc = RTC()
rtc.datetime()
wlan = network.WLAN(network.STA_IF)
clock_syncing = False

logger = logging.getLogger(__name__)
boot_time = None

offset_mins = 0


def set_offset():
    global offset_mins
    resp = requests.get("https://ifconfig.me")
    if resp.status_code != 200:
        raise Exception("Failed to get ip.")
    ip = resp.text
    resp.close()
    resp = requests.get(f"https://www.timeapi.io/api/Time/current/ip?ipAddress={ip}")
    if resp.status_code != 200:
        raise Exception("Failed to get time.")
    data = resp.json()
    resp.close()
    utc = ntptime.time()
    tm = time.gmtime()
    local = time.mktime(
        (
            data["year"],
            data["month"],
            data["day"],
            data["hour"],
            data["minute"],
            data["seconds"],
            tm[6],
            tm[7],
        )
    )
    # granularity for timezones is 15 mins.
    offset_mins = round((local - utc) / 900) * 15


def settime():
    t = ntptime.time() + offset_mins * 60
    tm = time.gmtime(t)
    rtc.datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))


def runtime():
    if not boot_time:
        return None
    else:
        return time.time() - boot_time


def clockstr(time=None):
    if not time:
        time = rtc.datetime()
    timestamp = "{}-{}-{}".format(*time[:3])
    timestamp += " {}:{}:{}".format(*time[4:7])
    return timestamp


def timestr(t):
    if not t:
        return None
    d, rem = divmod(t, 86400)
    h, rem = divmod(rem, 3600)
    m, s = divmod(rem, 60)
    return "{} days {:02}:{:02}:{:02}".format(d, h, m, s)


async def sync_clock():
    global boot_time
    while True:
        while clock_syncing:
            await asyncio.sleep(60)
            try:
                settime()
                if not boot_time:
                    boot_time = time.time()
            except (OverflowError, OSError) as e:
                print_exception(e)
                logger.error(str(e))
            await asyncio.sleep(300)
        while not clock_syncing:
            await asyncio.sleep(1)


async def sync_timezone():
    while True:
        while clock_syncing:
            try:
                set_offset()
            except Exception as e:
                print_exception(e)
                logger.error(str(e))
            await asyncio.sleep(60 * 60 * 12)
        while not clock_syncing:
            await asyncio.sleep(1)


def clock_synced():
    time = rtc.datetime()
    return time[0] != 2000


def try_sync_clock():
    ATTEMPTS = 10
    logger.debug("Trying to synchronise clock; this may take a while...")
    for _ in range(ATTEMPTS):
        try:
            settime()
        except (OverflowError, OSError) as e:
            logger.debug(f"Failed to sync, time: {rtc.datetime()}")
            print_exception(e)
            time.sleep(1)

        if clock_synced():
            return True

    return False


asyncio.create_task(sync_clock())
# asyncio.create_task(sync_timezone())


class UptimeAPI:
    def get(self, data):
        return {"value": timestr(runtime())}


class TimeAPI:
    def get(self, data):
        return {"value": clockstr()}


api = {
    "uptime": UptimeAPI(),
    "localtime": TimeAPI(),
}
