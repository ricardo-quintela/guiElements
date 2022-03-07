# Created by Ricardo Quintela

from pygame import font, Surface

class Label:
    def __init__(self, text: str, color: tuple, fontSize: int, bold: bool = False, italic: bool = False) -> None:
        """
        Constructor of the class Label\n

        Args:
            text: the text that will show up on the label
            color: the color of the text on the label
            fontSize: the size of the text of the label
            bold: whether the text is in bold or not
            italic: whether the text is in italic or not
        """
        self.text = text
        self.color = color
        self.fontSize = fontSize


        self.setText(text, self.color)

        self.size = (self.surface.get_width(), self.surface.get_height())

    def setText(self, text: str, textColor: tuple):
        """
        Sets the label text to a new text
        Args:
            text: the new text of the label
        """
        self.text = text if len(text) != 0 else "     " #label gets some space even is the text is inexistent
        self.surface = font.SysFont("Arial Black", self.fontSize).render("%s" % (text), False, textColor, self.fontSize)
        self.size = self.surface.get_size()

    def blit(self, canvas: Surface, pos: tuple):
        """
        Draws the label on a given surface
        Args:
            canvas: the surface to draw the label in
            pos: the position to draw the label in
        """
        canvas.blit(self.surface, pos)
