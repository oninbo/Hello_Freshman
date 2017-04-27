from contentUnit import ContentUnit
from typing import *

class State:
    content: ContentUnit = None
    children = []
    default_children = None

    def __init__(self, content, children, default_children):
        self.content = content
        self.children = children
        self.default_children = default_children
