print('     loading required modules... ')
import numpy
import os
import wave
# for how I processed samples/patches, see https://sound.stackexchange.com/questions/22769/are-there-free-records-of-separate-piano-notes-in-wav-files-for-instance 
noteOrRestLengths = [
'whole',
'half',
'quarter',
'eighth',
'sixteenth',
'32nd',
'halfNoteTriplet',
'quarterNoteTriplet',
'eighthNoteTriplet',
'sixteenthNoteTriplet'
]
#
def howManyBeats(thisNoteOrRestLength):
    match thisNoteOrRestLength:
        case 'whole':
            return(4) #
        case 'half':
            return(2)
        case 'quarter':
            return(1)
        case 'eighth':
            return(4/8)
        case 'sixteenth':
            return(4/16)
        case '32nd':
            return(4/32)
        case 'halfNoteTriplet':
            return(4/3)
        case 'quarterNoteTriplet':
            return(2/3)
        case 'eighthNoteTriplet':
            return(1/3)
        case 'sixteenthNoteTriplet':
            return((1/3)/2)
#
pitches = [
'A0',
'Ab0',
'B0',
#
'C1',
'Db1',
'D1',
'Eb1',
'E1',
'F1',
'Gb1',
'G1',
'Ab1',
'A1',
'Bb1',
'B1',
#
'C2',
'Db2',
'D2',
'Eb2',
'E2',
'F2',
'Gb2',
'G2',
'Ab2',
'A2',
'Bb2',
'B2',
#
'C3',
'Db3',
'D3',
'Eb3',
'E3',
'F3',
'Gb3',
'G3',
'Ab3',
'A3',
'Bb3',
'B3',
#
'C4',
'Db4',
'D4',
'Eb4',
'E4',
'F4',
'Gb4',
'G4',
'Ab4',
'A4',
'Bb4',
'B4',
#
'C5',
'Db5',
'D5',
'Eb5',
'E5',
'F5',
'Gb5',
'G5',
'Ab5',
'A5',
'Bb5',
'B5',
#
'C6',
'Db6',
'D6',
'Eb6',
'E6',
'F6',
'Gb6',
'G6',
'Ab6',
'A6',
'Bb6',
'B6',
#
'C7',
'Db7',
'D7',
'Eb7',
'E7',
'F7',
'Gb7',
'G7',
'Ab7',
'A7',
'Bb7',
'B7',
#
'C8'
]
#
def getChannelLength(c):
    lengthOfThisChannel = 0
    if type(c) is not list:
        raise Exception('type(c) must be list')
    for i in range(len(c)):
        if type(c[i]) is not dict:
            raise Exception('type(c[' + str(i) + '] must be dict')
        if 'noteOrRestLength' not in dict.keys(c[i]):
            raise Exception('"noteOrRestLength" must be in dict.keys(c[' + str(i) + '])')
        if '_' in c[i]["noteOrRestLength"]:
            for thisNoteStem in c[i]["noteOrRestLength"].split('_'):
                lengthOfThisChannel += howManyBeats(thisNoteStem)
        else:
            lengthOfThisChannel += howManyBeats(c[i]["noteOrRestLength"])
    return(lengthOfThisChannel)
