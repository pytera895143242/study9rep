from aiogram import types
from misc import dp, bot
from .sqlit import reg_user, info_members, cheak_black,status_access,update_status_access
from .callbak_data import reg_p
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001649501264
reg_user(1)  # Запуск в БД


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    reg_user(message.chat.id)  # Регистрация в БД
    s = status_access(message.chat.id)
    if s == "1":
        await message.answer("Введите пароль!")

    else:
        if int(cheak_black(message.chat.id)) == 0:
            markup = types.InlineKeyboardMarkup()
            bat_b = types.InlineKeyboardButton(text='Далее', callback_data='bat_video2')
            markup.add(bat_b)

            await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id = 120, reply_markup=markup)
