import telebot
from player import Player
import states
import time
import config
from states import states
from telebot import types
from typing import *
from state import State
import state
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
    change_state(message)


def show_content(player):
    content: ContentUnit = player.current_state.content
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for key in content.keys:
        markup.add(key)
 #   for photo in content.photos:
  #      bot.send_photo(player.id, photo)
    for message in content.text:
        bot.send_message(player.id, message, reply_markup=markup)
        time.sleep(delay)


def change_state(message):
    player_id = message.chat.id
    player = players[player_id]
    current_state: State = player.current_state
    #for foo in current_state.content.callback:
     #   foo(bot, player)
    if (message.text in current_state.children):
        current_state = states[message.text]
    else:
        current_state = states[current_state.default_children]
    player.current_state = current_state
    show_content(player)

if __name__ == '__main__':
    bot.polling(none_stop=True)
