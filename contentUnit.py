

class ContentUnit:
    type = ""
    value = ""
    delay = None

    def __init__(self, type, value, delay = 0):
        self.type = type
        self.value = value
        self.delay = delay
