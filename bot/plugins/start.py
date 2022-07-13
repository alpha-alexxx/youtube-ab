from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot
from ..youtube import GoogleAuth


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
    & Filters.user(Config.AUTH_USERS)
)
async def _start(c: UtubeBot, m: Message):
    await m.reply_chat_action("typing")

    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
          auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
          url = auth.GetAuthUrl()
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Login URL", url=url)]]
        ),
    )
