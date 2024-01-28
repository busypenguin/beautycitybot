from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from saloons.models import Master, Saloon, Service


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
        'show_prices': show_prices,
    }
    COMMANDS[update.callback_query.data](update, context)


def create_keyboard(queryset):
    """Создает вертикальную клавиатуру с наименованиями объектов из Queryset"""
    keyboard = [
        [InlineKeyboardButton(
            item.name,
            callback_data=item.name
        )] for item in queryset
    ]
    return InlineKeyboardMarkup(keyboard)


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
                callback_data='pdconsent_refuse'
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
    keyboard = [
        [InlineKeyboardButton(
            saloon.name,
            callback_data=f'show_saloon_services {saloon.id}'
        )] for saloon in saloons
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Список салонов:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# masters
def show_masters(update, context):
    """Вывести список мастеров."""
    masters = Master.objects.all()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Наши мастера:",
        reply_markup=create_keyboard(masters)
    )


# services
def show_services(update, context):
    """Вывести список услуг."""
    services = Service.objects.all()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Наши услуги:",
        reply_markup=create_keyboard(services)
    )


def show_saloon_services(update, context):
    """Показать услуги доступные в салоне."""
    saloon_id = update.callback_query.data.split()[1]
    saloon_services = Service.objects.filter(saloons=saloon_id)
    price_list = '\n'.join(
        f'{service.name} - {service.price}р.' for service in saloon_services)
    keyboard = [
        [
            InlineKeyboardButton(
                'Показать цены на все услуги',
                callback_data='show_prices',
            )
        ],
        [
            InlineKeyboardButton(
                'Показать даты для записи',
                callback_data='show_days',
            )
        ],
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Услуги салона {Saloon.objects.get(id=saloon_id)}:\n' +
             f'{price_list}',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# prices
def show_prices(update, context):
    """Показать цены на все услуги сети."""
    services = Service.objects.all()
    price_list = '\n'.join(
        f'{service.name} - {service.price}р.' for service in services)
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Цены на наши услуги:\n" + price_list,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Выбрать услугу",
                        callback_data="show_services"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Позвонить менеджеру ☎️",
                        callback_data='use_call'
                    ),
                ]
            ]))


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
