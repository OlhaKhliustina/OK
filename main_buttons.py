import telebot
import important_materials
import answers as ans
import collages
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Створюємо бота
bot = telebot.TeleBot(important_materials.TOKEN)


# Створюємо функцію для відправлення повідомлення з клавіатурою
@bot.message_handler(commands=['faq'])
def start(start_message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # Створюємо клавіатуру
    # Додаємо кнопки
    keyboard.add(KeyboardButton('Про коледжі'))
    keyboard.add(KeyboardButton('Загальні питання'))
    keyboard.add(KeyboardButton('Про освітню програму'))
    keyboard.add(KeyboardButton('Про відбір'))
    keyboard.add(KeyboardButton('Про стипендії та вартість навчання'))
    keyboard.add(KeyboardButton('Про анкету'))
    keyboard.add(KeyboardButton('Про біженців та осіб, що проживають на тимчасово окупованих територіях'))
    keyboard.add(KeyboardButton('<< Назад'))
    bot.send_message(chat_id=start_message.chat.id, text='Обери, що саме Тебе цікавить:', reply_markup=keyboard)


# Обробка відповідей на кнопки
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    match message.text:
        case 'Про коледжі':
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(
                KeyboardButton('Asia-Pacific'),
                KeyboardButton('Europe'),
                KeyboardButton('Africa'),
                KeyboardButton('Americas'),
                KeyboardButton('<< Назад'))
            bot.send_message(chat_id=message.chat.id, text='Про який регіон розказати детальніше?', reply_markup=keyboard)
        case 'Загальні питання':
            # Відправляємо наступні кнопки
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(KeyboardButton('Що таке UWC'))
            keyboard.add(KeyboardButton('Що таке Національний комітет'))
            keyboard.add(KeyboardButton('Як правильно вимовляти UWC'))
            keyboard.add(KeyboardButton('<< Назад'))
            bot.send_message(chat_id=message.chat.id, text='Оберіть наступне питання:', reply_markup=keyboard)
        case 'Про освітню програму':
            # Відправляємо наступні кнопки
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(KeyboardButton('Де продовжують навчання випускники UWC?'))
            keyboard.add(KeyboardButton('Чи визнають диплом Міжнародного бакалаврату в Україні?'))
            keyboard.add(KeyboardButton('<< Назад'))
            bot.send_message(chat_id=message.chat.id, text='Оберіть наступну кнопку:', reply_markup=keyboard)
        case 'Про відбір':
            # Виконуємо дії, пов'язані з кнопкою 3
            # Відправляємо наступні кнопки
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(KeyboardButton('Хто може подавати документи на програму?'))
            keyboard.add(KeyboardButton("Чи обов'язково знати англійську мову та на якому рівні?"))
            keyboard.add(KeyboardButton('Чи потрібно складати екзамени з математики чи англійської під час відбору?'))
            keyboard.add(KeyboardButton('Чи потрібно мені бути фізично присутнім на відборі?'))
            keyboard.add(KeyboardButton('Чи можу я подати заявку, якщо зараз беру gap year або навчаюся за програмою FLEX?'))
            keyboard.add(KeyboardButton('Якими є етапи відбору?'))
            keyboard.add(KeyboardButton('Якою мовою відбуваються 2, 3 та 4 етапи?'))
            keyboard.add(KeyboardButton('Якими є часові рамки відбору?'))
            keyboard.add(KeyboardButton('Якщо я стану фіналістом, чи зможу я обрати країну навчання?'))
            keyboard.add(KeyboardButton('<< Назад'))
            bot.send_message(chat_id=message.chat.id, text='Оберіть наступне питання:', reply_markup=keyboard)
        case 'Про анкету':
            # Відправляємо наступні кнопки
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(KeyboardButton('Скільки часу займає заповнення анкети?'))
            keyboard.add(KeyboardButton('Якою мовою заповнюється анкета?'))
            keyboard.add(KeyboardButton('Як додати в анкету рекомендаційний лист?'))
            keyboard.add(KeyboardButton('Чим відрізняється academic reference від non-academic reference?'))
            keyboard.add(KeyboardButton('Що робити, якщо я виїхав за кордон і не маю можливості отримати виписку з оцінками?'))
            keyboard.add(KeyboardButton('Як заповнити анкету, якщо я маю лише одного з батьків?'))
            keyboard.add(KeyboardButton('<< Назад'))
            bot.send_message(chat_id=message.chat.id, text='Оберіть наступне питання:', reply_markup=keyboard)
        case 'Про стипендії та вартість навчання':
            # Відправляємо наступні кнопки
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(KeyboardButton('Скільки коштує навчання в UWC?'))
            keyboard.add(KeyboardButton('Чи впливає спроможність моєї родини оплатити навчання на мої шанси стати фіналістом?'))
            keyboard.add(KeyboardButton('Чим відрізняється повні та часткові стипендії?'))
            keyboard.add(KeyboardButton('Які додаткові витрати не покриває стипендія?'))
            keyboard.add(KeyboardButton('Чи маєте ви особливі стипендії для біженців/дітей з особливими здібностями/переможцями олімпіад?'))
            keyboard.add(KeyboardButton('<< Назад'))
            bot.send_message(chat_id=message.chat.id, text='Оберіть наступне питання:', reply_markup=keyboard)
        case 'Про біженців та осіб, що проживають на тимчасово окупованих територіях':
            # Відправляємо наступні кнопки
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(KeyboardButton('Що робити, якщо я є біженцем та проживаю поза межами України?'))
            keyboard.add(KeyboardButton('Що робити, якщо я мешкаю на тимчасово окупованій території або був примусово депортований на територію іншої держави?'))
            keyboard.add(KeyboardButton('<< Назад'))
            bot.send_message(chat_id=message.chat.id, text='Оберіть наступне питання:', reply_markup=keyboard)
        case '<< Назад':
            start(message)

    bot.register_next_step_handler(message, on_click)


def on_click(message):
    match message.text:
        case 'Що таке UWC':
            bot.send_message(chat_id=message.chat.id, text=ans.ans1)
        case 'Що таке Національний комітет':
            bot.send_message(chat_id=message.chat.id, text=ans.ans2)
        case 'Як правильно вимовляти UWC':
            bot.send_message(chat_id=message.chat.id, text=ans.ans4)
        case 'Де продовжують навчання випускники UWC?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans5)
        case 'Чи визнають диплом Міжнародного бакалаврату в Україні?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans6)
        case 'Хто може подавати документи на програму?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans7)
        case "Чи обов'язково знати англійську мову та на якому рівні?":
            bot.send_message(chat_id=message.chat.id, text=ans.ans8)
        case 'Чи потрібно складати екзамени з математики чи англійської під час відбору?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans9)
        case 'Чи потрібно мені бути фізично присутнім на відборі?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans10)
        case 'Чи можу я подати заявку, якщо зараз беру gap year або навчаюся за програмою FLEX?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans11)
        case 'Якими є етапи відбору?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans12)
        case 'Якою мовою відбуваються 2, 3 та 4 етапи?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans13)
        case 'Якими є часові рамки відбору?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans14)
        case 'Якщо я стану фіналістом, чи зможу я обрати країну навчання?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans15)
        case 'Скільки часу займає заповнення анкети?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans16)
        case 'Якою мовою заповнюється анкета?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans17)
        case 'Як додати в анкету рекомендаційний лист?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans18)
        case 'Чим відрізняється academic reference від non-academic reference?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans19)
        case 'Що робити, якщо я виїхав за кордон і не маю можливості отримати виписку з оцінками?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans20)
        case 'Як заповнити анкету, якщо я маю лише одного з батьків?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans21)
        case 'Скільки коштує навчання в UWC?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans22)
        case 'Чи впливає спроможність моєї родини оплатити навчання на мої шанси стати фіналістом?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans23)
        case 'Чим відрізняється повні та часткові стипендії?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans24)
        case 'Які додаткові витрати не покриває стипендія?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans25)
        case 'Чи маєте ви особливі стипендії для біженців/дітей з особливими здібностями/переможцями олімпіад?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans26)
        case 'Що робити, якщо я є біженцем та проживаю поза межами України?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans27)
        case 'Що робити, якщо я мешкаю на тимчасово окупованій території або був примусово депортований на територію іншої держави?':
            bot.send_message(chat_id=message.chat.id, text=ans.ans28)
        case 'Asia-Pacific':
            for key, value in collages.asia.items():
                bot.send_message(chat_id=message.chat.id, text=f'{key}\n{value}')
        case 'Europe':
            for key, value in collages.europe.items():
                bot.send_message(chat_id=message.chat.id, text=f'{key}\n{value}')
        case 'Africa':
            for key, value in collages.africa.items():
                bot.send_message(chat_id=message.chat.id, text=f'{key}\n{value}')
        case 'Americas':
            for key, value in collages.americas.items():
                bot.send_message(chat_id=message.chat.id, text=f'{key}\n{value}')


# Запускаємо бота
bot.infinity_polling(none_stop=True)
