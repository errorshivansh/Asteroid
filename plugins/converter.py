

"""
✘ Commands Available -


• `{i}mtoi <reply to media>`
    Media to image conversion

• `{i}mtos <reply to media>`
    Convert media to sticker.

• `{i}doc <filename.ext>`
    Reply to a text msg to save it in a file.

• `{i}open`
    Reply to a file to reveal it's text.

• `{i}rename <file name with extension>`
    Rename the file

• `{i}thumbnail <reply to image/thumbnail file>`
    Upload Your file with your custom thumbnail.
"""

import os
import time

import cv2
import requests
from PIL import Image
from telegraph import upload_file as uf
from telethon.tl.types import MessageMediaDocument as doc
from telethon.tl.types import MessageMediaPhoto as photu

from . import *

opn = []


@Asteroid_cmd(pattern="thumbnail$")
async def _(e):
    r = await e.get_reply_message()
    pop = "`Reply to img or file with thumbnail.`"
    if not r:
        return await eor(e, pop)
    if isinstance(r.media, photu):
        dl = await Asteroid_bot.download_media(r.media)
    elif isinstance(r.media, doc):
        if r.media.document.thumbs:
            dl = await Asteroid_bot.download_media(r, thumb=-1)
        else:
            return await eor(e, pop)
    variable = uf(dl)
    os.remove(dl)
    nn = "https://telegra.ph" + variable[0]
    udB.set("CUSTOM_THUMBNAIL", str(nn))
    await bash(f"wget {nn} -O resources/extras/cee415d7720336ea1121debd2cddcbd1.png")
    await eor(e, f"Added [This]({nn}) As Your Custom Thumbnail", link_preview=False)


@Asteroid_cmd(pattern="rename ?(.*)")
async def imak(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        await eor(event, "Reply to any media/Document.")
        return
    inp = event.pattern_match.group(1)
    if not inp:
        await eor(event, "Give The name nd extension of file")
        return
    xx = await eor(event, "`Processing...`")
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            image = await downloader(
                reply.file.name, reply.media.document, xx, t, "Downloading..."
            )
            file = image.name
        else:
            file = await event.download_media(reply)
    os.rename(file, inp)
    k = time.time()
    xxx = await uploader(inp, inp, k, xx, "Uploading...")
    await ultroid_bot.send_file(
        event.chat_id,
        xxx,
        force_document=True,
        thumb="resources/extras/ultroid.jpg",
        caption=f"`{xxx.name}`",
        reply_to=reply,
    )
    os.remove(inp)
    await xx.delete()


@Asteroid_cmd(pattern="mtoi$")
async def imak(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await eor(event, "Reply to any media.")
        return
    xx = await eor(event, "`Processing...`")
    image = await Asteroid_bot.download_media(reply)
    file = "ult.png"
    if image.endswith((".webp", ".png")):
        c = Image.open(image)
        c.save(file)
    else:
        img = cv2.VideoCapture(image)
        ult, roid = img.read()
        cv2.imwrite(file, roid)
    await Asteroid_bot.send_file(event.chat_id, file, reply_to=reply)
    await xx.delete()
    os.remove(file)
    os.remove(image)


@Asteroid_cmd(pattern="mtos$")
async def smak(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await eor(event, "Reply to any media.")
        return
    xx = await eor(event, "`Processing...`")
    image = await Asteroid_bot.download_media(reply)
    file = "ult.webp"
    if image.endswith((".webp", ".png", ".jpg")):
        c = Image.open(image)
        c.save(file)
    else:
        img = cv2.VideoCapture(image)
        ult, roid = img.read()
        cv2.imwrite(file, roid)
    await Asteroid_bot.send_file(event.chat_id, file, reply_to=reply)
    await xx.delete()
    os.remove(file)
    os.remove(image)


@Asteroid_cmd(
    pattern="doc",
)
async def _(event):
    input_str = event.text[5:]
    xx = await eor(event, get_string("com_1"))
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        if not a.message:
            return await xx.edit("`Reply to a message`")
        else:
            b = open(input_str, "w")
            b.write(str(a.message))
            b.close()
            await xx.edit(f"**Packing into** `{input_str}`")
            await event.client.send_file(
                event.chat_id, input_str, thumb="resources/extras/ultroid.jpg"
            )
            await xx.delete()
            os.remove(input_str)


@Asteroid_cmd(
    pattern="open$",
)
async def _(event):
    xx = await eor(event, get_string("com_1"))
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        if a.media:
            b = await a.download_media()
            c = open(b)
            d = c.read()
            c.close()
            try:
                await xx.edit(f"```{d}```")
            except BaseException:
                key = (
                    requests.post(
                        "https://nekobin.com/api/documents", json={"content": d}
                    )
                    .json()
                    .get("result")
                    .get("key")
                )
                await xx.edit(
                    f"**MESSAGE EXCEEDS TELEGRAM LIMITS**\n\nSo Pasted It On [NEKOBIN](https://nekobin.com/{key})"
                )
            os.remove(b)
        else:
            return await eod(xx, "`Reply to a readable file`", time=5)
    else:
        return await eod(xx, "`Reply to a readable file`", time=5)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
