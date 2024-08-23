#DAY 4 - ONE TIME KEYPAD
#Dependencies
import random
import string
#Keypad maker, makes a random key of letters based off of length of the message
def makeKeypad(msgLength):
  result = ""
  for i in range(msgLength): #Go thorugh each letter in the string
    result += random.choice(string.ascii_letters)
  return result
#Converts a string of letters to a string of bits
def convertToBits(str):
  result = ""
  for i in range(len(str)): #Go thorugh each letter in the string
     #Converts ascii value of letter to 8bit binary
    result += format(ord(str[i]), '08b')
  return result
#Reverts a string of bits to a string of readable letters
def revertFromBits(str):
  j = 0
  result = ""
  while j < len(str): #Go thorugh each letter in the string
    #Converts 8bit binary to asii value and then to letter
    result += chr(int(str[j:j + 8], 2))
    j += 8
  return result
#Encrypts a message using a keypad via bit flipping
def encrypt(msg, keyPad):
  #Variablle initialization
  bitText = ""
  bitMsg = convertToBits(msg)
  bitKey = convertToBits(keyPad)
  #Goes through every bit in message
  for i in range(len(bitMsg)): 
    #XOR bit flips the message by key
    if bitMsg[i] == bitKey[i]: 
      bitText += "0"
    else:
      bitText += "1"
  return revertFromBits(bitText)
#Decrypts a message using a keypad via bit flipping
def decrypt(cip, keyPad):
  #Variablle initialization
  bitText = ""
  bitCip = convertToBits(cip)
  bitKey = convertToBits(keyPad)
  #Goes through every bit in message
  for i in range(len(bitCip)):
    #XOR bit flips the cipherText by key
    if bitCip[i] == bitKey[i]:
      bitText += "0"
    else:
      bitText += "1"
  return revertFromBits(bitText)
#Encryption and random key generation
message = input("Enter your secret message: ")
keyPad = makeKeypad(len(message))
print("KeyPad is " + keyPad)
cipherText = encrypt(message, keyPad)
print(cipherText)
#Decryption
message = decrypt(cipherText, keyPad)
print(message)
