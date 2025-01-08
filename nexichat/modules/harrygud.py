import re
from pyrogram import filters
import random
from nexichat import nexichat

@nexichat.on_message(filters.command(["gn", "n", "oodnight", "ood Night", "ood night"], prefixes=["/", "g", "G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    
    if send_sticker:
        sticker_id = get_random_sticker()
        nexichat.send_sticker(message.chat.id, sticker_id)  # Assuming nexichat object is used here
        message.reply_text(f"**❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖**\n\n**❍  {sender} 😴 **\n\n**❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ**")
    else:
        emoji = get_random_emoji()
        nexichat.send_message(message.chat.id, emoji)  # Assuming nexichat object is used here
        message.reply_text(f"**❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖**\n\n**❍  {sender} {emoji} **\n\n**❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ**")

def get_random_sticker():
    stickers = [
        "CAACAgQAAx0Ce9_hCAACaEVlwn7HeZhgwyVfKHc3WUGC_447IAACLgwAAkQwKVPtub8VAR018x4E", 
        "CAACAgIAAx0Ce9_hCAACaEplwn7dvj7G0-a1v3wlbN281RMX2QACUgwAAligOUoi7DhLVTsNsh4E", 
        "CAACAgIAAx0Ce9_hCAACaFBlwn8AAZNB9mOUvz5oAyM7CT-5pjAAAtEKAALa7NhLvbTGyDLbe1IeBA", 
        "CAACAgUAAx0CcmOuMwACldVlwn9ZHHF2-S-CuMSYabwwtVGC3AACOAkAAoqR2VYDjyK6OOr_Px4E",
        "CAACAgIAAx0Ce9_hCAACaFVlwn-fG58GKoEmmZpVovxEj4PodAACfwwAAqozQUrt2xSTf5Ac4h4E",
    ]
    return random.choice(stickers)

def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
    ]
    return random.choice(emojis)
