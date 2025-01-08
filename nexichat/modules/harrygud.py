import random
from pyrogram import Client, filters

# Example of an async method you want to await
async def registered_handler(self, client, message, *args):
    # Your handler logic here
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])

    if send_sticker:
        sticker_id = get_random_sticker()
        await client.send_sticker(message.chat.id, sticker_id)  # Await send_sticker
        await message.reply_text(f"**❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖**\n\n**❍  {sender} 😴 **\n\n**❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ**")
    else:
        emoji = get_random_emoji()
        await client.send_message(message.chat.id, emoji)  # Await send_message
        await message.reply_text(f"**❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖**\n\n**❍  {sender} {emoji} **\n\n**❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ**")

# Ensure the registered handler is actually an async method
async def goodnight_command_handler(client, message, *args):
    # Call the registered handler function (ensure it's async)
    if callable(self.registered_handler):
        await self.registered_handler(client, message, *args)
    else:
        print("Error: registered_handler is not callable or async.")

# Example of the correct usage of the handler
@app.on_message(filters.command(["gn", "n", "oodnight", "ood Night", "ood night"], prefixes=["/", "g", "G"]))
async def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])

    if send_sticker:
        sticker_id = get_random_sticker()
        await app.send_sticker(message.chat.id, sticker_id)  # Await send_sticker
        await message.reply_text(f"**❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖**\n\n**❍  {sender} 😴 **\n\n**❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ**")
    else:
        emoji = get_random_emoji()
        await app.send_message(message.chat.id, emoji)  # Await send_message
        await message.reply_text(f"**❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖**\n\n**❍  {sender} {emoji} **\n\n**❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ**")

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
