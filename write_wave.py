print("Loading required libraries...")
import math
# import numpy
import os
import random
import struct
import wave

'''
def flattenNestedList(L):
    flattenedList = []
    for i in range(len(L)):
        x = L[i]
        assertion1 = type(x) is str or type(x) is int or type(x) is float or type(x) is bool or type(x) is list # https://www.w3schools.com/python/python_datatypes.asp 
        if not assertion1:
            raise Exception("element " + str(i) + " of the provided nestedList is of type `" + str(type(x)) + "`") 
        if type(x) is list:
            assertion2 = len(x) != 0
            if not assertion2:
                raise Exception("element " + str(i) + " of the provided nestedList is a list but its length is 0") 
            if len(x) > 1:
                for item in x:
                    flattenedList.append(item)
            else:
                flattenedList.append(x)
        else:
            flattenedList.append(x)
    return(flattenedList)
'''

# os.getcwd()

sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz

Nframes = int(sampleRate * duration)

print("Writing data...")

myNotesArray = []

'''
#
for i in range(4):
    #myInt = random.randint(-32767, 32767)
    #myToneOrSilence = struct.pack("<h", myInt)
    #for r in range(11025):
    #    myNotesArray.append(myToneOrSilence) # Nframes / 4 = 11025. 
'''

def appendFull(x): # appendQuarter(x):
    #
    assertion1 = type(x) is int
    if not assertion1:
        raise Exception("type(x) is `" + str(type(x)) + "` but must be int")
    #
    assertion2 = x >= 0
    if not assertion2:
        raise Exception("x must be >= 0")
    #
    assertion3 = x <= 255
    if not assertion3:
        raise Exception("x must be <= 255")
    #
    for r in range (44100): # for r in range(11025):
        myNotesArray.append(x)

appendFull(random.randint(0, 255))
#appendQuarter(random.randint(0, 255))
#appendQuarter(random.randint(0, 255))
#appendQuarter(random.randint(0, 255))

myFramesArray = bytes(myNotesArray)

# myFramesArray = b''.join(myNotesArray) # https://stackoverflow.com/questions/25831710/convert-a-list-of-bytes-to-a-byte-string 

with wave.open(str(len(os.listdir())+3)+".wav", "w") as w:
    w.setnchannels(1) # mono
    w.setsampwidth(1) # w.setsampwidth(2)
    w.setframerate(sampleRate)
    w.setnframes(Nframes)
    #
    w.writeframes(myFramesArray)

input()