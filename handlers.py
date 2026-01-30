from aiogram.types import Message, ContentType 
from aiogram import Bot, F, Router, types
from aiogram.filters import CommandStart, Command 
from aiogram.enums import ParseMode


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет друг, я бот для пробива Искажение👋.')
    await message.reply('Напиши /search для начала поиска.')
@router.message(Command('search'))
async def handle_message(message: types.Message):
    await message.answer("Отлично вы вошли в режим поиска, пришлите мне номер телефона в таком формате:"  "<code>79991234567</code>", parse_mode=ParseMode.HTML)

@router.message(F.text.regexp(r'^\d{10,12}$'))
async def handle_phone(message: types.Message):
    # Сначала подтверждаем действие
    await message.answer("Поиск начался...")
@router.message()
async def wrong_format(message: types.Message):
    await message.answer("Ошибка! Введите номер телефона (только цифры, без букв и символов).")

#cоздайте папку app в рабочей области и добавть этот файл туда ОБЯЗАТЕЛЬНО!!!!
#cоздайте папку app в рабочей области и добавть этот файл туда ОБЯЗАТЕЛЬНО!!!!
#cоздайте папку app в рабочей области и добавть этот файл туда ОБЯЗАТЕЛЬНО!!!!
