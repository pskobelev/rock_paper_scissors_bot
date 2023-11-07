from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# CREATE KEYBOARD FROM ReplyKeyboardBuilder

# create buttons
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# initialize builder
yes_no_kb_builder = ReplyKeyboardBuilder()

# add button to builder width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# create keyboard
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    rezise_keyboard=True
)

# create buttons
btn_1 = KeyboardButton(text=LEXICON_RU['rock'])
btn_2 = KeyboardButton(text=LEXICON_RU['scissors'])
btn_3 = KeyboardButton(text=LEXICON_RU['paper'])

# create keyboard with buttons
game_kb = ReplyKeyboardMarkup(
    keyboard=[[btn_1], [btn_2], [btn_3]],
    resize_keyboard=True
)
