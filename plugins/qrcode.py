

"""
✘ Commands Available -

•`qrcode <text/reply to text>`
   Makes qrcode of text

•`addqr <reply image> <text>`
   Makes qr of text and add it to image.

•`qrdecode <reply to qrcode>`
   It decodes the qrcode.
"""


import os

import cv2
import qrcode
from PIL import Image
from telethon.tl.types import MessageMediaDocument as doc
from telethon.tl.types import MessageMediaPhoto as photu

from . import *


@Asteroid_cmd(pattern="qrcode ?(.*)")
async def cd(e):
    reply = await e.get_reply_message()
    msg = e.pattern_match.group(1)
    if reply and reply.text:
        msg = reply.text
    elif msg:
        msg = msg
    else:
        return await eod(e, "`Give Some Text or Reply")
    kk = await eor(e, "`processing`")
    pfp = await Asteroid_bot.get_profile_photos(Asteroid_bot.uid)
    img = "resources/extras/teamAsteroid.jpg"
    if len(pfp) >= 1:
        img = await Asteroid_bot.download_media(pfp[0])
    ok = Image.open(img)
    logo = ok.resize((60, 60))
    cod = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    cod.add_data(msg)
    cod.make()
    imgg = cod.make_image().convert("RGB")
    pstn = ((imgg.size[0] - logo.size[0]) // 2, (imgg.size[1] - logo.size[1]) // 2)
    imgg.paste(logo, pstn)
    imgg.save(img)
    await Asteroid_bot.send_file(e.chat_id, img, support_stream=True)
    await kk.delete()
    os.remove(img)


@Asteroid_cmd(pattern="addqr ?(.*)")
async def qrwater(e):
    msg = e.pattern_match.group(1)
    r = await e.get_reply_message()
    if not (msg and r and r.media):
        return await eod(e, "`Reply Any Media and Give Text`")
    kk = await eor(e, "`processing`")
    if isinstance(r.media, photu):
        dl = await Asteroid_bot.download_media(r.media)
    elif isinstance(r.media, doc):
        dl = await Asteroid_bot.download_media(r, thumb=-1)
    else:
        return
    img_bg = Image.open(dl)
    qr = qrcode.QRCode(box_size=5)
    qr.add_data(msg)
    qr.make()
    img_qr = qr.make_image()
    pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])
    img_bg.paste(img_qr, pos)
    img_bg.save(dl)
    await Asteroid_bot.send_file(e.chat_id, dl, support_stream=True)
    await kk.delete()
    os.remove(dl)


@Asteroid_cmd(pattern="qrdecode$")
async def decod(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eod(e, "`Reply to Qrcode Media`")
    kk = await eor(e, "`processing`")
    if isinstance(r.media, photu):
        dl = await Asteroid_bot.download_media(r.media)
    elif isinstance(r.media, doc):
        dl = await Asteroid_bot.download_media(r, thumb=-1)
    else:
        return
    im = cv2.imread(dl)
    try:
        det = cv2.QRCodeDetector()
        tx, y, z = det.detectAndDecode(im)
        await kk.edit("**Decoded Text:\n\n**" + tx)
    except BaseException:
        await kk.edit("`Reply To Media in Which Qr image present.`")
    os.remove(dl)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
#shivansh