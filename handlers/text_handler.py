import random

from aiogram import types
from misc import dp,bot
import asyncio
from .sqlit import update_status_access
from .admin import new_password,passwd
ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID = [ADMIN_ID_1,ADMIN_ID_2]

flag1 = 1 #НАСТРОЙКА РЕЖИМА ПОКАЗА FILE ID

@dp.message_handler(content_types=['text', 'photo', 'video_note', 'animation', 'document', 'video','file'])
async def all_message(message: types.Message):
    from .admin import passwd
    if str(passwd) == message.text:
        await message.answer('Доступ открыт! Жми /start')
        update_status_access(message.chat.id)

        new_password()
    else:
        await message.answer('Неверный пароль')