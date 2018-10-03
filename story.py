import sys
from time import sleep


words = "This story is based off the choices you make, you can choose the choices by inputing the correlating number next to the choice you want. Good luck..."
for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
sleep(1)
            
def Entrance():
    words = '''
    You stand at the entrance of a dark and dreary mansion after your friends have challenged you to go in...
    As you and your friends enter, you clip your shoelaces on a piece of wood. 
    You bend down to tie your shoes but as you look up, your friends have vanished. 
    Shaking with fear, you enter the front door of the mansion. You enter a dark room with two doors.
    '''
    for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
            
def choosePath():
        words = '''
        Do you want to enter the left door or the right door?
        #1 left door...
        #2 right door...
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
   
        x = input()
        return x
  

def leftDoor(x):
    if x == 1:
        words='''
        As you enter the dark and chilling room, the hairs on the back of your neck rise and you sense a faint light in the distance. 
        You get closer to see what it is but it imediately disappears...
        What do you want to do?
        #1 Do you go to towards the vanished light...
        #2 Leave house immediately...
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        y = input()
        return y
    
def rightDoor(x):
    if x == 2:
        words = '''
        You walk towards the right door and open it. 
        You see your friends arguing about something. 
        They are arguing whether or not to split or stay together. 
        They ask you for advice, so which will you choose?
        #1 Split and go left
        #2 Stay Together and go right
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        z = input()
        return z
    
def light(y):
    if y == 1:
        words = '''
        You go towards the light that you saw was there a second ago. 
        Once you get there, you notice a doorknob along the dark wall and pull it. 
        You then enter a room filled with lots of treasure, illuminated by the amount of light reflected off the jewels and coins! 
        You take as much as you can but its too much, you need the help of your friends to get all the remaining jewels but part of 
        you feels like it is enough and just leave before something bad happens too you...
        Which will you choose?
        #1 Get your friends?
        #2 Leave the house immediately...
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        a = input()
        return a
    

def leave(y):
    if y == 2:
        words = '''
        You run out of the house frantically and pause for a moment to catch your breath. 
        As you start to run again, you see a shadow behind but you don't wait to be seen. 
        You immediately hide in nearby bushes that surround the house. 
        You see a dark figure about the size of a giant, but you look closer and notice a... garden gnome? 
        You can't believe it and you gotta go tell the others, but then you have some urge to forget about it and leave. 
        Which will you choose?")
        #1 Leave the house
        #2 Go after your friends
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        b = input()
        return b


def apart(z):
    if z == 1:
        words = '''
        You slowly walk into the left door but pause as you hear screams from the door your friends went through
        You keep walking not wanting to know what happened to them and find yourself wandering to the backyard of the house. 
        You look around to find many dead bodies including... your friends. You instinctively run and escape the area, driving 
        away as you see on the rear view mirror a mysterious figure standing and staring at the car as it disappears into the fog.
        YoU hAvE tHiS iRrAdIaTeD fEeLiNg To Go BaCk AnD sEe ThE hAuNtEd HoUsE aGaIn
        #1 Go back to the house
        #2 Go back to the house
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        c = input()
        return c
        
        
def together(z):
    if z == 2:
        words = '''
        You manage to convince your friends to stick together and choose which room to go through. 
        You tell you friends to go through the left door but they would rather go through the right door, 
        you lose to the majority vote and you all go through the right door.
        As you enter the right door, you feel like something is off
        #1 tell your friends that something is wrong
        #2 keep it to yourself and see what happens
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        d = input()
        return d
        
        
def getFriends(a):
    if a == 1:
        words = "As you run back to tell your friends what you discovered, the floor starts shifting under you, and it gives way to a dark and bottomless pit"
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        quit()    
        
def goHome(a):
    if a == 2:
        words = "You have safely exited the house, survived and brought back treasure. You live to see the light of day again."
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        quit()   
        
        
def leaveHouse(b):
    if b == 1:
        words = "You have safely exited the house and survived. You live to see the light of day again."
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        quit()    
        
        
def tellFriends(b):
    if b == 2:
        words = '''
        You run back to tell your friends about the freaky gnomes you found but suddenly feel nauseous and collapse. 
        The last thing you see before you pass out is the laughing face of the gnome.
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        quit()        
        
        
def weirdFeeling(c):
    if c == 1:
        words = '''
        Against your will, your arms turn the steering wheel and you drive back to the house where you encounter the shadow. 
        The shadow wraps around you and drags you back into the house. You will never see the light of day again.
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        quit()  
        
        
def crazy(c):
    if c == 2:
        words = '''
        Against your will, your arms turn the steering wheel and you drive back to the house where you encounter the shadow. 
        The shadow wraps around you and drags you back into the house. You will never see the light of day again.
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        quit()   
        
        
def someWrong(d):
    if d == 1:
        words = '''
        You frantically tell your friends to stop and turn back because something feels off. However it is too late. 
        The door shuts behind you and you and your friends fall prey to a horrible creature that lurks inside.
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        quit()    
        
def keepSelf(d):
    if d == 2:
        words='''You decide not to tell your friends about this weird feeling and proceed into the room. 
        However you find nothing of interest there and leave the house, relieved that you are still alive.
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        quit()
        
def gameOver(x,y,z):
    if x != 1 or 2:
        print ("THAT IS NOT A CHOICE. THE CONSQUENCE IS IMMEDIATE DEATH!!!")
        words = '''
        Game Over
        '''
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif y != 1 or 2:
        print ("THAT IS NOT A CHOICE. THE CONSQUENCE IS IMMEDIATE DEATH!!!")
        words = '''
        Game Over
        '''
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif z != 1 or 2:
        print ("THAT IS NOT A CHOICE. THE CONSQUENCE IS IMMEDIATE DEATH!!!")
        words = '''
        Game Over
        '''
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif a != 1 or 2:
        print ("THAT IS NOT A CHOICE. THE CONSQUENCE IS IMMEDIATE DEATH!!!")
        words = '''
        Game Over
        '''
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif b != 1 or 2:
        print ("THAT IS NOT A CHOICE. THE CONSQUENCE IS IMMEDIATE DEATH!!!")
        words = '''
        Game Over
        '''
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif c != 1 or 2:
        print ("THAT IS NOT A CHOICE. THE CONSQUENCE IS IMMEDIATE DEATH!!!")
        words = '''
        Game Over
        '''
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    elif d != 1 or 2:
        print ("THAT IS NOT A CHOICE. THE CONSQUENCE IS IMMEDIATE DEATH!!!")
        words = '''
        Game Over
        '''
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    else:
         words = '''
        Game Over
        '''
         for char in words:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    

Entrance()
x = choosePath()
y = leftDoor(x)
z = rightDoor(x)
a = light(y)
b = leave(y)
c = apart(z)
d = together(z)
getFriends(a)
goHome(a)
leaveHouse(b)
tellFriends(b)
weirdFeeling(c)
crazy(c)
someWrong(d)
keepSelf(d)
gameOver(x,y,z)


