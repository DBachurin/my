import config
from aiogram import executor
from aiogram import Bot, Dispatcher

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(content_types=['text'])
async def create_word(message):
    await message.answer(message.text)
    #bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


