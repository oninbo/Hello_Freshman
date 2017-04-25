import telebot
from player import Player
import states
import time
import config
from states import states
from telebot import types

bot = telebot.TeleBot(config.token)

player = Player()

delay = 3


def show_content(state, playerID):
    content = state.content
    for message in content:
        text = message.value
        if player.name:
            text = text.replace("[player name]", player.name)
        if (message is content[-1] and len(state.choices)):
            buttons = state.choices.keys()
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            for button in buttons:
                markup.add(button)
            bot.send_message(playerID, text, reply_markup=markup)
        else:
            bot.send_message(playerID, text)
        time.sleep(delay)


@bot.message_handler(commands=['start'])
def game(message):
    state = "start"
    player.current_state = state
    show_content(states[state], message.chat.id)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def switch_state(message):
    state = states[player.current_state].get_next_state(message.text, player)
    player.current_state = state
    show_content(states[state], message.chat.id)

if __name__ == '__main__':
    bot.polling(none_stop=True)