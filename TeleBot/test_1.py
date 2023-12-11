#Модуль теста №1
    #Импорт необходимых модулей
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from history_7cl_f import*
import time

    #Формирование списка вопросов
QUESTION_1_1, QUESTION_1_2, QUESTION_1_3, QUESTION_1_4, QUESTION_1_5, RESULT_TEST_1  = range(6)
    #Присвоение переменной name_test_1 названия теста
name_test_1='Тест 1. Василий III'

    #Запуск теста 1
def test_1 (update:Update, context:CallbackContext):
        #Печать сообщения с название теста на консоль
    print ('Тест 1: Василий III')
        #Получение chat.id
    chat_id=update.message.chat.id
        #Выдача изображения к тесту №1
    context.bot.send_photo(chat_id=chat_id, photo=open('images/vasili3.jpg', 'rb'))
        #Выдача сообщения с Названием теста №1
    update.message.reply_text ('Тест 1: Василий III')
        #Формирование кнопки начала теста begin
    reply_keyboard=[
                    ['/begin']
                    ]
        #Назначение переменной кнопки
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
        #Сообщение о необходимости начать тест
    update.message.reply_text('Начните тест',
        #Присвоение переменой выбора=выбор пользователя    
        reply_markup=markup_key,)
    
        #Назначение глобальных преременных
    global number_correct_answer
    global answer
    global questions_count_test_1
        #Назначение глобальных переменных фиксации времени
    global start_time
    global end_time

        #Фиксация времени начала теста
    start_time=time.time()
        #Назначение переменной количества вопросов
    questions_count_test_1=5
        #Назначение переменной количества правильных ответов
    number_correct_answer=0
        #Печать на консоль переменной количества правильных ответов
    print (number_correct_answer)
        #Передача в управляющий модуль QUESTION_1_1
    return QUESTION_1_1

    #Модуль вопроса 1_1
def question_1_1 (update:Update, context:CallbackContext):
    #Вопрос 1_1
        #Формирование клавиатуры выбора ответа вопроса 1_1
    reply_keyboard=[
                    ['1405'],
                    ['1505'],
                    ['1503'],
                    ['1533'],
                    ]
        #Назначение переменной клавиатуры
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
        #Передача сообщения с вопросом
    update.message.reply_text('Вопрос 1: \nВ каком году  взошел на престол Василий III ?\nВыберите ответ',
        reply_markup=markup_key,)
        #Передача в управляющий модуль QUESTION_1_2
    return QUESTION_1_2

    #Модуль вопроса 1_2
def question_1_2 (update:Update, context:CallbackContext):
        #Запись в переменную answer сообщения об ответе на вопрос 1_1
    answer=update.message.text
        #Назначение глобальной переменной number_correct_answer 
    global number_correct_answer
        #Печать на консоль ответа на ворос 1_1
    print (answer)
        #Сравнение ответа пользователя с правильным
        #Если ответ полльзователя=правильному
    if answer=='1503':
            #Отправляем сообщени "Правильно"
        update.message.reply_text('Правильно \U0001F44D')
            #К переменной number_correct_answer добавляем 1
        number_correct_answer+=1
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)
        #Если ответ неправильный        
    else:
            #Отправляем сообщени "Не верно" 
        update.message.reply_text('Не верно \U0001F44E')
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)
        #Формирование клавиатуры выбора ответа вопроса 1_2
    reply_keyboard=[
                    ['23 года'],
                    ['24 года'],
                    ['26 лет'],
                    ['28 лет'],
                    ]
        #Назначение переменной клавиатуры вопроса 1_2
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
        #Передача сообщения с вопросом 1_2 с получением ответа
    update.message.reply_text('Вопрос 2: \nВ каком возрасте взошел на престол Василий III ?\nВыберите ответ',
        reply_markup=markup_key,)
        #Передача в управляющий модуль QUESTION_1_3
    return QUESTION_1_3

    #Модуль вопроса 1_3
def question_1_3 (update:Update, context:CallbackContext):
        #Запись в переменную answer сообщения об ответе на вопрос 1_2
    answer=update.message.text
        #Назначение глобальной переменной number_correct_answer 
    global number_correct_answer
        #Печать на консоль ответа на ворос 1_2
    print (answer)
        #Сравнение ответа пользователя с правильным
        #Если ответ полльзователя=правильному
    if answer=='26 лет':
            #Отправляем сообщени "Правильно"
        update.message.reply_text('Правильно \U0001F44D')
            #К переменной number_correct_answer добавляем 1        
        number_correct_answer+=1
            #На консоль печатаем количество правильных ответов        
        print (number_correct_answer)
        #Если ответ неправильный
    else:
            #Отправляем сообщени "Не верно" 
        update.message.reply_text('Не верно \U0001F44E')
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)
        #Формирование клавиатуры выбора ответа для вопросв 1_3
    reply_keyboard=[
                    ['Федор'],
                    ['Иван'],
                    ['Николай'],
                    ['Борис'],
                    ]
        #Назначение переменной клавиатуры вопроса 1_3
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
        #Передача сообщения с вопросом 1_3 с получением ответа
    update.message.reply_text('Вопрос 3: \nКак звали отца Василия III ?\nВыберите ответ',                             
        reply_markup=markup_key,)
        #Передача в управляющий модуль QUESTION_1_4
    return QUESTION_1_4

    #Модуль вопроса 1_4
