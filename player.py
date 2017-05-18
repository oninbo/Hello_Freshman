class Player:
    surname = "Городецкий"
    name = "Антон"
    id = None
    friendship = False
    meeting = False
    is_male = True

    def __init__(self, id):
        self.id = id
        self.current_state_id = "sex_select"
