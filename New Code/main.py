from Character import Character
from Battle import Battle
from appJar import gui

def press(button):
    if button == "Quit":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)

app = gui("Nottagochi","320x240")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

app.addButtons(["Login", "Quit"], press)
app.setFocus("Username")
app.go()
