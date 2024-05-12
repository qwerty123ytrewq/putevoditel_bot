import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
bot = Bot("7143832475:AAFwTQS6wBbIB27eDLZIzpdoRocG_2T7--k")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет) Я вывожу достопримечательности тех городов, которые Вы сюда забьёте. Приступим?")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
