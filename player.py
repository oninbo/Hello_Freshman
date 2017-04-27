from states import states
from state import State
class Player:
    surname = None
    name = None
    current_state:State
    id = None

    def __init__(self,id):
        self.id = id
        self.current_state = states["I_a_00_00"]
