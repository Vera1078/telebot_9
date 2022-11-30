import telebot
import requests

bot = telebot.TeleBot("токен", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, как дела?")



@bot.message_handler(content_types=["text", "sticker"])
def function_name(message):
	
	text = message.text
	
	if "привет" in text.lower():
		bot.reply_to(message, f"Привет, {message.from_user.first_name}! Чтобы узнать погоду, введите слово 'погода'")

	elif "погода" in text.lower():
		weather=requests.get("https://wttr.in/?0T")
		bot.reply_to(message, weather.text)	

	
bot.polling(non_stop=True, interval=1)

