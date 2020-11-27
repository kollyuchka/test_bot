# # -*- coding: utf-8 -*-
import telebot
import flask

from flask import Flask
from flask import request

import config

bot = telebot.TeleBot(config.TOKEN)
bot.remove_webhook()
bot.set_webhook(config.URL)



app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return {"ok": True}


@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    bot.reply_to(message, "Hello, did someone call for help?")


@bot.message_handler(content_types=['audio', 'video', 'document', 'location', 'contact', 'sticker'])
def default_command(message):
    bot.reply_to(message, "Hi."
                          "!")


if __name__ == "__main__":
    app.run(host="flask", port=5000)
