from states import states
from state import State


class Player:
    surname = "Городецкий"
    name = "Антон"
    current_state: State
    id = None
    friendship = False
    meeting = False

    def __init__(self, id):
        self.id = id
        self.current_state = states["I_a_00_00"]