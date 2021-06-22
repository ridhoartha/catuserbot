import asyncio
from collections import deque

from . import ALIVE_NAME, catub, edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="sadboi$",
    command=("sadboi", plugin_category),
    info={
        "header": "pamer sadboi userbot",
        "usage": "{tr}sadboi",
    },
) 
async def _(event):
    "animation command"
    animation_interval = 1.0
    animation_ttl = range(6)
    event = await edit_or_reply(event, "`bang?`")
    animation_chars = [
        "bot lu bisa gini ga?",
        f"{ALIVE_NAME} nih bos",
        "xixixi",
        "😈",
        f"{ALIVE_NAME} NIH BOS",
        "😈",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@catub.cat_cmd(
    pattern="intro$",
    command=("intro", plugin_category),
    info={
        "header": "untuk perkenalkan diri",
        "usage": "{tr} intro",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1.0
    animation_ttl = range(5)
    event = await edit_or_reply(event, "`intro`")
    animation_chars = [
    "Assalamualaikuum..",
    f"Perkenalkan nama gua {ALIVE_NAME}",
    "Biasa di panggil gembel",
    "Udh gitu aja btw lo kontol",
    "XIXIXI",
   
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])