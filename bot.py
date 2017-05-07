import telebot
from player import Player
from states import states
import time
import config
from telebot import types
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

    player: Player = players[message.chat.id]
    change_state(message)
    show_content(player)


contentFunctions = {"text": bot.send_message, "photo": bot.send_photo}


def show_content(player):
    current_state = player.current_state
    content: ContentUnit = current_state.content
    buttons = player.current_state.buttons
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    if current_state.callback:
        current_state.callback()
    for key in buttons.keys():
        markup.add(key)
    for contentUnit in content:
        contentFunctions[contentUnit.type](player.id, contentUnit.value, reply_markup=markup)
        time.sleep(delay)


def change_state(message):
    player = players[message.chat.id]
    current_state = player.current_state
    buttons = current_state.buttons

    if (message.text in buttons):
        player.current_state = states[buttons[message.text]]
    else:
        player.current_state = current_state.default_children



if __name__ == '__main__':
    bot.polling(none_stop=True)
