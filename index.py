import telebot
from keyboardModule import questions, answers
globalCounter = 0
globalIterator = 0
bot = telebot.TeleBot('950817616:AAGTzkSWyjyLeFDWE_KB6lviZbpONM5JJEs')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здраствуйте 5 вопросов, просто напишите game в чат')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'jojo':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAI4Bl57h-dSW3UspiCZi7u22GbYjgevAAJ-AQAC-7JCAhGHzwxDARFnGAQ')
    elif message.text.lower() == 'game':
        game(message)


def game(message):
    global globalIterator, globalCounter
    if globalIterator < 5:
        msg = bot.send_message(message.chat.id, questions[globalIterator]["question"], reply_markup=answers[globalIterator])
        bot.register_next_step_handler(msg, process_step)
    else:
        bot.send_message(message.chat.id, f"Count of true answers: {globalCounter}")


def process_step(message):
    global globalIterator, globalCounter
    if message.text.lower() == questions[globalIterator]["answerTrue"].lower():
        bot.send_message(message.chat.id, "Excellent")
        globalCounter += 1
    else:
        bot.send_message(message.chat.id, "Bad")
    globalIterator += 1
    game(message)


bot.polling()
