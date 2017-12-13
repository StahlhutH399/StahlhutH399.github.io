#Destiny

def greeting():
    print("You wake up in the middle of a junkyard filled with broken cars, destroyed junk, broken buildings, snowy soil, and a sense of danger all around you.")
    input("(Press Enter To Continue)")
    print("Unknown: " + "Guardian! Thank the Traveler I found you!")
    input("")
    print("You: What the hell is going on?")
    input("")
    print("You get your bearings on what the hell is going on and notice a robotic, floating shell in front of you.")
    input("")
    print("(You can choose what to type in response to the characters story. The choices you have to say are in parenthesis. This will affect the main story as you progress.)") 
    input("(Press Enter To Continue)")
    response = input("(Who are you?)")
    return response

def haters():    
    print("Unknown: No time to explain... We must go now!")
    input("")
    print("You run into a pack of strange looking creatures with guns that somehow have electricity conducting through them.")
    response=input("(Hide/Fight)")
    return response

def Hide():
    print("You hide behind a destroyed bus.")
    input("")
    print("The creatures then start to come towards the destroyed bus, until they hear an explosion and retreat.")
    input("")
    print('You hear a whisper on your shoulder, "The fallen."')
    input("")
    print("You look to your shoulder and find the shell floating just above your shoulder.")
    input("")
    response = input("(Tell me... Who are you?/Lets go.)")
    return response
    
x = greeting()

if x=="Who are you?":
    y = haters()
    if y=="Hide":
        Hide()
    elif y=="Fight":        
        print("You try to punch them since you have no weapon but end up being killed from being shot with the electricity gun that they have.")
        input("")
        print("They then hear an explosion and retreat.")
        input("")
        print("But then, you come back to life as the shell you are with revives you.")
        input("")
        print("You gasp for air and look at the shell that has revived you.")
        response = input("(Tell me... Who are you?/Lets go.)")

a = Hide()

if a=="Tell me... Who are you?":
  print("Ghost: Fine... I am your Ghost, the traveler has sent me centuries ago to find you, now I have found you. Now lets get out of here!")
  input("")
  print("You push on forward to this body with a gun next to it. You check if it has ammo and luckily it does.")
  input("")
  print("You then find an old ship.")
  input("")
  print("Ghost: Let me see if I can start this up.")
  input("")
  print("Your Ghost then levitates to the ship and fixes it.")
  input("")
  print("Suddenly, the fallen captain has appeared and looks angry.")
  input("")
  print("You hear behind you a ear shattering, spine shivering scream come from the captain.")
  input("")
  print("You: Hurry up!")
  input("")
  print("Ghost: Almost done!")
  input("")
  print("You shoot the unlimited fallen that run towards you and you end up running out of ammo.")
  input("")
  print("Ghost: Alright it's ready, but it can only reach the city.")
  input("")
  print("Your Ghost transmats you into the ship and it flies away just in time.")
  input("")
  print("Coming Soon...")
   
 
