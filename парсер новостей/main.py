import json
import random

from aiogram import Bot, Dispatcher, types, executor


async def on_start(_):
    print('Бот запустился')


async def on_shutdown(_):
    print('Бот остановился')


#
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

news_descriptions = list(data.keys())

API_TOKEN = '6287021376:AAElQ4_lTq5o7Had1Gdbg0hjlMeN-g4tV-A'

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def say_hello(msg: types.Message):
    await msg.answer('Hi! Type /send_news to get the news.')


@dp.message_handler(commands=['send_news'])
async def sending_news(msg: types.Message):
    chosen_news = random.choice(news_descriptions)
    value_of_key = data[chosen_news]
    if isinstance(value_of_key, str):
        msg_random_news = f'{chosen_news}\n{value_of_key}'
        await msg.reply(msg_random_news)
    elif isinstance(value_of_key, dict):
        href = value_of_key['Ссылка']
        time = value_of_key['Время']
        hashtag = value_of_key['Хэштэг'] if 'Хэштэг' in value_of_key.keys() else ''
        send_news = f'{chosen_news}\n{href} - {time}\n{hashtag}'
        await msg.reply(send_news)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start, on_shutdown=on_shutdown)
