

import time

from pyAsteroid.dB import *
from PyAsteroid.dB.core import *
from PyAsteroid.functions.all import *
from PyAsteroid.functions.broadcast_db import *
from PyAsteroid.functions.gban_mute_db import *
from PyAsteroid.functions.goodbye_db import *
from PyAsteroid.functions.google_image import googleimagesdownload
from PyAsteroid.functions.sudos import *
from PyAsteroid.functions.welcome_db import *
from PyAsteroid.functions.ytdl import *
from PyAsteroid.utils import *

#from strings import get_string

try:
    import glitch_me
except ModuleNotFoundError:
    os.system(
        "git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me"
    )


start_time = time.time()
Asteroid_version = "v0.0.1"
OWNER_NAME = Asteriod_bot.me.first_name
OWNER_ID = Asteriod_bot.me.id

List = []
Dict = {}
N = 0


def grt(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]
