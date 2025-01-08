import re
import random
from pyrogram import filters
from nexichat import nexichat  # Assuming this is where the bot is defined


@nexichat.on_message(filters.command(["gm", "m", "goodmorning", "Good Morning", "Good morning"], prefixes=["/", "g", "G"]))
async def goodmorning_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    
    try:
        if send_sticker:
            sticker_id = await get_random_sticker()
            await nexichat.send_sticker(message.chat.id, sticker_id)
            await message.reply_text(
                f"**❖ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ❖ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ʙʟɪssғᴜʟ ᴅᴀʏ ❖\n\n❍  {sender} 🌞 \n\n❖ ɢᴏ ᴏᴜᴛ ᴀɴᴅ ᴇxᴘʟᴏʀᴇ!**"
            )
        else:
            emoji = await get_random_emoji()
            await nexichat.send_message(message.chat.id, emoji)
            await message.reply_text(
                f"**❖ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ❖ ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀ ʙʟɪssғᴜʟ ᴅᴀʏ ❖\n\n❍  {sender} {emoji} \n\n❖ ɢᴏ ᴏᴜᴛ ᴀɴᴅ ᴇxᴘʟᴏʀᴇ!**"
            )
    except Exception as e:
        await message.reply_text("Oops! Something went wrong. Please try again later.")
        print(f"Error in goodmorning_command_handler: {e}")

# Define async functions for stickers and emoji
async def get_random_sticker():
    stickers = [
        "CAACAgQAAx0Ce9_hCAACaEVlwn7HeZhgwyVfKHc3WUGC_447IAACLgwAAkQwKVPtub8VAR018x4E",  # sticker1
        "CAACAgIAAx0Ce9_hCAACaEplwn7dvj7G0-a1v3wlbN281RMX2QACUgwAAligOUoi7DhLVTsNsh4E",  # sticker2
        "CAACAgIAAx0Ce9_hCAACaFBlwn8AAZNB9mOUvz5oAyM7CT-5pjAAAtEKAALa7NhLvbTGyDLbe1IeBA",  # sticker3
        "CAACAgUAAx0CcmOuMwACldVlwn9ZHHF2-S-CuMSYabwwtVGC3AACOAkAAoqR2VYDjyK6OOr_Px4E",  # sticker4
        "CAACAgIAAx0Ce9_hCAACaFVlwn-fG58GKoEmmZpVovxEj4PodAACfwwAAqozQUrt2xSTf5Ac4h4E",  # sticker5
    ]
    return random.choice(stickers)

async def get_random_emoji():
    emojis = [
        "🌞",
        "🌅",
        "☀️",
        "🌤️",
    ]
    return random.choice(emojis)
