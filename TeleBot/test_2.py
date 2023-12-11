#Модуль теста №2
    #Импорт необходимых модулей
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from history_7cl_f import*
import time

QUESTION_2_1, QUESTION_2_2, QUESTION_2_3, QUESTION_2_4, QUESTION_2_5, RESULT_TEST_2  = range(6)
name_test_2='Тест 2. Иван IV до 1560г'

    #Запуск теста 2
def test_2 (update:Update, context:CallbackContext):
    '''
    Запуск теста 2 Иван IV до 1560г
    '''
    print ('Тест 2. Иван IV до 1560г')

    chat_id=update.message.chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open('images/IvanIV_1.jpg', 'rb'))

    update.message.reply_text ('Тест 2. Иван IV до 1560г')
    reply_keyboard=[
                    ['/begin']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Начните тест',
        reply_markup=markup_key,)
    
    global number_correct_answer
    global answer
    global questions_count_test_2
    global start_time
    global end_time
    start_time=time.time()
    questions_count_test_2=5
    number_correct_answer=0
    print (number_correct_answer)
    return QUESTION_2_1

    #Модуль вопроса 2_1
def question_2_1 (update:Update, context:CallbackContext):
   
    reply_keyboard=[
                    ['1528'],
                    ['1530'],
                    ['1532'],
                    ['1531'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 1: \nВ каком году  родился Иван IV?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_2_2

    #Модуль вопроса 2_2
def question_2_2 (update:Update, context:CallbackContext):
    answer=update.message.text
    global number_correct_answer
    print (answer)
    if answer=='1530':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['1532'],
                    ['1533'],
                    ['1535'],
                    ['1537'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 2: \nВ каком году  взошел на престол Иван IV\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_2_3

    #Модуль вопроса 2_3
def question_2_3 (update:Update, context:CallbackContext):
    answer=update.message.text
    global number_correct_answer
    print (answer)
    if answer=='1533':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['Василий Шуйский'],
                    ['Алексей Адашев'],
                    ['Елена Глинская'],
                    ['Малюта Скуратов'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 3: \nКто был регентом до 1538г?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_2_4

    #Модуль вопроса 2_4
def question_2_4 (update:Update, context:CallbackContext):
    answer=update.message.text
    global number_correct_answer
    print (answer)
    if answer=='Елена Глинская':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['Рубль'],
                    ['Гривна'],
                    ['Алтын'],
                    ['Копейка'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 4: \nКак стали называть серебряную монету весом равную новгородской деньге?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_2_5

    #Модуль вопроса 2_5
def question_2_5 (update:Update, context:CallbackContext):
    answer=update.message.text
    global number_correct_answer
    print (answer)
    if answer=='Копейка':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['Кремль'],
                    ['Детинец'],
                    ['Китай-город'],
                    ['Палисад'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 4: \nКак называлась крепость с 12 башнями, возведенная в Москве во время регентства Елены Глинской?\nВыберите ответ',
        reply_markup=markup_key,)

    return RESULT_TEST_2

    #Модуль результатов теста №2
def result_test_2 (update:Update, context:CallbackContext):
    answer=update.message.text
    global number_correct_answer
    print (answer)
    if answer=='Китай-город':
        update.message.reply_text('Правильно \U0001F44D',
        reply_markup=ReplyKeyboardRemove(),
    )
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E',
        reply_markup=ReplyKeyboardRemove(),
    )
        print (number_correct_answer)

    global questions_count_test_2
    global start_time
    global end_time
    end_time=time.time()
    test_time=round(end_time-start_time)
    grade=round(number_correct_answer/questions_count_test_2*100,1)

    user = update.message.from_user.first_name
    update.message.reply_text(f'{user}, вы хорошо поработали')
    print ('Количество вопросов: ', questions_count_test_2)
    print ('Количество правильных ответов: ', number_correct_answer)
    print ('Процент правильных ответов: ', grade)
    update.message.reply_text(f'Количество вопросов: {questions_count_test_2}\nКоличество правильных ответов: {number_correct_answer} \nУ вас {grade} % правильных ответов \nВремя прохождения теста : {test_time} секунд')
    update.message.reply_text('Тест окончен. \nДля продолжения работы введите /start')

    return ConversationHandler.END