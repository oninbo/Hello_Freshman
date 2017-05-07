from contentUnit import ContentUnit
import states

class State:
    content: ContentUnit = []
    buttons = {}
    next_state = None
    callback = None

    def __init__(self, content, next_state, buttons={}):
        self.content = content
        if buttons:
            self.buttons = buttons
        else:
            self.buttons = {"Дальше": next_state}
        self.next_state = next_state

    def get_next_state(self, message, player):

        if (message.text in self.buttons.keys()):
            next_state = self.buttons[message.text]
        else:
            next_state = None
        return next_state