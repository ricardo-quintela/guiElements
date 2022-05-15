# Created by Ricardo Quintela

from pygame import Surface
from .button import Button

class DropDownMenu:
    def __init__(self, options: list):
        """
        Constructor of the class FastMenu\n

        Args:
            options: the buttons of the menu
        """
        self.options = options

        self.dimensions = (0,0)

        self.pos = (0,0)

        self.isActive = True


        self.setDimensions()

        #create the surface
        self.surface = Surface(self.dimensions)

        #draw the buttons in the surface
        self.draw()


    def setDimensions(self):
        """
        Changes the dimensions of the text input and its buttons
        """
        w, h = 0, 0
        Y = 0
        # change the positions of the buttons and define the dimensions of the menu
        for button in self.options:
            button.setPos((0, Y))
            Y += button.size[1]
            if button.size[0] > w:
                w = button.size[0]
            h += button.size[1]
        self.dimensions = (w, h)

        # set the width of all the buttons to the size of the menu
        for button in self.options:
            button.setWidth(self.dimensions[0])

        self.surface = Surface(self.dimensions)


    def draw(self):
        """
        Draw all the buttons in the surface\n
        """
        #iterate through the buttons array and draw them on the surface in order
        for button in self.options:
            button.blit(self.surface)


    def activate(self, pos: tuple):
        """Activates the menu

        Parameters
        ----------
        pos : tuple
            the new position of the fast menu
        """
        self.isActive = True
        self.pos = pos


    def deactivate(self):
        """Deactivates the menu
        """
        self.isActive = False


    def getClick(self, index: int):
        """
        Access the click attribute of a button on the menu\n

        Args:
            index: the index of the button of the menu
        """
        return self.options[index].getClick()


    def blit(self, canvas: Surface):
        """
        Draws the surface on the given canvas\n
        Updates the menu pos attribute\n

        Args:
            canvas: the surface on which to draw the menu
        """
        if not self.isActive:
            return

        canvas.blit(self.surface, self.pos)


    def addOption(self, option: Button):
        """
        Adds an option to the menu\n

        Args:
            option: the option to be added
        """

        self.options.append(option)

        self.setDimensions()


    def removeOption(self, index: int):
        """
        Removes an option on the given index\n

        Args:
            index: the index of the option to be removed
        """

        self.options.pop(index)

        self.setDimensions()



    def clickEvent(self, mousePos: tuple, click: bool):
        """
        Runs all the buttons and draws them on the surface\n

        Args:
            mousePos: the position of the canvas where to draw the menu
            click: the button of the mouse that was clicked
        """

        if not self.isActive:
            return

        #itereate through the buttons array and check for hover and clicks in each one
        mousePosition = (mousePos[0] - self.pos[0], mousePos[1] - self.pos[1])

        for button in self.options:
            button.clickEvent(mousePosition, click)

        #redraw the buttons in the surface
        self.draw()
