from content import content


class State:
    content = []
    choices = {}
    do_something = None

    def set_next_state(self, next_state):
        self.choices = {"Дальше":next_state}

    def __init__(self, name, dictionary):
        self.content = content[name]
        dictionary[name] = self

    def get_next_state(self, text, player_id):
        if self.do_something is not None:
            result = self.do_something(text, player_id)
            if result is not None:
                return result
        if text in self.choices:
            return self.choices[text]