import telebot

bot = telebot.TeleBot("5677656640:AAEJyEMn7vK2bklqsxN1g54B2XTraZX1UHw", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как дела?")



content_types=["text"]

@bot.message_handler(content_types)
def function_name(message):
	bot.reply_to(message, "Это обработчик сообщений")

bot.polling(non_stop=True, interval=1)