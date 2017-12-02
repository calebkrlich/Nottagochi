from appJar import gui
import RPi.GPIO as GPIO
import random
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(15, GPIO.IN)


global buttonPressed
buttonPressed = False

try:
    app = gui("Nottagochi")
    app.setGeometry("fullscreen")
    app.setResizable(False)
    app.hideTitleBar()
    app.setGeom("320x240")
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(12)

 

    app.showSplash("Nottagochi", fill="DarkSlateBlue", stripe="LightCyan", fg="black", font=20)

    #app.infoBox("Welcome to Nottagochi!", "Take care of your very own Octocat!")


    def toolbarq(namet):
        if namet == "New":
            print("This would be how it'd be reset.")
        elif namet == "Stats":
            print("Stats.")
        elif namet == "Pet":
            print("Pet")

    def pressg(namegb):
        global healthValue
        global hungerValue
        global happyValue

        print("Preforming the " + namegb + " action!")

        lowHealth = False
        lowHappy = False
        lowHungry = False
        
        if namegb == "Quit":
            app.stop()
            
        elif namegb == "Feed":
            healthValue += 5
            app.setMeter("Health", healthValue, text="Health")
            app.reloadImage("octokitty", "Eatingtest.gif")
            hungerValue -= 10
            app.setMeter("Hunger", hungerValue, text="Hunger")
            if hungerValue == 0:
                print('This is where a box went.')
                #app.warningBox("Warning!", "Do not overfeed your octocat!")
            elif hungerValue <= 0:
                healthValue -= 10
                app.setMeter("Health", healthValue, text="Health")
                if healthValue == 0:
                    app.reloadImage("octokitty", "deathnoloop.gif")
                    #app.infoBox("Dieded.", "You have killed your octocat. Apologize to github.")
                    
                    app.stop()
                

            
        elif namegb == "Play":
            
            happyValue += 10

            app.setMeter("Happiness", happyValue, text="Happiness")
            app.reloadImage("octokitty", "rollover.gif")
            if happyValue == 100:
                print('This is yet another comment box.')
                #app.infoBox("Happy", "There is no limit to happiness.")
            elif happyValue == 200:
                print('These wouldve been really funny.')
                #app.warningBox("Stop", "You are reaching near-lethal levels of happiness.")
            elif happyValue == 300:
                app.reloadImage("octokitty", "deathnoloop.gif")
                #app.errorBox("Oh NO!", "Octocat has literally exploded with joy. Apparently there is a limit to happiness.")
                app.stop()
            
        elif namegb == "Fight":
            app.reloadImage("octokitty", "fight.gif")
            healthValue -= 5
            hungerValue += 10
            happyValue -= random.randint(2,10)
            app.setMeter("Health", healthValue, text="Health")
            app.setMeter("Happiness", happyValue, text="Happiness")
            app.setMeter("Hunger", hungerValue, text="Hunger")
            if (healthValue <= 40 and lowHealth == False and healthValue > 0):
                #app.warningBox("Warning", "Your Octocat is seriously injured.")
                lowHealth = True
            elif healthValue <= 0:
                app.reloadImage("octokitty", "deathnoloop.gif")
                #app.infoBox("Dieded.", "Your octocat has dieded. You bastard.")
                app.stop()
            elif (happyValue <= 20 and lowHappy == False and happyValue > 0):
                #app.warningBox("Depressed", "Your octocat is getting depressed.")
                lowHappy = True
            elif happyValue <= 0:
                app.reloadImage("octokitty", "deathnoloop.gif")
                #app.infoBox("Suicide", "Octocat commits seppuku.")
                app.stop()
            elif (hungerValue == 80 and lowHungry == False and hungerValue < 100):
                #app.warningBox("Hunrgy", "Octocat is hungry.")
                lowHungry = True
            elif hungerValue >= 140:
                app.reloadImage("octokitty", "deathnoloop.gif")
                #app.infoBox("Dieded", "Octocat has starved to death.")
                app.stop()

    def listener():
        if(GPIO.input(11) != 0):
            pressg("Feed")
            time.sleep(.5)
            
        if(GPIO.input(13) != 0):
            pressg("Quit")
            time.sleep(.5)
            
        if(GPIO.input(15) != 0):
            pressg("Play")
            time.sleep(.5)
            
        if(GPIO.input(16) != 0):
            pressg("Fight")
            time.sleep(.5)
                


            
            
            
        
        
            
    '''#Tools
    tools = ["Pet", "Stats", "New"]
    app.addToolbar(tools, toolbarq, findIcon=False)'''
    app.setPadding([1,1])
    app.setSticky("")
    app.addImage("octokitty", "octocatysu2.gif")

    elapsed = 0
    #Caleb's goddamned meters
    healthValue = 100
    happyValue = 50
    hungerValue = 50

    app.addMeter("Health")
    app.addMeter("Happiness")
    app.addMeter("Hunger")

    app.setMeterFill("Health", "Red")
    app.setMeterFill("Happiness", "Yellow")
    app.setMeterFill("Hunger", "Violet")
    app.setMeter("Health", healthValue, text="Health")
    app.setMeter("Happiness", happyValue, text="Happiness")
    app.setMeter("Hunger", hungerValue, text="Hunger")

    app.addButtons(["Feed", "Play", "Fight", "Quit"], pressg)

    app.setBgImage("YSU.gif")

    #Creates a registered event that is called once every .5 secs
    app.registerEvent(listener)
    app.setPollTime(1)
    
    app.go()

finally:
    GPIO.cleanup()
