from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def sendMessage(update):
    keyboard = [
        [
            InlineKeyboardButton("Записаться через бота 🤖", callback_data="1"),
            InlineKeyboardButton("Записаться через менеджера ☎️", callback_data="use_call"),
        ]
    ]
   reply_markup = InlineKeyboardMarkup(keyboard)

   return update.message.reply_text("Please choose:", reply_markup=reply_markup)