#DAY 4 - ONE TIME KEYPAD
#Dependencies (random and string)

#Keypad maker, makes a random key of letters based off of length of the message
#def makeKeypad(msgLength):
  #Create result string

  #Loop msglength times
    #Add a random ascii value using random.choice() and string.ascii_letters

  #Return the result


#Converts a string of letters to a string of bits
#def convertToBits(str):
  #Create result string
  
  #Go thorugh each letter in the string
     #Converts ascii value of letter to 8bit binary using its ascii value and format(num, '08b')

  #Return the result


#Reverts a string of bits to a string of readable letters
#def revertFromBits(str):
  #Create a result string and index variable

  #Go through each letter in the string using  while loop
    #Converts 8bit binary to asii value and then to letter using chr(), int(str, 2), 
    #and an 8-bit binary sequence. Add this converted letter

    #Increase the index to the next set of 8-bit

  #Return the result


#Encrypts a message using a keypad via bit flipping
#def encrypt(msg, keyPad):
  #Variable initialization, converts msg and keyPad to binary, make a result string

  #Loops through every bit in message
    #XOR bit flips the message with key
      #Adds to the result string

  #Returns the result string reverted from binary


#Decrypts a message using a keypad via bit flipping
#def decrypt(cip, keyPad):
  #Variable initialization, converts cip and keyPad to binary, make a result string
  
  #Loops through every bit in message
    #XOR bit flips the cipherText with key
      #Adds to the result string

  #Returns the result string reverted from binary

#Encryption and random key generation

#Decryption
