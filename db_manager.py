import shelve

db_directory = "db/"


def save_player(key, player):
    key = str(key)
    with shelve.open(db_directory + "players") as players:
        players[key] = player
    players.close()


def get_player(key):
    key = str(key)
    with shelve.open(db_directory + "players") as players:
        player = players[key]
    players.close()
    return player


def check_player(key):
    key = str(key)
    with shelve.open(db_directory + "players") as players:
        presence = key in players
    players.close()
    return presence

