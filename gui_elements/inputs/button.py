# Created by Ricardo Quintela

from pygame import Rect, Surface
from .label import Label


class Button:
    def __init__(self, text: str, color: tuple, pos:tuple = (0,0), event = None,
                 textSize: int = 15, textColor:tuple = (255,255,255), index: int = 0, active: bool = True):
        """
        Constructor of the class Button\n
        A button is a window object that can be clicked with the mouse\n\n

        The object can be associated with a function so that when the user clicks, the function is called\n
        The event attribute can be used to store a function to later execute. The function can also
        be associated with the setEvent method\n\n

        To add args to the stored function a anonymous function can be used (lambda)

        Args:
            text: the text to show on the button
            color: the color of the button
            pos: the position of the button
            event: the function to associate with the button
            textColor: the color of the text of the button
            index: the index of the button
            active: whether the button is clickable or not
        """
        self.text = text
        self.color = color
        self.pos = pos
        self.event = event
        self.textSize = textSize
        self.textColor = textColor
        self.index = index
        self.active = active

        #store the size of the button based on the size of the label
        self.label = Label(text, textColor, textSize)
        self.size = (self.label.size[0] + 4, self.label.size[1] + 4)

        #create and draw the surface object
        self.surface = Surface(self.size)
        self.draw(color)

        self.hitbox = Rect(pos, self.size)

        self.clicked = False

    def setWidth(self, width: int):
        """
        Defines a new width for the button box\n

        Args:
            width: the new width of the button
        """
        self.size = (width, self.size[1])
        self.hitbox = Rect(self.pos, self.size)
        self.surface = Surface(self.size)
        self.draw(self.color)


    def setPos(self, pos: tuple):
        """
        Define the position of the button\n

        Args:
            pos: the new position og the button
        """
        self.pos = pos
        self.hitbox.topleft = pos


    def activate(self, textColor):
        """
        Activates the button\n

        Args:
            textColor: the color of the text
        """
        self.active = True
        self.label.setText(self.text, textColor)
        self.draw(self.color)


    def deactivate(self, textColor):
        """
        Deactivates the button\n

        Args:
            textColor: the color of the text
        """
        self.active = False
        self.label.setText(self.text, textColor)
        self.draw(self.color)


    def draw(self, color: tuple):
        """
        Draws the button in the given color\n

        Args:
            color: the color of the button
        """
        self.surface = Surface(self.size)
        self.surface.fill(color)
        self.label.blit(self.surface, (2, 2))

    def blit(self, canvas:Surface):
        """
        Draw the button on the given surface\n

        Args:
            canvas: the surface where the button will be drawn
        """
        canvas.blit(self.surface, self.pos)


    def getClick(self):
        """
        Access the clicked attribute of the button
        """
        if self.clicked:
            self.clicked = False
            return True
        return False


    def setEvent(self, event):
        """
        Define the event function\n

        Args:
            event: the event function
        """
        self.event = event


    def setText(self, text: str):
        """
        Set the text of the button\n

        Args:
            text: the new text to set on the button
        """
        self.text = text
        self.label.setText(text, self.textColor)
        self.size = (self.label.size[0] + 4, self.label.size[1] + 4)
        self.draw(self.color)


    def hoverColor(self):
        """
        Draws the button in brighter color\n
        """
        r,g,b = self.color
        r = r+40 if r+40 < 256 else 255
        g = g+40 if g+40 < 256 else 255
        b = b+40 if b+40 < 256 else 255
        self.draw((r,g,b))


    def isHovered(self, mousePos: tuple):
        """
        Know if the button is being hovered\n

        Args:
            mousePos: the position of the mouse

        Returns:
            True if is hovered; False otherwise
        """

        if self.hitbox.collidepoint(mousePos):
            return True
        return False


    def clickEvent(self, mousePos:tuple, click: bool):
        """
        Run the event attribute function with the given arguments\n
        Only works if it's active (clickable)\n

        Args:
            mousePos: the position of the mouse pointer
            click: the state of the wanted mouse button
        """

        #only goes to the other instructions if the button is active (clickable)
        if not self.active:
            return


        #if the button is clicked the event function is ran with the given arguments
        if self.isHovered(mousePos):
            #draws the button in a brighter color if it's hovered
            self.hoverColor()

            # skip the next condition if there is no event defined
            if click:
                self.clicked = True

                if self.event == None:
                    return

                #call the event function
                self.event()
        else:
            #draws the button in its natural color
            self.draw(self.color)
