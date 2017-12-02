from appJar import gui

win = gui("Welcome")
win.setGeom("320x240")
#win.setGeometry("fullscreen")



def main(name):
    app = gui("Nottagochi")

    app.setGeom("320x240")
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(20)


    #Tools
    tools = ["Pet", "Stats", "New"]
    app.addToolbar(tools, toolbarq, findIcon=False)
    


    def pressg(namegb):
        win.stop()
        app.stop()

    #Caleb's goddamned meters
    healthValue = 100
    happyValue = 100
    hungerValue = 0
    app.setSticky("e")
    app.addMeter("Health")
    app.addMeter("Happiness")
    app.addMeter("Hunger")
    app.setMeterFill("Health", "Red")
    app.setMeterFill("Happiness", "Yellow")
    app.setMeterFill("Hunger", "DarkViolet")
    app.setMeter("Health", healthValue, text="Health")
    app.setMeter("Happiness", happyValue, text="Happiness")
    app.setMeter("Hunger", hungerValue, text="Hunger")

    #Bottom buttons
    app.setSticky("se")
    app.addButtons(["Feed", "Play", "Fight", "Quit"], pressg)

    
    
    app.go()


def quitg(name):
    win.stop()



def toolbarq(namet):
    if namet == "New":
        print("This would be how it'd be reset.")
    elif namet == "Stats":
        print("Stats.")
    elif namet == "Pet":
        print("Pet")

        



win.setBgImage("bulb_on.png")

win.setSticky("s")
win.addButtons(["Play", "Quit"], [main, quitg])


win.go()
