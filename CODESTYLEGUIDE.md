# Code style guide

The code style for this project is pretty minimal due to the fact that most of the rules for writing classes is enforced by python

## Defining classes
Defining classes is pretty simple in python:

~~~
//Note that class names should be uppercase
class CLASS_NAME:


//Examples of proper class names
class Game:
class Character:

~~~

**NOTE:**
Classes should all be defined in SEPERATE FILES meaning for every class, there should be a corresponding file called *class.py*

## Private Variables
While python enforces private on all variables (for the most part), when defining them in a class, use this notation:
~~~
def Character:

    //Private variables
    _health = 0
    _armour = 40

~~~
The notation being Camel Case with the first word being lower case **AND** with and underscore before the name

## Notes
This code style should be upheld and any errors in the style will result in a very angry message
