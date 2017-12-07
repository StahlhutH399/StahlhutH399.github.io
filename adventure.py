#Destiny

import time

def greeting():
    print("You wake you in the middle of a junkyard filled with broken cars and destroyed junk, broken buildings, snowy soil, and a sense of danger all around you.")
    input("(Press Enter To Continue)")
    print("Unknown: " + "Guardian! Thank the Traveler I found you!")
    input("")
    print("You: What the hell is going on?")
    input("")
    print("You get your bearings on what the hell is going on and notice a robotic, floating, shell in front of you.")
    input("")
    print("Unknown: ")
    response=("")
    return response

def second_choice():
    print("Great....")
    response=input("do you open it? (yes/no)")
    return response

def haters():    #exits the game
    print("Lame, bye then!")

def opened():
    print("Great!")
    #enter your code here
def not_opened():
    print("you live!")
                        #Enter your code here

x = greeting()

if x=="yes":
    y = second_choice()
    if y=="yes":
        opened()
    elif y=="maybe":
        print("why maybe bitch?")    
    else:
            not_opened()

else:
    haters()
        
