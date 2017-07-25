# Misc
import os
import logging
import json
import textwrap
import random

# Bot
from aiotg import Bot

# Queries
from queries import user_exists, insert_user, deactivate_user

# Variables
api_token = os.environ.get('API_TOKEN')
bot_name = os.environ.get('BOT_NAME')

# Bot
bot = Bot(api_token=api_token, name=bot_name)

# Logging
logger = logging.getLogger('bot')
logging.basicConfig(level=logging.DEBUG)


def format_text(text):
    return textwrap.dedent(text)


@bot.command(r'salom')
@bot.command(r'салом')
async def greeting(chat, match):
    greeting = format_text('''
    Салом, {name}. 🖐 
    ''')
    logger.info('Got greeting from %s', chat.sender)
    await chat.send_text(
        greeting.format(name=chat.sender['first_name']))


@bot.command(r'/start')
async def greeting(chat, match):
    greeting = format_text('''
    Салом, {name}. 🖐 
    ''')
    logger.info('Got start from %s', chat.sender)
    await chat.send_text(
        greeting.format(name=chat.sender['first_name']))


@bot.command(r'/test')
async def greeting(chat, match):
    greeting = format_text('''
    {name} 🙄 
    ''')
    logger.info('Got start from %s', chat.sender)
    await chat.send_text(
        greeting.format(name=chat.sender['first_name']))


@bot.command(r'/stop')
async def greeting(chat, match):
    greeting = format_text('''
    Хайр, {name}. 🖐 
    ''')
    logger.info('Got goodbye from %s', chat.sender)
    await chat.send_text(
        greeting.format(name=chat.sender['first_name']))


@bot.default
async def unknown(chat, match):
    greeting = format_text('''
    {name}, қизиқиш билдирганингиз учун раҳмат. Бот ҳали битгани йўқ.
    ''')
    logger.info('Got unknown command from %s', chat.sender)
    await chat.send_text(
        greeting.format(name=chat.sender['first_name']))


@bot.command(r'/gif')
async def gif(chat, match):
    await chat.send_document(document=open("media/funny.gif", "rb"))


@bot.handle('new_chat_member')
async def new_chat_member(chat, member):
    logger.info('New chat member %s joined group', member['first_name'])
    text = format_text('''
    {greet}, {name}!

    Гуруҳимизга хуш келибсиз!

    Ушбу гуруҳ ўзбек дастурчилари учун очилган бўлиб, бу ерда аъзолар бир-бирлари билан тажриба алмашишлари, савол-жавоб қилишлари ва шу турдаги фойдали нарсаларни (технологиялар, янгиликлар) ўзаро улашишлари кўзда тутилган.

    {name}, гуруҳимизда фаол бўласиз деган умиддаман. {emoticon}
    ''')
    greetings = (
        'Ассалому алайкум', 'Салом',
        'Ҳайрли кун', 'Вау! Кутиб олинг, гуруҳимизнинг янги аъзоси',
        'Хэллоу', 'Чао', 'Сава'
    )
    greet = random.choice(greetings)
    emoticons = (
        '😎', '🤠'
    )
    emoticon = random.choice(emoticons)

    if not await user_exists(chat.bot.pg_pool, member):
        await insert_user(chat.bot.pg_pool, member)

    await chat.send_text(
        text.format(name=member['first_name'], greet=greet, emoticon=emoticon))


@bot.handle('left_chat_member')
async def left_chat_member(chat, member):
    logger.info('Chat member %s left group', member['first_name'])
    text = format_text('''
    {farewell}, {name}! Яхши-ёмон гапларга узр! Ишларга омад. {emoticon}
    ''')
    farewells = (
        'Эх аттанг, гуруҳни тарк этганиз яхши бўлмадида', 'Яхши боринг',
        'Кутилмаганда гуруҳимиздан чиқиб кетган', 'Яхши гаплашиб ўтиргандик',
        'Хайр', 'Кўришгунча', 'Алвидо'
    )
    farewell = random.choice(farewells)
    emoticons = (
        '😌', '😕', '🙁',' ☹️', '😫', '😩', '😢', '🤕'
    )
    emoticon = random.choice(emoticons)

    if await user_exists(chat.bot.pg_pool, member):
        await deactivate_user(chat.bot.pg_pool, member)

    await chat.send_text(
        text.format(name=member['first_name'], farewell=farewell, emoticon=emoticon))
