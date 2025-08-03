from aiogram import Bot, Dispatcher, executor, types
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

MENU = {
    "Шаурма с курицей стандарт": 300,
    "Шаурма с курицей Мега": 330,
    "Шаурма с говядиной стандарт": 330,
    "Шаурма с говядиной Мега": 360,
    "Бургер сырный выстрел": 390,
    "Бургер с яйцом и беконом": 390,
    "Бургер Гамбургер": 390,
    "Бургер грибной растяпа": 390,
    "Бургер Чикенбургер": 390,
    "Сэндвич с яйцом беконом": 250,
    "Сэндвич с курицей": 250,
    "Сэндвич с ветчиной и грибами": 250,
    "Сэндвич с ветчиной и сыром": 250,
    "Шея Свиная": 450,
    "Бедро Куриное": 320,
    "Шампиньоны на углях с соусом": 220,
    "Нарезка овощей": 100,
    "Картошка фри маленькая": 100,
    "Картошка фри большая": 130,
    "Капучино": 110,
    "Латте": 130,
    "Американо": 90,
    "Чай черный/зеленый": 35,
}

ADDONS = {
    "Сыр": 40,
    "Яйцо": 40,
    "Бекон": 40,
    "Болгарский перец": 40,
    "Халапеньо": 40,
    "Грибы": 40,
    "Доп котлета": 140,
    "Доп мясо курица": 70,
    "Доп мясо говядина": 90,
}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для предзаказа шаурмы 🍔🌯\nНапиши /menu чтобы посмотреть меню.")

@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    text = "📋 *Меню:*\n\n"
    for item, price in MENU.items():
        text += f"{item} — {price}₽\n"
    text += "\n🥫 *Добавки:*\n"
    for item, price in ADDONS.items():
        text += f"{item} — {price}₽\n"
    text += "\n💵 *Оплата на месте.*\n📍 *Адрес:* г. Красноярск, пр-кт Свободный 81г/1"
    await message.reply(text, parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)