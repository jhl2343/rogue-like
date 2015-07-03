import libtcodpy as libtcod
class Object:
    # If it is able to be represented as a character on the screen, then it is an object
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, console):
        # Set the color and then draw the character that represents this object at its position
        libtcod.console_set_default_foreground(console, self.color)
        libtcod.console_put_char(console, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self, console):
        # Srase the character that represents this object
        libtcod.console_put_char(console, self.x, self.y, ' ', libtcod.BKGND_NONE)

