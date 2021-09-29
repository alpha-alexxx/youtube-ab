from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


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
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Thank You", url="https://www.youtube.com/channel/UCHwnjZgBoKFSaxUhrLx1lWQ")]]
        ),
@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("url")
    & Filters.user(Config.AUTH_USERS)
)
async def _url(c: UtubeBot, m: Message):
    await m.reply_chat_action("typing")

    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
        auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
        url = auth.GetAuthUrl()

        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Direct Auth url", url=url)]]
        ),
    )
    )
