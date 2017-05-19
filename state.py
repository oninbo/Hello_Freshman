from contentUnit import ContentUnit


class State:
    content: ContentUnit = []
    buttons = {}
    default_children = None
    callback = None

    def __init__(self, content, buttons, default_children=None, callback=None):
        self.content = content
        self.buttons = buttons
        self.default_children = default_children
        self.callback = callback

    def next_state(self, text):
        if self.buttons and text in self.buttons:
            return self.buttons[text]
        elif self.default_children:
            return self.default_children
        else:
            return None
