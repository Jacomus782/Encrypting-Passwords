#Alphabet
from cmath import e


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&()_:\"{}<>?\'~`;,.[]=/*-+|"

#USER INPUT
des = str(input("Decrypt or Encrypt enter (D/E): "))
key = str(input("Enter Key: "))


# DECRYPT
if des == "D":
    temppass = []
    tempkey = []

    encpass = str(input("Enter a password to Decrypt: "))
    for i in encpass:
        if i in alpha:
            temppass.append(alpha.find(i))
        else:
            print("Error  unusable Character: " )
            print(i)
    
    for i in key:
        if i in alpha:
            tempkey.append(alpha.find(i))

    # Make the length of the key greater then the password 
    while len(temppass) > len(tempkey):
        tempkey += tempkey

    # Create number decryption
    decpassnum  = []
    for i in range(len(temppass)):
        X = temppass[i] + tempkey[i]
        if X > len(alpha)-1:
            X = X - len(alpha)
        decpassnum.append(X)
    
    # Convert number to string
    decpass = []
    for i in decpassnum:
        decpass.append(alpha[i])
    print(''.join(decpass))


# Encrypt
if des == "E":
   temppass = []
   tempkey = [] 

   encpass = str(input("Enter a Password to Encrypt: "))
   for i in encpass:
       if i in alpha:
           temppass.append(alpha.find(i))
       else:
           print("Error  unusable Character: " )
           print(i)
   
   for i in key:
       if i in alpha:
           tempkey.append(alpha.find(i))
   
   while len(temppass) > len(tempkey):
        tempkey += tempkey
   
   encpassnum = []
   for i in range(len(temppass)):
        X = temppass[i] - tempkey[i]
        if X < 0:
            X = X + len(alpha)
        encpassnum.append(X)

   encpass = []
   for i in encpassnum:
        encpass.append(alpha[i])
   print(''.join(encpass))

input('press any Enter to end the program')
