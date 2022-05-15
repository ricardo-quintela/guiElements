# guiElements

## Make pygame apps with custom inputs easier

This module provides useful inputs for pygame interfaces such as apps or games.  

The window package can be used to create and manage a window with ease.  

The inputs package can be used to create graphical inputs on the window  

# Inputs package

* Button - A standart button input that can be associated with a function/method to execute instructions  
* "Fast Menu" - Right click menu that can contain a list of buttons  
* Text input - A text box that the user can write on  
* Color Picker - A color selector with a small variety of colors to pick  
* Label - A place to display text  
(all these inputs have ways to change their behaviour during code execution)

# Window package

To create a working window, the user need to create an instance of the ```Window``` class. To controll its events one must instance the ```WindowEvent``` class.  
The user may then use the ```eventsCheck``` method to check for window events.  
After all this is set, the window must be updated to keep showing frames. This can be done by using the ```update``` method.  
Pygame module must be initiated by using the ```init``` method.

Example:  
```
pygame.init()

# create Window and WindowEvent instances
root = Window((800,600), 60, "My first window")
events = WindowEvent()

# mainloop
while events.getEvent("windowState"):
    
    # check for events
    events.eventsCheck()

    # tick the window
    root.tick()

    # fill the canvas with white
    root.fill("white")

    # update the window
    root.update()

pygame.quit()

```

## Checking for window events

In the ```WindowEvent``` class the ```eventsCheck``` method can get the state of some of the most important window events in pygame.  
By using the ```getEvent``` method, one can get a specific event at a time.  

Available events and their meaning:

Event         | Meaning
--------------|----------------------------------------------------------
windowState   | Whether the window is running or a user asked to close it
windowResize  | Stands for a window resize request by the user
windowSize    | The current window size
mouseButtons  | A list with all the values from the clicked mouse buttons
mouseUp       | A list with all the values from the released mouse buttons
mousePos      | The current position of the mouse pointer
mouseClicking | A list that contains the current state of all mouse buttons
keyText       | A decoded string of all the text keys being pressed currently
keyRETURN     | The current value on the RETURN key
keyBACKSPACE  | The current value on the BACKSPACE key