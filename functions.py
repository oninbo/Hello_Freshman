from player import Player

def set_meeting(player, message):
    player.meeting = True


def check_meeting(player, message):
    if player.meeting is True:
        player.current_state = "II_a_06_00"
    else:
        player.current_state = "II_a_06_01"


def restart_button(player, message):
    player = Player(player.id)


def check_friendship(player, message):
    if (player.friendship):
        player.current_state = "I_c_01_00"
    else:
        player.current_state = "I_c_01_01"


def set_name(player, message):
    player.name = message.text
    #player.current_state.content[0] = ContentUnit("text", player.name + ", - сообщил ты, смеясь над шуткой.", delay=0)
    player.friendship = True
    print(str(player.id) + " name: " + player.name)


def set_surname(player, message):
    player.surname = message.text
    print(str(player.id) + " surname: " + player.surname)


def set_sex(player, message):
    if message.text == "женский": player.is_male = False
