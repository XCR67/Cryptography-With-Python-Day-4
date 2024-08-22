#Symmetric Encryption, One Time Keypad on Line 46
#Dependencies
import random
import string
#Converts readable text into Hexadecimal
def conHex(message):
  result = ""
  for i in range(len(message)):
    result += str(hex(ord(message[i]))) #Convert its to ascii > Hexadecimal > String
  return result
#Reverts the Hexadecimal string back into readable text
def revHex(hexmessage):
  result = ""
  letter = 2
  while letter < len(hexmessage): #Go though every letter in the message
    tenplc = int(hexmessage[letter], 16) * 16
    onesplc = int(hexmessage[letter + 1], 16) 
    result += chr(tenplc + onesplc) #Converts sum into its letter equivalent using ascii
    letter += 4 #Move to the next letter
  return result
#Encrypts the message by adding the key to the message
def encryptSymm(message, key):
  #Variable initializationa nd converts key and message to encryptable hex values
  message = conHex(message)
  key = conHex(key)
  index = 2
  cipherText = ""
  while index < len(message) - 1: #Go thorugh eac letter in message
    #Swap hex values of message and key by adding their tens and ones places
    ten = int(message[index], 16) * 16 + int(key[index + 1], 16)
    one = int(message[index + 1], 16) + int(key[index], 16) * 16
    cipherText += chr(ten + one) #Converts sum into its letter equivalent using ascii
    index += 4
  return cipherText
#Decrypts the encrypted text with the same key
def decryptSymm(cipherText, key):
  #Variable initializationa nd converts key and message to decryptable hex values
  cipherText = conHex(cipherText)
  key = conHex(key)
  index = 2
  message = ""
  while index < len(cipherText) - 1: #Go thorugh eac letter in message
    #Revert hex values of message and key by subtracting their tens and oens places
    ten = int(cipherText[index], 16) * 16 - int(key[index + 1], 16)
    one = int(cipherText[index + 1], 16) - int(key[index], 16) * 16
    message += chr(ten + one) #Converts sum into its letter equivalent using ascii
    index += 4
  return message
#Encryption and Key Generation
message = input("Enter your secret message: ")
key = input("Enter a key of at least length " + str(len(message)) + ":")
while len(key) < len(message): #Makes sure the key is as long as the message
  key = input("Key must be at least length " + str(len(message)) + ":")
print("Key is " + key)
cipherText = encryptSymm(message, key)
print(cipherText)
#Decryption
print(decryptSymm(cipherText, key))



#One Time keypad
#Dependencies, theyre commented out because theyre already imported
#import random
#import string
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