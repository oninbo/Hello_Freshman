from typing import List, ByteString


class ContentUnit:
    text = []
    photos = []
    keys = []
    callback = []

    def __init__(self, text, photos, keys, callback):
        self.text = text
        self.photos = photos
        self.keys = keys
        self.callback = callback
