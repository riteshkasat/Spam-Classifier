import os
import sys
import pickle as pkl

def buildDictionary(category, directory, files, count):
    global vocabulary; global numberOfFiles
    for file in files:
        if file == '.DS_Store':
            continue

        file_path = os.path.join(directory, file)
        with open(file_path, "r", encoding="latin1" ) as f:
            numberOfFiles += 1; count += 1
            for line in f:
                line = line.strip().split()
                for token in line:
                    if token not in category:
                        category[token] = 1;

                    else:
                        category[token] += 1;

                    if token not in vocabulary:
                        vocabulary[token] = 1
    return category,count


def calculateWordProbabilities(category):
    global vocabulary;
    wordProbabilites = {};
    vocabularySize = sum(vocabulary.values())
    totalWordCountInCategory = sum(category.values())

    for word in vocabulary:
        individualWordCount = category[word] if word in category else 0
        probability = float(individualWordCount + 1) / float(totalWordCountInCategory + vocabularySize)
        wordProbabilites[word] = probability
    return wordProbabilites


if __name__ == '__main__':
    stopword = set()
    with open("stopwords.txt") as f:
        for line in f:
            stopword.add(line.strip())

    walk_dir = os.path.abspath(sys.argv[1])
    vocabulary = {}; spam = {}; ham = {}; numberOfFiles = 0
    numberOfSpamFiles = 0; numberOfHamFiles = 0
    for root, subdirs, files in os.walk(walk_dir):
        nameOfDirectory = root.split('/')[-1]
        if nameOfDirectory == 'ham':
            ham, numberOfHamFiles = buildDictionary(ham, root, files, numberOfHamFiles)

        elif nameOfDirectory == 'spam':
            spam, numberOfSpamFiles = buildDictionary(spam, root, files, numberOfSpamFiles)


    #prior probabilities of spam and ham
    probabilityOfSpam = numberOfSpamFiles/numberOfFiles
    probabilityOfHam = 1 - probabilityOfSpam

    #individual word probabilities given spam or ham
    hamWordProbabilities = calculateWordProbabilities(ham)
    spamWordProbabilities = calculateWordProbabilities(spam)
    pickledObjects = [{'probabilityOfSpam' : probabilityOfSpam}, {'probabilityOfHam' : probabilityOfHam},
                     hamWordProbabilities, spamWordProbabilities]

    pkl.dump( pickledObjects, open( "nbmodel.txt", "wb" ))
