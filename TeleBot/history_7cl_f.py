#Модуль с методами (функциями). Содержит методы, используемые при работе. 

    #Импорт необходимых модулей
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from test_1 import*
from test_2 import*
from test_3 import*
#from history_7cl import*

#Создание списка номеров тестов
TEST_NUMBER = range(2)

def start (update:Update,context:CallbackContext):
    #Действия при вводе команды start
        #Получение данных об адресате (chat.id)
    chat_id=update.message.chat.id
        #Выдача изображения на заставку бота   
    context.bot.send_photo(chat_id=chat_id, photo=open('images/History.jpg', 'rb'))
        #Получение данных имени (first_name) из chat.id
    user = update.message.from_user.first_name
        #Формирование приветствия пользователю
    update.message.reply_text(f'{user}, вас приветствует бот для проверки \nзнаний по истории. 7 класс')
        #Формирование клавиатуры выбора действия show/cancel (Выбора теста или выхода из бота)
    reply_keyboard=[
                    ['/show','/cancel']
                    ]
        #Назначение переменной клавиатуры
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
        #Сообщение о необходимости выбора действия: выбор теста/выход, фиксация выбора
    update.message.reply_text('Выберите тест или выйдите из программы',                   
        reply_markup=markup_key,)
    return


def show_test(update:Update, context:CallbackContext):
    #Действия при вводе команды show_test
        #Формирование клавиатуры выбора номера теста
    reply_keyboard=[
                    [name_test_1],
                    [name_test_2],
                    [name_test_3]
                    ]
        #Назначение переменной клавиатуры
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
        #Сообщение о необходимости выбора теста с фиксацией выбранного теста    
    update.message.reply_text('Выберите тест',
        reply_markup=markup_key,)

def test_number (update:Update, context:CallbackContext):
#Метод получения сообщения с переменной test_number 
    #Получение сообщения с переменной test_number  
    test_number=update.message.text 
    #Печать в консоль переменной test_number
    print (test_number) 
    return

def cancel (update:Update, context:CallbackContext):
#Действия при вводе команды cancel - Завершение работы
    #Передача сообщения об окончании работы
    update.message.reply_text (f'Работа окончена\nДля возобновления работы нажмите /start')
    return #ConversationHandler. END



