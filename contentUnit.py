class ContentUnit:
    def __init__(self, type, value, delay=1):
        self.type = type
        self.value = value
        self.delay = delay
        if type == "photo": self.delay = 0
