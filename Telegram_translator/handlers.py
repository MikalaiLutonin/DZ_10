
from translate import Translator
from aiogram.types import Message
from config import dp
import text


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{text.greeting}'
                         f'{message.from_user.first_name} \n\n'
                         f' {text.rules}\n'
                         f' {text.agree}')


@dp.message_handler(commands=['translate'])
async def translate(message: Message):
    await message.answer('Введите слово или выражение, которое необходимо перевести:\n')


@dp.message_handler()
async def trans(message: Message):
    translator = Translator(to_lang="Russian")
    trans = message.text
    translation = translator.translate(trans)
    await message.answer(f'{translation}')
