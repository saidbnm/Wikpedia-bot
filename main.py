from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN



bot=Bot(token=API_TOKEN)
sb=Dispatcher(bot)


@sb.message_handler(commands=['start'])
async def start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Salom {name}")

@sb.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    
executor.start_polling(sb, skip_updates=True)