import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

sentences = [
    {"text": "When my time comes \nForget the wrong that I’ve done.", "level": 1},
    {"text": "In a hole in the ground there lived a hobbit.", "level": 2},
    {
        "text": "The sky the port was the color of television, tuned to a dead channel.",
        "level": 1,
    },
    {"text": "I love the smell of napalm in the morning.", "level": 0},
    {
        "text": "The man in black fled across the desert, and the gunslinger followed.",
        "level": 0,
    },
    {"text": "The Consul watched as Kassad raised the death wand.", "level": 1},
    {"text": "If you want to make enemies, try to change something.", "level": 2},
    {
        "text": "We're not gonna take it. \nOh no, we ain't gonna take it \nWe're not gonna take it anymore",
        "level": 1,
    },
    {
        "text": "I learned very early the difference between knowing the name of something and knowing something.",
        "level": 2,
    },
]

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду несколько предложений')

# Получение сообщений от юзера и визиваем ф-ции обработки и составления ответа
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, create_result_message(fill_matched_sentences(message)))

# Поиск предложений
def fill_matched_sentences(message):
    matched_sentences = []
    for sentence in sentences:
        sentences_txt = sentence.get("text")
        if message.text in sentences_txt:
            matched_sentences.append(sentences_txt)
    return matched_sentences

# Составление ответа юзеру
def create_result_message(matched_sentences: list) -> str:
    result_message = ""
    if not matched_sentences:
        result_message = "Sorry, not found sentences for your request"
    if len(matched_sentences) == 1:
        result_message = matched_sentences[0]
    if len(matched_sentences) > 1:
        for x in matched_sentences:
            result_message += x + "\n...\n"
    return result_message

# Запускаем бота
bot.polling(none_stop=True, interval=0)