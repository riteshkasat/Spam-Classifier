import pickle as pkl
import os, sys
import math

def checkSpamOrHam(path, name):
    global hamWordProbabilities
    global spamWordProbabilities
    global probabilityOfSpam
    global probabilityOfHam
    global output

    filePath = os.path.join(path, name)
    file = open(filePath, "r", encoding="latin1" )
    pSpam = math.log(probabilityOfSpam); pHam = math.log(probabilityOfHam)
    for line in file:
        line = line.strip().split()
        for word in line:
            if word in hamWordProbabilities:
                pHam += math.log(hamWordProbabilities[word])
                pSpam += math.log(spamWordProbabilities[word])


    if pHam>pSpam:
        print('ham ' + name, file=output )
        # print('ham ' + name)

    else:
        print('spam ' + name, file=output )
        # print('spam ' + name)


if __name__ == '__main__':

    #read test data
    walk_dir = os.path.abspath(sys.argv[1])
    # walk_dir =  os.path.abspath('./data/dev')

    #read pickled objects
    file = open('nbmodel.txt', 'rb')
    objectFile = pkl.load(file)
    probabilityOfSpam = objectFile[0]['probabilityOfSpam']
    probabilityOfHam = objectFile[1]['probabilityOfHam']
    hamWordProbabilities = objectFile[2]
    spamWordProbabilities = objectFile[3]

    #create output file
    output = open('nboutput.txt', 'w')

    for path, subdirs, files in os.walk(walk_dir):
        for name in files:
            if name == '.DS_Store':
                continue

            checkSpamOrHam(path, name)

