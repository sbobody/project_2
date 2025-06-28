import telebot
import config
import logic
bot = telebot.TeleBot(config.key)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который поможет тебе найти новые идеи для развития карьеры и в выборе работы. Напиши /help, чтобы узнать, как пользоваться ботом.')
    bot.send_message(message.chat.id, 'Как вас зовут?')
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    logic.create_user(message.text, message.chat.id, message.from_user.id)
    bot.send_message(message.chat.id, 'Спасибо, ' + message.text + '.  Вы зарегестрированы.')
    
bot.infinity_polling()








