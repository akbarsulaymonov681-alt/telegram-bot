import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
client = OpenAI(api_key=OPENAI_API_KEY)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Salom! Men AI Math Botman. Masalangizni yozing.")

@dp.message()
async def handle(message: types.Message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sen matematik masalalarni yechadigan assistentsan. Step-by-step tushuntir."},
            {"role": "user", "content": message.text}
        ]
    )

    await message.answer(response.choices[0].message.content)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


