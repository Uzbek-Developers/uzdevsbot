# Misc
import os
import logging
import textwrap
import random

# Bot
from aiotg import Bot

# Queries
from database.queries import user_exists, insert_user, deactivate_user
from database.queries import insert_text

# Variables
api_token = os.environ.get("API_TOKEN")
bot_name = os.environ.get("BOT_NAME")

# Bot
bot = Bot(api_token=api_token, name=bot_name)

# Logging
logger = logging.getLogger("bot")
logging.basicConfig(level=logging.DEBUG)


def format_text(text):
    return textwrap.dedent(text)


@bot.handle("new_chat_member")
async def new_chat_member_event(chat, member):
    logger.info("New chat member %s joined group", member["first_name"])
    text = format_text(
        """
    {greet}, {name}!

    Guruhga xush kelibsiz!

    Ushbu guruh o'zbek dasturchilari uchun ochilgan bo'lib, bu yerda guruh a'zolar bir-birlari bilan tajriba almashishlari, savol-javob qilishlari va shu sohadagi foydali narsalar (texnologiyalar, yangiliklar) ni o'zaro ulashishlari maqsad qilingan.

    {name}, {wish}. {emoticon}
    """
    )
    greetings = ("Assalomu alaykum", "Salom", "Guruhimizning yangi a'zosi")
    greet = random.choice(greetings)
    wishes = (
        "guruhda faol bo'lasiz degan umiddaman",
        "ishlaringizga omad",
        "yana bir bor hush kelibsiz",
    )
    wish = random.choices(wishes)
    emoticons = ("😎", "🤠", "😃", "😊", "🙂", "🤓")
    emoticon = random.choice(emoticons)

    if not await user_exists(chat.bot.pg_pool, member):
        await insert_user(chat.bot.pg_pool, member)

    await chat.send_text(
        text.format(
            name=member["first_name"], greet=greet, wish=wish, emoticon=emoticon
        )
    )


@bot.handle("left_chat_member")
async def left_chat_member_event(chat, member):
    logger.info("Chat member %s left group", member["first_name"])
    text = format_text(
        """
    {farewell}, {name}! Yaxshi-yomon gaplarga uzr! {wish}. {emoticon}
    """
    )
    farewells = (
        "Yaxshi boring",
        "Kutilmaganda guruhimizni tark etgan",
        "Yaxshi gaplashib o'tirgandik",
        "Xayr",
        "Alvido",
    )
    farewell = random.choice(farewells)
    wishes = ("Ishlaringizga omad", "Yaxshi boring", "Ko'rishguncha")
    wish = random.choice(wishes)
    emoticons = ("😌", "😕", "🙁", "☹️", "😫", "😩", "😢", "🤕")
    emoticon = random.choice(emoticons)

    if await user_exists(chat.bot.pg_pool, member):
        await deactivate_user(chat.bot.pg_pool, member)

    await chat.send_text(
        text.format(
            name=member["first_name"], farewell=farewell, wish=wish, emoticon=emoticon
        )
    )


@bot.default
@bot.group_message
async def group_message_event(chat, message):
    sender = message.get("from")
    message_date = message.get("date")
    text = message.get("text")
    logger.info("Got message from group at %s", message_date)
    await insert_text(chat.bot.pg_pool, sender, text)


@bot.command(r"/about")
async def about_command(chat, match):
    text = format_text(
        """
    https://github.com/Uzbek-Developers/uzdevsbot
    """
    )
    logger.info("Got about from %s", chat.sender)
    await chat.send_text(text, disable_web_page_preview=True)
