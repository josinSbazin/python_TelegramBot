# -*- coding: utf-8 -*-
import re
import config
import telebot

bomg = "Бомж"
regRusLetters = re.compile("^[а-яА-Яё]+$")

bot = telebot.TeleBot(config.token)


def second_vowels(text):
    pos = 0
    i = 1
    while i < len(text):
        if text[i] in "ауоыиэяюёе":
            pos = i
            break
        i = i + 1
    return pos


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Пришли мне слово на Русском и я его бомжирую!")


@bot.message_handler(content_types=["text"])
def repeat_all_mesages(message):
    response = "не могу бомжировать..."
    text = message.text.lower()
    if re.match(regRusLetters, text):
        pos = second_vowels(text)
        response = bomg + text[pos:]

    bot.send_message(message.chat.id, response)


if __name__ == '__main__':
    bot.polling(none_stop=True)
