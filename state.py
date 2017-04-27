from contentUnit import ContentUnit
import states

class State:
    content: ContentUnit = []
    buttons = {}
    default_children = None
    callback = None

    def __init__(self, content, buttons, default_children):
        self.content = content
        self.buttons = buttons
        self.default_children = default_children

    def get_next_state(self,message, player):

        # for foo in current_state.content.callback:
        #   foo(bot, player)

        if (message.text in self.buttons.keys()):
            next_state = self.buttons[message.text]
        else:
            next_state = self.default_children
        return next_state