from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from saloons.models import Saloon


def callback_handler(update, context):
    """Запуск команд отловленных CallbackQueryHandler-ом."""
    COMMANDS = {
        'use_call': use_call,
        'use_bot': use_bot,
        'ask_pdconsent': ask_pdconsent,
        'pdconsent_refuse': pdconsent_refuse,
        'show_locations': show_locations,
        'show_masters': show_masters,
        'show_services': show_services,
    }
    COMMANDS[update.callback_query.data](update, context)


# start
def start_callback(update, context):
    """Стартовый вопрос."""
    update.message.reply_text(
        "Добро пожаловать в салон BeautyCity!\n" +
        "Выберите как вы хотите записаться на процедуру.",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "В боте 🤖",
                callback_data="use_bot"
            ),
            InlineKeyboardButton(
                "Через менеджера ☎️",
                callback_data='use_call'
            ),
        ]])
    )


# usage
def use_call(update, context):
    """Вывести контакты менеджера."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=("Запишитесь на процедуру у нашего менеджера по номеру"
              "+79371234567")
    )


def use_bot(update, context):
    """Вывести вопрос о согласии обработки персональных данных."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Подтвердите согласие на обработку персональных данных",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "✅",
                callback_data="ask_pdconsent"
            ),
            InlineKeyboardButton(
                "❌",
                callback_data='use_call'
            ),
        ]])
    )


def ask_pdconsent(update, context):
    """Отправить типовое согласие на обработку персональных данных."""
    doc_path = r'./assets/Согласие на обработку персональных данных.pdf'
    with open(doc_path, 'rb') as f:
        context.bot.sendDocument(chat_id=update.effective_chat.id, document=f)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Выберите вариант поиска",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "По салону",
                callback_data="show_locations"
            ),
            InlineKeyboardButton(
                "По мастеру",
                callback_data='show_masters'
            ),
            InlineKeyboardButton(
                "По услуге",
                callback_data='show_services'
            ),
        ]])
    )


def pdconsent_refuse(update, context):
    """Попрощаться после отказа предоставления персональных данных."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Досвидания"
    )


# location
def show_locations(update, context):
    """Вывести список салонов."""
    saloons = Saloon.objects.all()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Список салонов:"
        
    )


# masters
def show_masters(update, context):
    update.message.reply_text("Наши мастера:")


# services
def show_services(update, context):
    update.message.reply_text("Наши услуги:")


# prices
def show_prices(update, context):
    update.message.reply_text("Цены на услуги:")


# date and time
def show_days(update, context):
    update.message.reply_text("Выбирите день:")


def show_hours(update, context):
    update.message.reply_text("Выберите время:")


# registration
def ask_phone_number(update, context):
    update.message.reply_text("Введите номер телефона:")


def registration_success(update, context):
    update.message.reply_text("Вы успешно записаны на процедуру!")
