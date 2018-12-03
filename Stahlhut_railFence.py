#Program is suppost to take the users input and choose whether to decrypt or encrypt a piece of string and run the code
#Written by Martin Stahlhut

choose = input("Would you like to decypt(d) or encrypt(e): ")

if (choose == "e"):
    Scramble2Text()

elif (choose == "d"):
    Scramble2Decrypt()
    

def Scramble2Text(plainText):
    plainText = input("Insert phrase here: ")
    char = 0
    evenChars = ""
    oddChars = ""
    for ch in plainText:
        if(char%2 == 0):
            evenChars += ch
        else:
            oddChars += ch
        char += 1
    ciphertext = oddChars + evenChars
    return ciphertext

def Scramble2Decrypt(cipherText):
    cipherText = input("Insert encrypted phrase here: ")
    half = len(cipherText) // 2
    oddChars = cipherText[:half]
    evenChars = cipherText[half:]
    print(evenChars)
    print(oddChars)
    plainText = ""
    for i in range(half):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]
    if len(evenChars) > len(oddChars):
        plainText = plainText + evenChars[-1]
    return plainText



