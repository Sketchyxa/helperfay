import telebot
from config import TOKEN
import handlers

bot = telebot.TeleBot(TOKEN)

if __name__ == "__main__":
    bot.polling()
