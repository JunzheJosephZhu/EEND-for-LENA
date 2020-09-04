import glob
import json
wavfiles = glob.glob('/home/joseph/Desktop/LENA_praat/OLD PROTOCOL/**/*.wav', recursive = True)
wavfiles.sort()
import random
random.seed(0)
random.shuffle(wavfiles)
trainfiles = wavfiles[:80]
testfiles = wavfiles[80:]
print(len(trainfiles), len(testfiles))
def findmap(wavfile):
    try:
        annofile = glob.glob(wavfile.replace('.wav', '*.TextGrid'))[0]
        return annofile
    except:
        annofile = glob.glob(wavfile.replace('.wav', '*.textgrid'))[0]
        return annofile
with open('/home/joseph/Desktop/LENA_praat/train.scp', 'w+') as file:
    dict = {}
    for trainfile in trainfiles:
        dict[trainfile] = findmap(trainfile)
    json.dump(dict, file)
with open('/home/joseph/Desktop/LENA_praat/test.scp', 'w+') as file:
    dict = {}
    for testfile in testfiles:
        dict[testfile] = findmap(testfile)
    json.dump(dict, file)