from contentUnit import ContentUnit
import states

class State:
    content: ContentUnit = []
    buttons = {}
    default_children = None
    callback = None

    def __init__(self, content, buttons, default_children, callback = None):
        self.content = content
        self.buttons = buttons
        self.default_children = default_children
        self.callback = callback

