import os
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Update
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Настройка логгера
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Обработка команды /начнем
@dp.message(commands=["начнем"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я готов принять твой заказ на шаурму 🌯")

# Webhook обработчик
async def telegram_webhook(request: web.Request):
    try:
        data = await request.json()
        update = Update.model_validate(data)
        await dp.feed_update(bot, update)
    except Exception as e:
        logging.error(f"Ошибка при обработке запроса: {e}")
    return web.Response(text="OK")

# Создаём приложение AIOHTTP
app = web.Application()
app.router.add_post("/webhook", telegram_webhook)

# Устанавливаем webhook при запуске
async def on_startup(app):
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(WEBHOOK_URL)
        logging.info(f"Webhook установлен: {WEBHOOK_URL}")

app.on_startup.append(on_startup)

# Запуск сервера
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
