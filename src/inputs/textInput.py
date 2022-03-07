# Created by Ricardo Quintela

from pygame import Rect, Surface, time, draw
from guiElements.inputs.label import Label

class TextInput:
    def __init__(self, pos: tuple, color: tuple, name:str = "", textColor: tuple = (255,255,255)):
        """
        Constructor of the class TextInput\n

        Args:
            pos: the position of the input on the screen
            color: the color of the input box
            textColor: the color of the written text
        """
        self.pos = pos
        self.color = color
        self.textColor = textColor
        self.name = name

        #in case the user wants to distinguish
        self.index = 0


        self.text = ""

        self.label = Label(self.text, textColor, 15)

        #start label
        r,g,b = textColor
        r = r - 50 if r - 50 > 0 else 0
        g = g - 50 if g - 50 > 0 else 0
        b = b - 50 if b - 50 > 0 else 0
        self.startColor = r,g,b
        self.startLabel = Label(name, self.startColor, 15)

        self.surface = Surface(self.label.size)

        self.size = self.surface.get_size()


        #the time since last time update
        self.lastTime = 0


    def setIndex(self, index: int):
        """
        Define the index attribute\n

        Args:
            index: the new index
        """
        self.index = index


    def setPos(self, pos):
        """
        Define the position of the text input box\n

        Args:
            pos: the new position of the text input box
        """
        self.pos = pos


    def setText(self, text: str):
        """
        Sets the active text in the text input\n

        Args:
            text: the text to show in the textInput
        """
        self.text = text
        self.label.setText(text, self.textColor)


    def setName(self, name: str):
        """
        Sets a new name for the Text input box\n

        Args:
            name: the new name of the text input box
        """
        self.name = name
        self.startLabel.setText(name, self.startColor)


    def reset(self):
        """
        Resets the text attribute
        """
        self.text = ""


    def addChar(self, char: str, backspace: bool):
        """
        Adds text to the label\n

        Args:
            char: the character or string to add to the text
            backspace: whether backspace is pressed or not
        """
        self.text += char

        if backspace:
            self.text = self.text[:-2]

        self.label.setText(self.text, self.textColor)

        self.draw()


    def draw(self):
        """
        Draws the label in a surface
        """

        label = self.startLabel if len(self.text) == 0 else self.label

        self.size = (label.size[0] + 8, label.size[1] + 6)

        self.surface = Surface(self.size)
        self.surface.fill(self.color)
        label.blit(self.surface, (4,3))


    def clearText(self):
        """
        Clears the text in the text input
        """
        self.text = ""


    def getText(self) -> str:
        """
        Access the text in the label\n

        Returns:
            the text is its length is > than 0, None otherwise
        """
        return self.text if len(self.text) != 0 else None


    def blit(self, canvas: Surface):
        """
        Draw the label on the given surface
        Args:
            canvas: the surface where the label with be drawn
        """

        now = time.get_ticks()

        #redraw the label
        self.draw()

        #text cursor effect
        if now - self.lastTime > 500:
            draw.line(self.surface, (255,255,255), (self.size[0] - 3, 2), (self.size[0] - 3, self.size[1] - 2), 2)
        if now - self.lastTime > 1000:
            self.lastTime = now

        canvas.blit(self.surface, self.pos)
