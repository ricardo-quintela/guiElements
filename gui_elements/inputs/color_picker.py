# Created by Ricardo Quintela

from pygame import Surface, Rect, draw
from .button import Button

class ColorPicker:
    def __init__(self, color: tuple, pos: tuple = (0,0)):
        """
        The constructor of the class ColorPicker\n

        Args:
            color: the color of the background of the color picker
            pos: the position of the color picker
        """
        # default attributes
        self.color = color
        self.pos = pos

        #new attributes
        self.size = (404, 60)
        self.surface = Surface(self.size)
        self.hitbox = Rect(self.pos[0] + 10, self.pos[1] + 5, 384, 20)

        self.canvas = Surface((384,20))
        self.drawCanvas()

        r,g,b = color
        r = r+40 if r+40 < 256 else 255
        g = g+40 if g+40 < 256 else 255
        b = b+40 if b+40 < 256 else 255

        #select color button
        self.select = Button("Select", (r,g,b))
        self.select.setPos((404/2 - self.select.size[0] / 2, 30))

        self.draw()

        self.selectedColor = (0,0,0)

    def setPos(self, pos: tuple):
        """
        Define the position of the color picker\n

        Args:
            pos: the new position
        """
        self.pos = pos
        # update the color picker box hitbox position
        self.hitbox.topleft = self.pos[0] + 10, self.pos[1] + 5


    def checkHitbox(self, mousePos: tuple, mouseClick: bool):
        """
        Set the selected color with a mouse input
        Args:
            mousePos: the position of the mouse on screen
            mouseClick: whether the mouse is clicked or not
        """

        #calculate relative mouse position
        if self.hitbox.collidepoint(mousePos) and mouseClick:
            self.surface.blit(self.canvas, (10,5))

            #calculate relative positions
            pointerPoint = int(mousePos[0] - self.pos[0]), int(mousePos[1] - self.pos[1])
            colorPos = pointerPoint[0] - 10, pointerPoint[1] - 5

            #get the color from the canvas at the mouse position
            color = self.canvas.get_at(colorPos)
            self.selectedColor = (color.r, color.g, color.b)

            #draw an indicator where the color was selected
            draw.line(self.surface, (0,0,0), (pointerPoint[0], 5), (pointerPoint[0], 25))




    def getColor(self) -> tuple:
        """
        Select the color\n

        Returns:
            the color
        """
        self.surface.blit(self.canvas, (10,5))
        return self.selectedColor


    def drawCanvas(self):
        """
        Draw all the colors in the canvas\n
        """
        # retorna a cor para fazer um gradiente
        l = (1, 0, 2, 1, 0, 2, 3)

        color = [255, 0, 0]

        index = 0

        for i in range(384):
            if l[index] != 3:
                color[l[index]] += 3 * ((-1) ** index)
                draw.line(self.canvas, color, (i, 0), (i, 20))
                i += 1

                if color[l[index]] == 255 or color[l[index]] == 0:
                    index += 1 if index < len(l) - 1 else 0


    def draw(self):
        """
        Draw a rainbow like area for picking colors\n
        """
        self.surface.fill(self.color)

        self.surface.blit(self.canvas, (10,5))


    def blit(self, canvas: Surface, mousePos: tuple, click: bool):
        """
        Draw the color picker on the giver surface\n

        Args:
            canvas: the surface to draw the color picker in
            mousePos: the position of the mouse on screen
            click: if the mouse is being clicked or not
        """
        #draw the button on the surface
        self.select.blit(self.surface)

        #calculate the relative mouse position
        mousePosition = (mousePos[0] - self.pos[0], mousePos[1] - self.pos[1])

        #chack if the button is being clicked
        self.select.clickEvent(mousePosition, click)

        self.checkHitbox(mousePos, click)

        canvas.blit(self.surface, (self.pos))
