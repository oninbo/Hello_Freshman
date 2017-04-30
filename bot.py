import telebot
from player import Player
import time
import config
from states import states
from telebot import types
from contentUnit import ContentUnit

bot = telebot.TeleBot(config.token)

players = {}

delay = 0.5




@bot.message_handler(commands=['start'])
def start_game(message):
    player_id = message.chat.id
    player = Player(player_id)
    players[player_id] = player
    start_state_key = player.current_state_key
    show_content(states[start_state_key], player_id)
    #switch_state()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def read_message(message):
    if message.chat.id in players.keys():
        switch_state(message)

contentFunctions = {"text":bot.send_message,"photo":bot.send_photo}

def show_content(state, id):
    content: ContentUnit = state.content
    buttons = state.buttons
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for key in buttons.keys():
        markup.add(key)
    for contentUnit in content:
        contentFunctions[contentUnit.type](id,contentUnit.value,reply_markup = markup)
        time.sleep(delay)


def switch_state(message):
    player: Player = players[message.chat.id]
    old_state = states[player.current_state_key]
    new_state_key = old_state.get_next_state(message, player)
    player.current_state_key = new_state_key
    new_state = states[new_state_key]
    if new_state.callback:
        new_state.callback()
    show_content(states[new_state_key], player.id)




if __name__ == '__main__':
    bot.polling(none_stop=True)
