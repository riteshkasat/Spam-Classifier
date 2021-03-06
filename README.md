# Email Spam Classifier
This is an implementation of the simple but effective machine learning technique, Naïve Bayes classification for a binary text classification task (i.e., spam detection).

Requirements
-------------
- **Python 3**

- **train-data**
This directory contains the training data. The code recursively looks for sub-directories: "ham" and "spam". You can have multiple "ham" and "spam" sub-directories inside this directory. Emails must be stored in files with the extension ".txt" under these sub-directories.


- **test-data**
This directory contains the unlabelled data files that needs to be classified as spam or ham.

- **stopwords.txt**
This is a text file that contains list of words which are filtered out before processing of natural language data (text)

**Note:** This repo contains demo data with a handful of spam and ham files for training. For significant results, please collect large amount of training data.

Running
-------
    
- This repo contains two programs: 
    - nblearn.py which learns a naive Bayes model from labeled data, and write the model parameters to a file called nbmodel.txt. 
    - nbclassify.py will use the model generated in above step to classify new data. 

nblearn.py will be invoked in the following way:
    
    python3 nblearn.py /path/to/training/data 

nbclassify.py will be invoked will be invoked in the following way:

    python3 nbclassify.py /path/to/test/data

this will write the result to a text file called nboutput.txt in the following format:

LABEL path_1<br/>
LABEL path_2</br/>
⋮</br>
In the above format, LABEL is either “spam” or “ham” and path is the path to the file, and the name of filename 

