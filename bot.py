import telebot
from player import Player
from states import states
import time
import config
from telebot import types
from contentUnit import ContentUnit
import db_manager

bot = telebot.TeleBot(config.token)

admins = ["Oninbo"]


@bot.message_handler(commands=['start'])
def start_game(message):
    player = Player(message.chat.id, message.chat.username)
    if message.chat.username:
        print("Player @" + message.chat.username + " with id:" + str(message.chat.id) + " started the game")
    else:
        print("Player with id:" + str(message.chat.id) + " started the game")
    show_content(player)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def reply(message):
    player_id = message.chat.id
    if not db_manager.check_player(player_id):
        bot.send_message(player_id, "Чтобы начать игру нажмите /start")
    else:
        player: Player = db_manager.get_player(player_id)
        current_state = states[player.current_state_id]
        if player.last_message_index == -1:
            success = change_state(player, message.text)
            print("id:" + str(player_id) + " state changed to " + player.current_state_id + ": " + str(success))
            if success:
                if current_state.callback:
                    current_state.callback(player, message)
                db_manager.save_player(player_id, player)
        show_content(player)


def replace_text(text, text_changes):
    for word in text_changes.keys():
        text = text.replace(word, text_changes[word])
    return text


contentFunctions = {"text": bot.send_message, "photo": bot.send_photo}


def show_content(player):  # username for debugging
    text_changes = {"#name": player.name}

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    current_state = states[player.current_state_id]
    buttons = current_state.buttons
    content: ContentUnit = current_state.content
    if player.is_male in content:
        content = content[player.is_male]
    if buttons:
        for key in buttons.keys():
            markup.add(key)

    for i in range(player.last_message_index + 1, len(content)):
        value = content[i].value
        value = replace_text(value, text_changes)
        content_function = contentFunctions[content[i].type]
        if content[i] is content[-1]:
            content_function(player.id, value, reply_markup=markup)
        elif content[i] is content[0]:
            content_function(player.id, value, reply_markup=types.ReplyKeyboardRemove())
        else:
            content_function(player.id, value)
        player.last_message_index = i
        db_manager.save_player(player.id, player)
        if player.username not in admins and content[i] is not content[-1]:
            time.sleep(content[i].delay)
    player.last_message_index = -1
    db_manager.save_player(player.id, player)


def knock_user(player):
    if player.last_message_index != -1:
        show_content(player)

db_manager.go_through(knock_user)


def change_state(player, text):
    new_state = states[player.current_state_id].next_state(text)
    if new_state:
        player.current_state_id = new_state
        return True
    else:
        return False





if __name__ == '__main__':
    bot.polling(none_stop=True)
