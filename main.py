import telebot

TOKEN = "8879624458:AAFlgClHJ7V1L9YBhJRQ9K1kCruG4NnzwPc"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت شغال!")

print("البوت يعمل الآن...")
bot.polling()
