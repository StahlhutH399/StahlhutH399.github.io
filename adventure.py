#My Python Story

def greeting():
    print("Hello....")
    response=input("do you want to play? (yes/no)")
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
        
