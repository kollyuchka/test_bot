# # -*- coding: utf-8 -*-
import telebot
import flask

from flask import Flask
from flask import request

import config

bot = telebot.TeleBot(config.TOKEN)


app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@app.route('/' + config.TOKEN, methods=['POST'])
def getMessage():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return "!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.URL + config.TOKEN)
    return "!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
