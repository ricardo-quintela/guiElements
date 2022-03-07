# Created by Ricardo Quintela

from pygame import event, mouse, QUIT, VIDEORESIZE, MOUSEBUTTONDOWN, MOUSEBUTTONUP, KEYDOWN, K_RETURN, K_BACKSPACE

class WindowEvent:
    def __init__(self):
        """
        Constructor of the class WindowEvent\n
        An object of this type can be used to analyze some events in a pygame window\n
        """
        self.events = {}

        self.resetEvents()

    def resetEvents(self):
        """
        Sets all the events to their base state
        """
        self.events = {"windowState": True,
                       "windowResize": False,
                       "windowSize": (0,0),
                       "mouseButtons": [False, False, False, False, False, False],
                       "mouseUp": [False, False, False, False, False, False],
                       "mousePos": mouse.get_pos(),
                       "mouseClicking": mouse.get_pressed(),
                       "keyText": "",
                       "keyRETURN": False,
                       "keyBACKSPACE": False
                       }

    def getEvent(self, event: str):
        """
        Access the attribute events\n

        Returns:
            the events attribute
        """

        return self.events[event]


    def eventsCheck(self):
        """
        Checks for each event there is on the display\n

        Returns:
            a tuple object with all the values of the checked events
        """

        # resets all the events and gets the mouse position on the window
        self.resetEvents()

        # iterates through all the pygame events
        for e in event.get():
            # quit the window
            if e.type == QUIT:
                print("QUIT EVENT")
                self.events["windowState"] = False

            #if the window gets resized
            if e.type == VIDEORESIZE:
                self.events["windowResize"] = True
                self.events["windowSize"] = (e.w, e.h)

            # check for mouse clicks
            if e.type == MOUSEBUTTONDOWN:
                self.events["mouseButtons"][e.button] = True

            # check for mouse clicks
            if e.type == MOUSEBUTTONUP:
                self.events["mouseUp"][e.button] = True

            # check for key input (write text)
            if e.type == KEYDOWN:
                self.events["keyText"] = e.unicode

                # return (ENTER) key event
                if e.key == K_RETURN:
                    self.events["keyRETURN"] = True
                # backspace key event
                if e.key == K_BACKSPACE:
                    self.events["keyBACKSPACE"] = True
