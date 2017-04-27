import telebot
from player import Player
import states
import time
import config
from states import states
from telebot import types
from typing import *
from state import State
import states
from contentUnit import ContentUnit

bot = telebot.TeleBot(config.token)

players = {}

delay = 0.5




@bot.message_handler(commands=['start'])
def start_game(message):
    player = Player(message.chat.id)
    players[message.chat.id] = player
    show_content(player)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def switch_state(message):
    player:Player = players[message.chat.id]
    current_state = player.current_state
    if current_state.callback:
        current_state.callback()
    next_state = current_state.get_next_state(message, player)
    player.current_state = states[next_state]
    show_content(player)

contentFunctions = {"text":bot.send_message,"photo":bot.send_photo}

def show_content(player):
    content: ContentUnit = player.current_state.content
    buttons = player.current_state.buttons
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for key in buttons.keys():
        markup.add(key)
    for contentUnit in content:
        contentFunctions[contentUnit.type](player.id,contentUnit.value,reply_markup = markup)
        time.sleep(delay)







if __name__ == '__main__':
    bot.polling(none_stop=True)
