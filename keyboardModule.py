import telebot

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard5 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)

questions = [{
    "question": "1. Banana color",
    "answerTrue": "Yellow",
    "answerFalse": "White"
    },
    {
        "question": "2. Red HEX",
        "answerFalse": "FF5434",
        "answerTrue": "FF0000"
    },
    {
        "question": "3. Yellow HEX",
        "answerFalse": "FH4512",
        "answerTrue": "FFFF00"
    },
    {
        "question": "4. Green HEX",
        "answerFalse": "98FB98",
        "answerTrue": "008000"
    },
    {
        "question": "5. Cyan HEX",
        "answerTrue": "00FFFF",
        "answerFalse": "AFEEEE"
    },
]

keyboard1.row(questions[0]["answerFalse"], questions[0]["answerTrue"])
keyboard2.row(questions[1]["answerTrue"], questions[1]["answerFalse"])
keyboard3.row(questions[2]["answerFalse"], questions[2]["answerTrue"])
keyboard4.row(questions[3]["answerTrue"], questions[3]["answerFalse"])
keyboard5.row(questions[4]["answerFalse"], questions[4]["answerTrue"])


answers = [keyboard1, keyboard2, keyboard3, keyboard4, keyboard5]