def question_1_4 (update:Update, context:CallbackContext):
        #Запись в переменную answer сообщения об ответе на вопрос 1_3
    answer=update.message.text
        #Назначение глобальной переменной number_correct_answer 
    global number_correct_answer
        #Печать на консоль ответа на ворос 1_3
    print (answer)
        #Сравнение ответа пользователя с правильным
        #Если ответ полльзователя=правильному
    if answer=='Иван':
            #Отправляем сообщени "Правильно"
        update.message.reply_text('Правильно \U0001F44D')
            #К переменной number_correct_answer добавляем 1
        number_correct_answer+=1
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)
        #Если ответ неправильный
    else:
            #Отправляем сообщени "Не верно" 
        update.message.reply_text('Не верно \U0001F44E')
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)
        #Формирование клавиатуры выбора ответа для вопросв 1_4
    reply_keyboard=[
                    ['Марфа'],
                    ['Елена'],
                    ['Мария'],
                    ['Софья'],
                    ]
        #Назначение переменной клавиатуры вопроса 1_4
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
        #Передача сообщения с вопросом 1_4 с получением ответа
    update.message.reply_text('Вопрос 4: \nКак звали мать Василия III ?\nВыберите ответ',
        reply_markup=markup_key,)
        #Передача в управляющий модуль QUESTION_1_5
    return QUESTION_1_5

    #Модуль вопроса 1_5
def question_1_5 (update:Update, context:CallbackContext):
        #Запись в переменную answer сообщения об ответе на вопрос 1_4
    answer=update.message.text
        #Назначение глобальной переменной number_correct_answer 
    global number_correct_answer
        #Печать на консоль ответа на ворос 1_4
    print (answer)
        #Сравнение ответа пользователя с правильным
        #Если ответ полльзователя=правильному        
    if answer=='Софья':
            #Отправляем сообщение "Правильно"  
        update.message.reply_text('Правильно \U0001F44D')
            #К переменной number_correct_answer добавляем 1
        number_correct_answer+=1
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)
        #Если ответ неправильный
    else:
            #Отправляем сообщение "Не верно" 
        update.message.reply_text('Не верно \U0001F44E')
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)
        #Формирование клавиатуры выбора ответа для вопросв 1_5
    reply_keyboard=[
                    ['Иван'],
                    ['Гавриил'],
                    ['Степан'],
                    ['Кузьма'],
                    ]
        #Назначение переменной клавиатуры вопроса 1_5
    markup_key=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True,)
        #Передача сообщения с вопросом 1_5 с получением ответа
    update.message.reply_text('Вопрос 4: \nКакое христианское имя было у Василия III ?\nВыберите ответ',
        reply_markup=markup_key,)
        #Передача в управляющий модуль RESULT_TEST_1
    return RESULT_TEST_1

    #Модуль результатов прохождения теста_1
def result_test_1 (update:Update, context:CallbackContext):
        #Запись в переменную answer сообщения об ответе на вопрос 1_5
    answer=update.message.text
        #Назначение глобальной переменной number_correct_answer 
    global number_correct_answer
        #Печать на консоль ответа на ворос 1_5    
    print (answer)
        #Сравнение ответа пользователя с правильным
        #Если ответ полльзователя=правильному        
    if answer=='Гавриил':
            #Отправляем сообщение "Правильно"  
        update.message.reply_text('Правильно \U0001F44D',
            #Убираем клавиатуру выбора ответа                           
        reply_markup=ReplyKeyboardRemove(),
    )
            #К переменной number_correct_answer добавляем 1
        number_correct_answer+=1
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)
        #Если ответ неправильный
    else:
            #Отправляем сообщение "Не верно" 
        update.message.reply_text('Не верно \U0001F44E',
            #Убираем клавиатуру выбора ответа                     
        reply_markup=ReplyKeyboardRemove(),
    )
            #На консоль печатаем количество правильных ответов
        print (number_correct_answer)

    #global questions_count_test_1
    #global start_time
    #global end_time
        #Фиксация времени окончания теста
    end_time=time.time()
        #Вычисление округленного времени прохождения теста
    test_time=round(end_time-start_time)
        #Вычисление процента правильных ответов
    grade=round(number_correct_answer/questions_count_test_1*100,1)
        #Формирование сообщения о результатах прохождения теста
        #Фиксируем имя пользователя
    user = update.message.from_user.first_name
        #Отправляем сообщение, что пользователь хорошо поработал
    update.message.reply_text(f'{user}, вы хорошо поработали')
        #Отправляем сообщение, с результатами прохождения теста
    update.message.reply_text(f'Количество вопросов: {questions_count_test_1}\nКоличество правильных ответов: {number_correct_answer} \nУ вас {grade} % правильных ответов \nВремя прохождения теста : {test_time} секунд')
        #Отправляем сообщение о том, что тест окончен
    update.message.reply_text('Тест окончен. \nДля продолжения работы введите /start')
        #Результаты прохождения выводим на консоль
    print ('Количество вопросов: ', questions_count_test_1)
    print ('Количество правильных ответов: ', number_correct_answer)
    print ('Процент правильных ответов: ', grade)
    return ConversationHandler.END