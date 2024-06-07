import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from CWMUSIC import LOGGER, app, userbot
from CWMUSIC.core.call import Anony
from CWMUSIC.misc import sudo
from CWMUSIC.plugins import ALL_MODULES
from CWMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("CWMUSIC.plugins" + all_module)
    LOGGER("CWMUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://telegra.ph/file/ae4fd5304701e15a25620.jpg")
    except NoActiveGroupCall:
        LOGGER("CWMUSIC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("CWMUSIC").info(
        "DROP YOUR GIRLFRIEND'S NUMBER AND SEXY PIC TO @ll_SABKA_BHAI_KILLER_ll , @ll_OWN_WORLD_ll FOR ANY ISSUES"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("CWMUSIC").info("Stopping CWMUSIC Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
