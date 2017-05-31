class Player:
    surname = "Городецкий"
    name = "Антон"
    id = None
    friendship = False
    meeting = False
    is_male = True
    late = False
    state_content_showing_finished = False
    last_message_index = -1
    username = None
    en_language = True

    def __init__(self, id, username):
        self.id = id
        self.current_state_id = "language_select"
        self.username = username
