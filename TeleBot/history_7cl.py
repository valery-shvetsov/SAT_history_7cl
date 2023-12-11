#Управляющий модуль. Производит управление всеми модулями бота. 

    #Импорт необходимых модулей
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update
from config import TOKEN
from history_7cl_f import*
from test_1 import*
from test_2 import*
from test_3 import*

    #Подключение бота к API (системе обмена информацией) с Telegram
    #для проверки Telegram на наличие новых сообщений в боте.
updater=Updater(TOKEN)
    #Передача управления классу dispatcher для подбора необходимого обработчика
dispatcher=updater.dispatcher
    #Обработчик входящих сообщений для команды start
start_handler=CommandHandler('start', start)
    #Обработчик входящих сообщений для команды cansel
cancel_handler=CommandHandler('cancel',cancel)
    #Обработчик входящих сообщений для команды show
show_test_handler=CommandHandler('show',show_test)
    #Обработчики входящих сообщений для теста №1
    # Обработчик для ведения беседы с одним пользователем
test_1_handler=ConversationHandler(
    # Запуск выдачи вопросов теста при получение сообщения с номером теста    
    entry_points=[MessageHandler(Filters.regex(f"^{name_test_1}"), test_1)], 
        # Выдача вопросов теста №1    
    states={
        QUESTION_1_1: [MessageHandler(Filters.text, question_1_1) ],
        QUESTION_1_2: [MessageHandler(Filters.text, question_1_2) ],
        QUESTION_1_3: [MessageHandler(Filters.text,question_1_3) ],
        QUESTION_1_4: [MessageHandler(Filters.text,question_1_4) ],
        QUESTION_1_5: [MessageHandler(Filters.text,question_1_5) ],
    # Выдача результатов прохождения теста
        RESULT_TEST_1: [MessageHandler(Filters.text, result_test_1)]
        }, 
    # Прерывание работы теста командой cansel      
        fallbacks=[CommandHandler('cancel',cancel)],
)
    #Обработчики входящих сообщений для теста №2
test_2_handler=ConversationHandler(
    entry_points=[MessageHandler(Filters.regex(f"^{name_test_2}"), test_2)], 
    states={
        QUESTION_2_1: [MessageHandler(Filters.text, question_2_1)],
        QUESTION_2_2: [MessageHandler(Filters.text, question_2_2)],
        QUESTION_2_3: [MessageHandler(Filters.text,question_2_3)],
        QUESTION_2_4: [MessageHandler(Filters.text,question_2_4)],
        QUESTION_2_5: [MessageHandler(Filters.text,question_2_5)],
        RESULT_TEST_2: [MessageHandler(Filters.text, result_test_2)]
        },       
        fallbacks=[CommandHandler('cancel',cancel)],
)
    #Обработчики входящих сообщений для теста №3
test_3_handler=ConversationHandler(
    entry_points=[MessageHandler(Filters.regex(f"^{name_test_3}"), test_3)], 
    states={
        QUESTION_3_1: [MessageHandler(Filters.text, question_3_1) ],
        QUESTION_3_2: [MessageHandler(Filters.text, question_3_2) ],
        QUESTION_3_3: [MessageHandler(Filters.text,question_3_3) ],
        QUESTION_3_4: [MessageHandler(Filters.text,question_3_4) ],
        QUESTION_3_5: [MessageHandler(Filters.text,question_3_5) ],
        RESULT_TEST_3: [MessageHandler(Filters.text, result_test_3)]
        },       
        fallbacks=[CommandHandler('cancel',cancel)],
)
    #Обработчик входящих сообщений для выбора теста
test_number_handler=MessageHandler(Filters.text, test_number)
    #Отправление всех видов обновлений своим зарегистрированным обработчикам
dispatcher.add_handler(start_handler)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(show_test_handler)
dispatcher.add_handler(test_1_handler)
dispatcher.add_handler(test_2_handler)
dispatcher.add_handler(test_3_handler)
dispatcher.add_handler(test_number_handler)
    #Печать в консоль сообщения о запуске сервера
print('Сервер запущен')
    #Команда начала проверки новых сообщений
updater.start_polling()
    #Команда продолжения проверки новых сообщений, для
    #продолжения действия скрипта start_polling, во время работы бота.
updater.idle()
