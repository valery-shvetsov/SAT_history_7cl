from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from history_7cl_f import*
import time

QUESTION_3_1, QUESTION_3_2, QUESTION_3_3, QUESTION_3_4, QUESTION_3_5, RESULT_TEST_3  = range(6)
name_test_3='Тест 3. Иван IV после 1560г'

def test_3 (update:Update, context:CallbackContext):
    '''
    Тест 3. Иван IV после 1560г
    '''
    print ('Тест 3. Иван IV после 1560г')

    chat_id=update.message.chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open('images/IvanIV_2.jpg', 'rb'))

    update.message.reply_text ('Тест 3. Иван IV после 1560г')
    reply_keyboard=[
                    ['/begin']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Начните тест',
        reply_markup=markup_key,)
    
    global number_correct_answer
    global answer
    global questions_count_test_3
    global start_time
    global end_time
    start_time=time.time()
    questions_count_test_3=5
    number_correct_answer=0
    print (number_correct_answer)
    return QUESTION_3_1

def question_3_1 (update:Update, context:CallbackContext):
    """
   
    """
    
    reply_keyboard=[
                    ['1558-1583'],
                    ['1558-1585'],
                    ['1559-1583'],
                    ['1557-1582'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 1: \nКогда проходила Ливонская война?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_3_2

def question_3_2 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='1558-1583':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['Захватить Смоленск, Краков'],
                    ['Захватить Полоцк и Пинск'],
                    ['Захватить Ригу, Ревель и Нарву'],
                    ['Освободить Псков, Новгород, Трубеж'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 2: \nЧто Московское государство хотело приобрести в результате победы в Ливонской войне?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_3_3

def question_3_3 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='Захватить Ригу, Ревель и Нарву':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['Смерть Елены Глинской'],
                    ['Предательство Андрея Курбского'],
                    ['Смерть Анастасии Романовой'],
                    ['Введение Опричнины'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 3: \nКакое событие послужило поводом превращения Иван IV в Ивана Грозного?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_3_4

def question_3_4 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='Смерть Анастасии Романовой':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['1560'],
                    ['1562'],
                    ['1564'],
                    ['1565'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 4: \nДруг и соратник Ивана IV Андрей Курбский сбежал из Руси после того как Иван Грозный уничтожил всех остальных своих соратников и ближников. Когда это произошло??\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_3_5

def question_3_5 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='1564':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['1564-1573'],
                    ['1566-1573'],
                    ['1565-1572'],
                    ['1565-1573'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 4: \nКогда был период в истории России, который назвали Опричнина?\nВыберите ответ',
        reply_markup=markup_key,)

    return RESULT_TEST_3

def result_test_3 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='1565-1572':
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

    global questions_count_test_3
    global start_time
    global end_time
    end_time=time.time()
    test_time=round(end_time-start_time)
    grade=round(number_correct_answer/questions_count_test_3*100,1)

    user = update.message.from_user.first_name
    update.message.reply_text(f'{user}, вы хорошо поработали')
    print ('Количество вопросов: ', questions_count_test_3)
    print ('Количество правильных ответов: ', number_correct_answer)
    print ('Процент правильных ответов: ', grade)
    update.message.reply_text(f'Количество вопросов: {questions_count_test_3}\nКоличество правильных ответов: {number_correct_answer} \nУ вас {grade} % правильных ответов \nВремя прохождения теста : {test_time} секунд')
    update.message.reply_text('Тест окончен. \nДля продолжения работы введите /start')

    return ConversationHandler.END