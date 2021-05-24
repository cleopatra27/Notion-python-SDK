from colors import Colors


class Annotations:
    def __init__(self, bold, italic, strikethrough, underline, code, colors):
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline
        self.code = code
        self.colors = Colors