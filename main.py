# Asyncio
import asyncio

# UVLoop
import uvloop

# Asyncpg
from asyncpg import create_pool as create_pg_pool

# Aiobotocore
from aiobotocore import get_session as boto_session

# Bot
from bot import bot

# Misc
import os

# Use uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def run_bot():
    await bot.loop()

# Main event loop
loop = asyncio.get_event_loop()

# Attach admin group to bot
setattr(bot, 'group', bot.private(os.environ.get('BOT_GROUP')))


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == 'loop':
        loop.run_until_complete(run_bot())
    else:
        bot.run_webhook(os.environ.get('APP_URL') + 'webhook')
