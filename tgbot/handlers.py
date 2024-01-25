# start
def start_callback(update, context):
    update.message.reply_text("Добро пожаловать в салон BeautyCity!\n" +
                              "Чтобы записаться на процедуру через бота нажми /use_bot\n" +
                              "Чтобы записаться на процедуру через менеджера /use_call")


# usage
def use_call(update, context):
    update.message.reply_text(
        "Запишитесь на процедуру у нашего менеджера по номеру +79371234567")


def use_bot(update, context):
    update.message.reply_text("")


def ask_pdconsent(update, context):
    update.message.reply_text(
        "Сервис запрашивает согласие на обработку персональных данных")
    doc_path = r'./assets/Согласие на обработку персональных данных.pdf'
    with open(doc_path, 'rb') as f:
        context.bot.sendDocument(chat_id=update.effective_chat.id, document=f)


def pdconsent_refuse(update, context):
    update.message.reply_text("Досвидания")


# location
def show_locations(update, context):
    update.message.reply_text("Адреса салонов:")


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
