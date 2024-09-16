import telebot

# Please register your bot in Telegram (https://t.me/BotFather) and enter your token below

bot = telebot.TeleBot("ENTER_YOUR_TOKEN_HERE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to my bot! Good to see you!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Your request is being processed. Please wait for a reply message.")

@bot.message_handler(commands=['helloWorld'])
def send_helloWorld(message):
    bot.reply_to(message, "You have written the first programming phrase! Congratulations!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()