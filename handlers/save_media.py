# (c) @Rudraa2213

import asyncio
from configs import Config
from pyshorteners import Shortener
from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.value > 45:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await forward_to_channel(bot, message, editable)


async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list):
    try:
        message_ids_str = ""
        for message in (await bot.get_messages(chat_id=editable.chat.id, message_ids=message_ids)):
            sent_message = await forward_to_channel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.id)} "
            await asyncio.sleep(2)
        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Delete Batch", callback_data="closeMessage")
            ]])
        )
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=Rudraa332_{str_to_b64(str(SaveMessage.id))}"
        s = Shortener()
        url = s.dagd.short(share_link)
        await editable.edit(
            # f"**Batch Files Stored in my Database!**\n\nHere is the Permanent Link of your files: \n\n`{share_link}` \n\n"
            f"**Your Batch Files Stored in my Database!**\n\n**__Modern Link__** (__Recomended Link__) :\n\n`{url}`\n\n**__Normal Link__**:\n\n`{share_link}` \n\n"
            f"Just Click the link to get your files!",
            reply_markup=InlineKeyboardMarkup(
               [    [
                        InlineKeyboardButton("😎Modern Link", url=url),InlineKeyboardButton("😒Normal Link",url=share_link)
                    ],
                    # [
                    #     InlineKeyboardButton("🤖Bots Channel", url="https://telegram.me/bot_channelv1"),
                    #     InlineKeyboardButton("👪Support Group", url="https://telegram.me/Joint0T")
                    # ]
               ]
            ),
            disable_web_page_preview=True
        )
        await bot.send_message(
            chat_id=int(Config.DB_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) __Got Batch Link!__",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open Link", url=share_link)]])
        )
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )


async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.forward(Config.DB_CHANNEL)
        file_er_id = str(forwarded_msg.id)
        # await forwarded_msg.reply_text(
        #     f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Got File Link!__",
        #     disable_web_page_preview=True)
        share_link = f"https://telegram.me/{Config.BOT_USERNAME}?start=Rudraa332_{str_to_b64(file_er_id)}"
        s = Shortener()
        url = s.dagd.short(share_link)
        await editable.edit(
            # f"Here is the Permanent Link of your file: \n\n`{share_link}` \n\n"
            f"**Your Files Stored in my Database!**\n\n**__Modern Link__** (__Recomended Link__) :\n\n`{url}`\n\n**__Normal Link__**:\n\n`{share_link}` \n\n"
            f"Just Click the link to get your file!",
            reply_markup=InlineKeyboardMarkup(
               [    [
                        InlineKeyboardButton("😎Modern Link", url=url),InlineKeyboardButton("😒Normal Link",url=share_link)
                    ],
                    # [
                    #     InlineKeyboardButton("🤖Bots Channel", url="https://telegram.me/bot_channelv1"),
                    #     InlineKeyboardButton("👪Support Group", url="https://telegram.me/Joint0T")
                    # ]
               ]
            ),
            disable_web_page_preview=True
        )
        await bot.send_message(
            chat_id=int(Config.DB_CHANNEL),
            text=f"#Single_file:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) __Got Batch Link!__",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open Link", url=share_link)]])
        )
    except FloodWait as sl:
        if sl.value > 45:
            print(f"Sleep of {sl.value}s caused by FloodWait ...")
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text="#FloodWait:\n"
                     f"Got FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await save_media_in_channel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text="#ERROR_TRACEBACK:\n"
                 f"Got Error from `{str(editable.chat.id)}` !!\n\n"
                 f"**Traceback:** `{err}`",
            disable_web_page_preview=True,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
