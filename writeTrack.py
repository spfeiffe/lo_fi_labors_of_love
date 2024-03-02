import os
import sys
#def writeTrack(metronomeSpeed, noteArrayFile, outFile):
print("     validating your input... ")

{
"metronomeSpeed":   80,
"rightHandPiano":   [
                        {"noteType":"dottedEighthMarcato",  "pitch":"C4",   "volume":"mp",  "instrument":""}, 
                        {"noteType":"quarterREST",          "pitch":"",     "volume":"",    "instrument":""},
                        {}
                    ],
"leftHandPiano":    [
                    ],
"percussion":       [
                    ]
}


metronomeSpeed = int(sys.argv[1])
if type(metronomeSpeed) is not int:
    raise Exception("type(int(sys.argv[1])) must be `int`")
with open(sys.argv[2], "r") as f:
    x = f.read()
myNoteArray = eval(x)
if type(myNoteArray) is not list:
    raise Exception("type(myNoteArray) must be `list`")
if set([type(note) is list for note in myNoteArray]) != {True}:
    raise Exception("every note in myNoteArray must be a `list`")
for note in myNoteArray:
    # assertions
