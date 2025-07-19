import telebot
import config
import logic
bot = telebot.TeleBot(config.key)
import gpt

questions = ['Чем вы занимаетесь?', 'Сколько вам лет?', 'Чемы вы увлекаетесь?', 'Какая сфера деятельности интрересует?']
answers = {}

@bot.message_handler(commands=['start'])
def start(message):
    get = logic.get_user(message.from_user.id)
    if get:
        bot.send_message(message.chat.id, 'Вы уже зарегестрированы.Узнайте свой проффесию с командой /work')
    else:
        bot.send_message(message.chat.id, 'Привет, я бот, который поможет тебе найти новые идеи для развития карьеры и в выборе работы. Напиши /help, чтобы узнать, как пользоваться ботом.')
        bot.send_message(message.chat.id, 'Как вас зовут?')
        bot.register_next_step_handler(message, get_name)
def get_name(message):
    logic.create_user(message.text, message.chat.id, message.from_user.id)
    bot.send_message(message.chat.id, 'Спасибо, ' + message.text + '.  Вы зарегистрированы.')
    

@bot.message_handler(commands=['work'])
def help(message):
    bot.send_message(message.chat.id, questions[0])
    bot.register_next_step_handler(message, get_answer_1)

def get_answer_1(message):
    if message.from_user.id not in answers:
        answers[message.from_user.id] = []
    answers[message.from_user.id].append(message.text)
    bot.send_message(message.chat.id, questions[1])
    bot.register_next_step_handler(message, get_answer_2)

def get_answer_2(message):
    answers[message.from_user.id].append(message.text)
    bot.send_message(message.chat.id, questions[2])
    bot.register_next_step_handler(message, get_answer_3)

def get_answer_3(message):
    answers[message.from_user.id].append(message.text)
    bot.send_message(message.chat.id, questions[3])
    bot.register_next_step_handler(message, get_answer_4)


def get_answer_4(message):
    answers[message.from_user.id].append(message.text)
    logic.write_user_answer(message.from_user.id," ".join(answers[message.from_user.id]))
    text_answers = gpt.gpt(f"пользователю задали вопровы - {' '.join(questions)}, его ответы - {' '.join(answers[message.from_user.id])}. Какую проффесию можно рекомендовать?")
    bot.send_message(message.chat.id, text_answers)
    answers[message.from_user.id].clear()



bot.infinity_polling()








