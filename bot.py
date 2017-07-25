# Misc
import os
import logging
import json
import textwrap

# Bot
from aiotg import Bot

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
async def new_chat_member(chat, match):
    logger.info('chat  ----> %s', chat)
    logger.info('match ----> %s', match)
    await chat.send_text('somebody came')
