import uasyncio as asyncio
from machine import Pin
from mqtt_as import MQTTClient
from pusbutton import Pushbutton
from utime import time

import sound
from config import config

button = Pushbutton(Pin(2, Pin.IN))

SERVER = "voyage.lan"

last_timestamp = None



async def sound(reason):
    if reason

def callback(topic, msg, retained):
    """Callback for messages."""
    if "sound" in msg.decode():
        ring("alarm")

def ring(reason):
    if "timeout" in reason:
        print("sounding")
        asyncio.get_event_loop().create_task(sound.ring())
    else:
        asyncio.get_event_loop().create_task(sound.siren())

def stop_alarm():
    sound.sound = False
        


async def conn_han(client):
    await client.subscribe("motorcyle_alarm", 1)

async def main(client):
    await client.connect()
    while True:
        # timeout
        if last_timestamp and (time() - last_timestamp > 120):
            await sound("timeout")
        await asyncio.sleep(10)

