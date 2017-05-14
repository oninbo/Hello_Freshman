import telebot
from player import Player
from states import states
import time
import config
from telebot import types
from contentUnit import ContentUnit

bot = telebot.TeleBot(config.token)

players = {}


@bot.message_handler(commands=['start'])
def start_game(message):
    player = Player(message.chat.id)
    players[message.chat.id] = player
    show_content(player, message=None)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def switch_state(message):
    if (not message.chat.id in players.keys()):
        player = Player(message.chat.id)
        players[message.chat.id] = player
        show_content(player,message)
    else:
        player: Player = players[message.chat.id]
        change_state(message)
        show_content(player, message)


contentFunctions = {"text": bot.send_message, "photo": bot.send_photo}


def show_content(player, message):
    current_state = player.current_state
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    if current_state.callback:
        current_state.callback(player, message)
    current_state = player.current_state
    buttons = player.current_state.buttons
    content: ContentUnit = current_state.content
    if (buttons):
        for key in buttons.keys():
            markup.add(key)

    for contentUnit in content:
        content_function = contentFunctions[contentUnit.type]
        if contentUnit is content[-1]:
            content_function(player.id, contentUnit.value, reply_markup=markup)
        elif contentUnit is content[0]:
            content_function(player.id, contentUnit.value, reply_markup=types.ReplyKeyboardRemove())
        else:
            content_function(player.id, contentUnit.value)
        time.sleep(contentUnit.delay)


def change_state(message):
    player = players[message.chat.id]
    current_state = player.current_state
    buttons = current_state.buttons

    if (buttons and message.text in buttons):
        player.current_state = states[buttons[message.text]]
    else:
        player.current_state = states[current_state.default_children]





if __name__ == '__main__':
    bot.polling(none_stop=True)
