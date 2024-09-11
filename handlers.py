import telebot
from config import TOKEN, DELETE_DELAY, HEROES, CHAR_REPLACEMENTS, FORBIDDEN_WORDS, FORBIDDEN_PHRASES, URL_REGEX
from utils import contains_forbidden_word, contains_forbidden_phrase
import time

bot = telebot.TeleBot(TOKEN)
user_messages = {}
confirmed_users = set()

@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(message.chat.id, "Бот работает нормально.")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Пожалуйста, напишите слово 'ПОДТВЕРЖДАЮ', чтобы получить доступ к чату.")
    user_id = message.from_user.id
    confirmed_users.discard(user_id)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.from_user.id
    if user_id not in confirmed_users:
        if message.text.lower() == "подтверждаю":
            confirmed_users.add(user_id)
            bot.send_message(message.chat.id, "Вы подтвердили свое присутствие.")
        else:
            delete_message_and_notify(message.chat.id, message.message_id, "Сначала подтвердите свое присутствие.")
            return
    
    text = message.text.lower()
    if contains_forbidden_word(text) or contains_forbidden_phrase(text) or re.search(URL_REGEX, text):
        delete_message_and_notify(message.chat.id, message.message_id, "Сообщение удалено из-за использования запрещённых слов, фраз или ссылок.")
    
    user_messages[user_id] = user_messages.get(user_id, 0) + 1

@bot.message_handler(commands=['top'])
def handle_top(message):
    top_users = sorted(user_messages.items(), key=lambda x: x[1], reverse=True)[:10]
    top_message = "\n".join([f"Пользователь {user_id}: {count} сообщений" for user_id, count in top_users])
    bot.send_message(message.chat.id, f"Топ 10 пользователей:\n{top_message}")

def delete_message_and_notify(chat_id, message_id, notification_text):
    try:
        bot.delete_message(chat_id, message_id)
        notification_message = bot.send_message(chat_id, notification_text)
        time.sleep(DELETE_DELAY)
        bot.delete_message(chat_id, notification_message.message_id)
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Ошибка удаления сообщения: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
