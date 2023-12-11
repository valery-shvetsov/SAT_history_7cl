from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from history_7cl_f import*
import time

QUESTION_1_1, QUESTION_1_2, QUESTION_1_3, QUESTION_1_4, QUESTION_1_5, RESULT_TEST_1  = range(6)
name_test_1='Тест 1. Василий III'

def test_1 (update:Update, context:CallbackContext):
    '''
    Запуск теста 1 Василий III
    '''
    print ('Тест 1: Василий III')

    chat_id=update.message.chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open('images/vasili3.jpg', 'rb'))

    update.message.reply_text ('Тест 1: Василий III')
    reply_keyboard=[
                    ['/begin']
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Начните тест',
        reply_markup=markup_key,)
    
    global number_correct_answer
    global answer
    global questions_count_test_1
    global start_time
    global end_time
    start_time=time.time()
    questions_count_test_1=5
    number_correct_answer=0
    print (number_correct_answer)
    return QUESTION_1_1

def question_1_1 (update:Update, context:CallbackContext):
    """
   
    """
    
    reply_keyboard=[
                    ['1405'],
                    ['1505'],
                    ['1503'],
                    ['1533'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 1: \nВ каком году  взошел на престол Василий III ?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_1_2

def question_1_2 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='1503':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['23 года'],
                    ['24 года'],
                    ['26 лет'],
                    ['28 лет'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 2: \nВ каком возрасте взошел на престол Василий III ?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_1_3

def question_1_3 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='26 лет':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['Федор'],
                    ['Иван'],
                    ['Николай'],
                    ['Борис'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 3: \nКак звали отца Василия III ?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_1_4

def question_1_4 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='Иван':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['Марфа'],
                    ['Елена'],
                    ['Мария'],
                    ['Софья'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 4: \nКак звали мать Василия III ?\nВыберите ответ',
        reply_markup=markup_key,)
    return QUESTION_1_5

def question_1_5 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='Софья':
        update.message.reply_text('Правильно \U0001F44D')
        number_correct_answer+=1
        print (number_correct_answer)
    else:
        update.message.reply_text('Не верно \U0001F44E')
        print (number_correct_answer)

    reply_keyboard=[
                    ['Иван'],
                    ['Гавриил'],
                    ['Степан'],
                    ['Кузьма'],
                    ]
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
    update.message.reply_text('Вопрос 4: \nКакое христианское имя было у Василия III ?\nВыберите ответ',
        reply_markup=markup_key,)

    return RESULT_TEST_1

def result_test_1 (update:Update, context:CallbackContext):
    """
    """
    answer=update.message.text
    #answer=update.message.reply_text
    global number_correct_answer
    print (answer)
    if answer=='Гавриил':
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


    global questions_count_test_1
    global start_time
    global end_time
    end_time=time.time()
    test_time=round(end_time-start_time)
    grade=round(number_correct_answer/questions_count_test_1*100,1)
    

    user = update.message.from_user.first_name
    update.message.reply_text(f'{user}, вы хорошо поработали')
    print ('Количество вопросов: ', questions_count_test_1)
    print ('Количество правильных ответов: ', number_correct_answer)
    print ('Процент правильных ответов: ', grade)
    update.message.reply_text(f'Количество вопросов: {questions_count_test_1}\nКоличество правильных ответов: {number_correct_answer} \nУ вас {grade} % правильных ответов \nВремя прохождения теста : {test_time} секунд')
    update.message.reply_text('Тест окончен. \nДля продолжения работы введите /start')

    return ConversationHandler.END