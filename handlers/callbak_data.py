import asyncio
import json
from aiogram import types
from misc import dp, bot
from .sqlit import change_status,cheak_black
import random


from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content = -1001649501264

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


@dp.callback_query_handler(text = 'reg_prokladka', state = "*")
async def reg_prokladka(call, state: FSMContext):
    if int(cheak_black(call.message.chat.id)) == 0:
        await reg_p.step2.set() #ОЖИДАЕМ НАЗВАНИЕ КАНАЛА ЧЕРЕЗ @
        await call.message.answer("""<b>Отправь ссылку на свой канал через @ (собачку), как показано на видео!</b>

Не знаешь как это сделать? Посмотри видео еще раз😉""")

        await bot.answer_callback_query(call.id)  # Отвечаем на callback


@dp.message_handler(state=reg_p.step2, content_types='text')
async def name_channel(message: types.Message, state: FSMContext):
    if int(cheak_black(message.chat.id)) == 0:
        if message.text[0] == '@':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Продолжить обучение ✅',callback_data='bat_video9')
            markup.add(bat_a)
            await message.answer(text=f"""<b>Твоя «индивидуальная ссылка»:</b>
https://t.me/MovTokBot?start={message.text[1:]}""", disable_web_page_preview=True, reply_markup=markup)


        else:
            await message.answer(text="""<b>Отправь ссылку на канал через @, как это показано на видео☝️☝️☝️</b>
Пример : @BearPublic""")




@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    if int(cheak_black(call.message.chat.id)) == 0:
        if call.data == 'bat_video2': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_b = types.InlineKeyboardButton(text='Вперёд', callback_data='bat_video3')
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=122)
            await asyncio.sleep(0.2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=123)
            await asyncio.sleep(0.2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=124)
            await asyncio.sleep(0.2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=125)
            await asyncio.sleep(0.2)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=126,reply_markup=markup)

        if call.data == 'bat_video3': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_b = types.InlineKeyboardButton(text='Далее', callback_data='bat_video4')
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=128)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=129,reply_markup=markup)

        if call.data == 'bat_video4': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/MQnJHoS2dmI')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video5')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=131,reply_markup=markup)


        if call.data == 'bat_video5': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/D4B0TZYRWS4')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video6')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=134,reply_markup=markup)


        if call.data == 'bat_video6': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/eEFGje9pi6s')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video7')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=137,reply_markup=markup)

        if call.data == 'bat_video7': #отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/5kYhmZ9uTHo')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video8')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=140,reply_markup=markup)

        if call.data == 'bat_video8':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/8E6QZx7QyjI')
            bat_b = types.InlineKeyboardButton(text='Создать ИС', callback_data='reg_prokladka')
            bat_с = types.InlineKeyboardButton(text='У меня есть ИС', callback_data='bat_video9')
            markup.add(bat_a)
            markup.add(bat_b)
            markup.add(bat_с)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=143,reply_markup=markup)



        if call.data == 'bat_video9':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/xasm6zWZpTk')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video10')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=147,reply_markup=markup)


        if call.data == 'bat_video10':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/i8QjJpLJKbs')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video11')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=150,reply_markup=markup)

        if call.data == 'bat_video11':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/y47KNUNPqRM')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video12')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=153,reply_markup=markup)

        if call.data == 'bat_video12':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/augZObi08Yg')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video13')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=156,reply_markup=markup)

        if call.data == 'bat_video13':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/KTnWXmJArJg')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video14')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=159,reply_markup=markup)

        if call.data == 'bat_video14':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/uFgGFSrIJLc')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video15')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=162,reply_markup=markup)


        if call.data == 'bat_video15':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/2A3e7egJNbc')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video16')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=165,reply_markup=markup)

        if call.data == 'bat_video16':  # отправляем второе видео
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Смотреть урок', url='https://youtu.be/8imal6Oxc4I')
            bat_b = types.InlineKeyboardButton(text='Я выполнил(а)', callback_data='bat_video17')
            markup.add(bat_a)
            markup.add(bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=168,reply_markup=markup)

        if call.data == 'bat_video17':  # отправляем второе видео
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=171)
            change_status(call.message.chat.id)