#
def writeTrack():
    #
    print('     validating your input... ')
    if not os.path.exists(os.path.join(os.getcwd(),'myInput.txt')):
        raise Exception('`myInput.txt` must exist')
    with open('myInput.txt', 'rt', encoding='utf-8') as f:
        myInput = f.read()
    d = eval(myInput) # 'd' for python dict
    if not 'metronomeSpeed' in dict.keys(d):
        raise Exception('please specify `metronomeSpeed`')
    if type(d["metronomeSpeed"]) is not int:
        raise Exception('type("metronomeSpeed") must be int')
    if len(dict.keys(d)) < 2:
        raise Exception('please add at least one channel')
    for X in dict.keys(d):
        if X != 'metronomeSpeed':
            if type(d[X]) is not list:
                raise Exception('type("' + X + '") must be list')
            if len(d[X]) == 0:
                raise Exception('len("' + X + '" must be >= 1')
            for i in range(len(d[X])):
                if type(d[X][i]) is not dict:
                    raise Exception('type("' + X + '"[' + str(i) + '] must be dict')
                if "_" in d[X][i]["noteOrRestLength"]:
                    if "__" in d[X][i]["noteOrRestLength"] or if d[X][i]["noteOrRestLength"][0]=="_" or d[X][i]["noteOrRestLength"][len(d[X][i]["noteOrRestLength"])]=="_": 
                        raise Exception('["' + X + '"][' + str(i) + ']["noteOrRestLength"] is formatted improperly:   ' + d[X][i]["noteOrRestLength"]) 
                    for j in range(len(d[X][i]["noteOrRestLength"].split("_"))):
                        if d[X][i]["noteOrRestLength"].split("_")[j] not in noteOrRestLengths:
                            raise Exception('["' + X + '"][' + str(i) + ']["noteOrRestLength"].split("_")[' + str(j) + '] must be in `noteOrRestLengths`, but instead is "' + d[X][i]["noteOrRestLengths"].split("_")[j] + '"') 
                else:
                    if d[X][i]["noteOrRestLength"] not in noteOrRestLengths:
                        raise Exception('["' + X + '"][' + str(i) + ']["noteOrRestLength"] must be in `noteOrRestLengths`, but instead is "' + d[X][i]["noteOrRestLength"] + '"') 
                if d[X][i]["isRest"]:
                    if d[X][i]["pitch"] != "":
                        raise Exception('since ["' + X + '"][' + str(i) + ']["isRest"] is True, ["' + X + '"][' + str(i) + ']["pitch"] must == ""') 
                    if d[X][i]["instrument"] != "":
                        raise Exception('since ["' + X + '"][' + str(i) + ']["isRest"] is True, ["' + X + '"][' + str(i) + ']["instrument"] must == ""') 
                    if d[X][i]["volume"] != "":
                        raise Exception('since ["' + X + '"][' + str(i) + ']["isRest"] is True, ["' + X + '"][' + str(i) + ']["volume"] must == ""') 
                    if d[X][i]["attackRelease"] != "":
                        raise Exception('since ["' + X + '"][' + str(i) + ']["isRest"] is True, ["' + X + '"][' + str(i) + ']["attackRelease"] must == ""') 
                else:
                    if d[X][i]["pitch"] not in pitches:
                        raise Exception('["' + X + '"][' + str(i) + ']["pitch] must be in `pitches`') 
                    if d[X][i]["instrument"] != "piano":
                        raise Exception('["' + X + '"][' + str(i) + ']["instrument"] must be "piano" for this version')
                    if d[X][i]["volume"] != "mf":
                        raise Exception('["' + X + '"][' + str(i) + ']["volume"] must be "mf" for this version')
                    if d[X][i]["attackRelease"] != "marcato":
                        raise Exception('["' + X + '"][' + str(i) + ']["attackRelease"] must be "marcato" for this version') 
    k = []
    for K in dict.keys(d):
        k.append(K)
    k.remove('metronomeSpeed')
    lengthOfFirstChannel = getChannelLength(d[k[0]])
    if len(k) > 1:
        for y in k[1:]:
            if getChannelLength(d[y]) != lengthOfFirstChannel:
                raise Exception('length of channel "' + k[0] '" = ' + str(round(lengthOfFirstChannel,3)) + ' but length of channel "' + y + '" = ' + str(round(getChannelLength(d[y]),3))) 
    #
    print('     reading patch files... ')
    q = dict.keys(d)
    q.remove('metronomeSpeed')
    for thisChannel in q:
        allFramesForThisChannel = bytes()
        for thisNoteOrRest in thisChannel:
#                                  beats                                                *  minutes/beat           * s/min  * frames/s 
            nFramesOfPatchToRead = howManyBeats(thisNoteOrRest["thisNoteOrRestLength"]) * (1/d["metronomeSpeed"]) * (60/1) * 48000 
            if thisNoteOrRest["isRest"]:
                filepath = os.path.join(os.getcwd(), "samplesPatchesEtc", "silence.wav")
            else:
                filepath = os.path.join(os.getcwd(), "samplesPatchesEtc", "piano", thisNoteOrRest["pitch"], ".wav") 
            with wave.open(filepath, "r") as f: 
                if f.getnchannels() != 2:
                    raise Exception('f.getnchannels() must == 2')
                if f.getsampwidth() != 2:
                    raise Exception('f.getsampwidth() must == 2')
                if f.getframerate() != 48000:
                    raise Exception('f.getframerate() must == 48000')
                theFrames = f.readframes(nFramesOfPatchToRead)[0::2] # don't need stereo 
            allFramesForThisChannel += theFrames
        ## l = ['A','B','C']
        ## m = ['a','b','c']
        ## n = ['1', '2', '3']
        ## o = numpy.repeat(numpy.array([' ']), 3)
        ## p = "".join(["".join(list(x)) for x in zip(l, m, n, o)])
        ## p
        
        
        
        
        
        
        
        
        
                    
'''
{
"metronomeSpeed":   80,
"rightHandPiano":   [
                        {"noteOrRestLength":"quarter_eighth",   "isRest":0,  "pitch":"C4",    "instrument":"piano",   "volume":"mf",  "attackRelease":"marcato"}, 
                        {"noteOrRestLength":"eighth",           "isRest":1,  "pitch":"",      "instrument":"",        "volume":"",    "attackRelease":""} 
                    ],
"leftHandPiano":    [
                    ],
"percussion":       [
                    ]
}
'''