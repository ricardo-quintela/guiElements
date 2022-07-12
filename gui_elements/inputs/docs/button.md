# The Button class
  
  
## Methods
  
  
### \_\_init\_\_  
  
**Signature:**  
  
>```__init__(self, text: str, color: tuple, pos:tuple = (0,0), event = None,                 textSize: int = 15, textColor:tuple = (255,255,255), index: int = 0, active: bool = True)```  
  
**Description:**  
  
>Constructor of the class Button  
>A button is a window object that can be clicked with the mouse  
>  
>The object can be associated with a function so that when the user clicks, the function is called  
>The event attribute can be used to store a function to later execute. The function can alsobe associated with the setEvent method  
>  
>To add args to the stored function a anonymous function can be used (lambda)  
  
**Arguments:**  
  
>```text```: the text to show on the button  
>```color```: the color of the button  
>```pos```: the position of the button  
>```event```: the function to associate with the button  
>```textColor```: the color of the text of the button  
>```index```: the index of the button  
>```active```: whether the button is clickable or not  
>  
  
  
### setWidth  
  
**Signature:**  
  
>```setWidth(self, width: int)```  
  
**Description:**  
  
>Defines a new width for the button box  
>  
  
**Arguments:**  
  
>```width```: the new width of the button  
>  
  
  
### setPos  
  
**Signature:**  
  
>```setPos(self, pos: tuple)```  
  
**Description:**  
  
>Define the position of the button  
>  
  
**Arguments:**  
  
>```pos```: the new position og the button  
>  
  
  
### activate  
  
**Signature:**  
  
>```activate(self, textColor)```  
  
**Description:**  
  
>Activates the button  
>  
  
**Arguments:**  
  
>```textColor```: the color of the text  
>  
  
  
### deactivate  
  
**Signature:**  
  
>```deactivate(self, textColor)```  
  
**Description:**  
  
>Deactivates the button  
>  
  
**Arguments:**  
  
>```textColor```: the color of the text  
>  
  
  
### draw  
  
**Signature:**  
  
>```draw(self, color: tuple)```  
  
**Description:**  
  
>Draws the button in the given color  
>  
  
**Arguments:**  
  
>```color```: the color of the button  
>  
  
  
### blit  
  
**Signature:**  
  
>```blit(self, canvas:Surface)```  
  
**Description:**  
  
>Draw the button on the given surface  
>  
  
**Arguments:**  
  
>```canvas```: the surface where the button will be drawn  
>  
  
  
### getClick  
  
**Signature:**  
  
>```getClick(self)```  
  
**Description:**  
  
>Access the clicked attribute of the button  
  
  
### setEvent  
  
**Signature:**  
  
>```setEvent(self, event)```  
  
**Description:**  
  
>Define the event function  
>  
  
**Arguments:**  
  
>```event```: the event function  
>  
  
  
### setText  
  
**Signature:**  
  
>```setText(self, text: str)```  
  
**Description:**  
  
>Set the text of the button  
>  
  
**Arguments:**  
  
>```text```: the new text to set on the button  
>  
  
  
### hoverColor  
  
**Signature:**  
  
>```hoverColor(self)```  
  
**Description:**  
  
>Draws the button in brighter color  
>  
  
  
### isHovered  
  
**Signature:**  
  
>```isHovered(self, mousePos: tuple)```  
  
**Description:**  
  
>Know if the button is being hovered  
>  
  
**Arguments:**  
  
>```mousePos```: the position of the mouse  
>  
  
**Returns:**  
  
>True if is hovered; False otherwise
  
  
  
### clickEvent  
  
**Signature:**  
  
>```clickEvent(self, mousePos:tuple, click: bool)```  
  
**Description:**  
  
>Run the event attribute function with the given arguments  
>Only works if it's active (clickable)  
>  
  
**Arguments:**  
  
>```mousePos```: the position of the mouse pointer  
>```click```: the state of the wanted mouse button  
>  
  
  
