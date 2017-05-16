class Player:
    surname = "Городецкий"
    name = "Антон"
    id = None
    friendship = False
    meeting = False

    def __init__(self, id):
        self.id = id
        self.current_state_id = "I_a_00_00"
