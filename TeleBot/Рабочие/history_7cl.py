from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from telegram import Update
from config import TOKEN
from history_7cl_f import*
from test_1 import*
from test_2 import*
from test_3 import*

updater=Updater(TOKEN)
dispatcher=updater.dispatcher

start_handler=CommandHandler('start', start)
cancel_handler=CommandHandler('cancel',cancel)
show_test_handler=CommandHandler('show',show_test)

test_1_handler=ConversationHandler(
    entry_points=[MessageHandler(Filters.regex(f"^{name_test_1}"), test_1)], 
    states={
        QUESTION_1_1: [MessageHandler(Filters.text, question_1_1) ],
        QUESTION_1_2: [MessageHandler(Filters.text, question_1_2) ],
        QUESTION_1_3: [MessageHandler(Filters.text,question_1_3) ],
        QUESTION_1_4: [MessageHandler(Filters.text,question_1_4) ],
        QUESTION_1_5: [MessageHandler(Filters.text,question_1_5) ],
        RESULT_TEST_1: [MessageHandler(Filters.text, result_test_1)]
        },       
        fallbacks=[CommandHandler('cancel',cancel)],
)

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

test_number_handler=MessageHandler(Filters.text, test_number)
#test_1_handler=MessageHandler(Filters.regex(f"^{name_test_1}"), test_1)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(show_test_handler)
dispatcher.add_handler(test_1_handler)
dispatcher.add_handler(test_2_handler)
dispatcher.add_handler(test_3_handler)

dispatcher.add_handler(test_number_handler)

print('Сервер запущен')
updater.start_polling()
updater.idle()
