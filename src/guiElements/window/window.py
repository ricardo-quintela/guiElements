# Created by Ricardo Quintela

from pygame import display, time, RESIZABLE, Surface

class Window:
    def __init__(self,size: tuple, fps: int, title: str = "App") -> None:
        """
        The constructor of the class Window
        Args:
            size: the dimensions of the canvas to be created as an attribute
            fps: the tick rate on which iteration is going to be ran
        """
        self.size = size
        self.FPS = fps
        self.title = title

        self.clock = time.Clock()

        info = display.Info()
        self.screenSize = (info.current_w, info.current_h)

        self.isFullscreen = False

        self.canvas = display.set_mode(size, RESIZABLE)
        display.set_caption(title)


    def resize(self, size: tuple):
        """
        Resizes the window\n

        Args:
            size: the new size of the window
        """
        self.canvas = display.set_mode(size, RESIZABLE)
        self.size = size


    def setTitle(self, title: str):
        """
        Defines a new title for the window\n

        Args:
            title: thge new title for the window
        """
        self.title = title
        display.set_caption(title)


    def blit(self, surface: Surface, pos:tuple):
        """Draws the surface on the canvas

        Parameters
        ----------
        surface : Surface
            the surface to draw on the canvas
        pos : tuple
            the position where to draw the surface
        """
        self.canvas.blit(surface, pos)


    def tick(self) -> None:
        """
        Adjusts the tick rate of the mainloop
        """
        self.clock.tick(self.FPS)

    def update(self) -> None:
        """
        Updates the display
        """
        display.update()

    def fill(self, color: tuple) -> None:
        """
        Fills the canvas with the given color argument
        Args:
            color: the RGB type color
        """
        self.canvas.fill(color)
