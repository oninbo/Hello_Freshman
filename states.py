from state import State

states = {}


def sign_in(text, player):
    player.name = text
    return "rest or friend"


def make_friends(text, player):
    player.is_Vanya_met = True

start = State("start", states)
start.set_next_state("kombinat")

kombinat = State("kombinat", states)
kombinat.set_next_state("first choice")

first_choice = State("first choice", states)
first_choice.choices = {
    "выпить воды":"drink",
    "оглянутся кругом":"look around"
}

drink = State("drink", states)
drink.set_next_state("sign in")

look_around = State("look around", states)
look_around.set_next_state("sign in")

name_check = State("sign in", states)
name_check.do_something = sign_in

rest_or_friend = State("rest or friend", states)
rest_or_friend.choices = {
    "Передохнуть под тенью дерева":"rest",
    "Познакомиться с кем-нибудь":"make friends"
}

rest = State("rest", states)

friend = State("make friends", states)
friend.do_something = make_friends

