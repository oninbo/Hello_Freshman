from player import Player


def set_meeting(player, message):
    player.meeting = True


def set_late(player, message):
    player.late = True


def check_late(player, message):
    if player.late is True:
        player.current_state_id = "I_c_04_01_end"


def check_meeting(player, message):
    if player.meeting is True:
        player.current_state_id = "II_a_06_00"
    else:
        player.current_state_id = "II_a_06_01"


def restart_button(player, message):
    player = Player(player.id)


def check_friendship(player, message):
    if player.friendship:
        player.current_state_id = "I_c_01_00"
    else:
        player.current_state_id = "I_c_01_01"


def set_name(player, message):
    player.name = message.text
    player.friendship = True
    print(str(player.id) + " name: " + player.name)


def set_surname(player, message):
    player.surname = message.text
    print(str(player.id) + " surname: " + player.surname)


def set_sex(player, message):
    if message.text == "Женский": player.is_male = False


def check_sex(player, message):
    if not player.is_male:
        player.current_state_id = "II_a_00_00_female"


def end(player, message):
    print(player.name + " " + player.surname + " finished the game")