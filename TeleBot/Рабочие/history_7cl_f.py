from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from test_1 import*
from test_2 import*
from test_3 import*
#from history_7cl import*

TEST_NUMBER = range(2)

def start (update:Update,context:CallbackContext):
    """
    Действия при вводе команды start
     
    """
    chat_id=update.message.chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open('images/History.jpg', 'rb'))

    user = update.message.from_user.first_name
    update.message.reply_text(f'{user}, вас приветствует бот для проверки \nзнаний по истории. 7 класс')
    #print('Вас приветствует бот для проверки знаний по истории. 7 класс')
    #print('/choose a test')
    reply_keyboard=[
                    ['/show','/cancel']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Выберите тест или выйдите из программы',
        reply_markup=markup_key,)
    return


# def choose_test(update:Update, context:CallbackContext):

#     reply_keyboard=[
#                     ['/test_1'],
#                     ['/test_2'],
#                     ['/test_3']
#                     ]
#     markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
#     update.message.reply_text('Выберите тест',
#         reply_markup=markup_key,)

def show_test(update:Update, context:CallbackContext):

    reply_keyboard=[
                    [name_test_1],
                    [name_test_2],
                    [name_test_3]
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Выберите тест',
        reply_markup=markup_key,)

def test_number (update:Update, context:CallbackContext): 
    test_number=update.message.text 
    print (test_number) 
#    if test_number=='Тест 1. Василий III':
#        test_1
#        print ('соответствует Тест 1 Василий III')
#         update.message.reply_text('/test_1')
#     elif test_number=='Тест 2. Иван IV до 1560г':
#         test_2
# #       print ('соответствует Тест 2. Иван IV до 1560г')
#         update.message.reply_text('/test_2')
#     elif test_number=='Тест 3. Иван IV после 1560г':
#         test_3
#        print ('соответствует Тест 3. Иван IV после 1560г')
#        update.message.reply_text('/test_3')    
    return

def cancel (update:Update, context:CallbackContext):
    """
    Действия при вводе команды cancel
    Завершение работы
    """
    update.message.reply_text (f'Работа окончена\nДля возобновления работы нажмите /start')
    return #ConversationHandler. END



