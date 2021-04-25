import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import json
import math
import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import filters
from pyrogram import Client
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserBannedInChannel 


@Client.on_message(filters.command(["start"]))
async def text(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await update.reply_text("You are Banned")
        return
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text(" Sorry, You are **B A N N E D**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="**Oh Dear In Order To Use Me Join My Update Channnl 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        else:
            await update.reply_text(
          chat_id=update.chat.id,
          text=Translation.START_TEXT,
          parse_mode="html",
          disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🤠Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ🤠', url='https://t.me/TN57_BotZ'),
                    InlineKeyboardButton('🤓Fᴇᴇᴅʙᴀᴄᴋ🤓', url='https://t.me/BLuVDS')
                ],
                [
                    InlineKeyboardButton('😼Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ👾', url='https://t.me/TN57_BotzSupport'),
                    InlineKeyboardButton('«Cʟᴏsᴇ🔐»', callback_data='DM')
                ]
            ]
        )


@Client.on_callback_query()
async def button(bot, update):
 
      if  'DM'  in update.data:
                await update.message.delete()
