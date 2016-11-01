# Email Spam Classifier
This is an implementation of the simple but effective machine learning technique, Naïve Bayes classification for a binary text classification task (i.e., spam detection).

Requirements
-------------
- Python 3

Data
-----
**train-data**
This directory stores the training data. The code recursively looks for folders: "ham" and "spam". You can have multiple "ham" and "spam" folders in the data directory. Emails are stored in files with the extension ".txt" under these directories.


**test-data**
This directory stores the unlabelled data files that needs to be classified as spam or ham.

**Note:** The repo contains dummy data with handful of spam and ham files for training. For significant result, please collect large amount of data.

Installation
------------

After cloning, create a virtual environment and install the requirements. For Linux and Mac users:

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

If you are on Windows, then use the following commands instead:

    $ virtualenv venv
    $ venv\Scripts\activate
    (venv) $ pip install -r requirements.txt

Building the application
-------------------------

After completing the installation, run the following command:

    (venv) $ pyb

Running
-------

If you want to run the service locally, uncomment following line from application.py

    
    application.run()

To run the server use the following command:

    (venv) $ python application.py
     * Running on http://127.0.0.1:5000/
     * Restarting with reloader

Then from a different terminal window you can send requests.




#UserRegistrationAPI
====================

API for User registration. The user information is stored in a SQLite Database with username as the primary key and a hashed password, once the password hash is generated the password is discarded and never stored. Once a new users are registered, the user can be authenticated in two ways using the username/password combination or a generated token. The token has an expiration of 600 sec once the token has expired a new token is generated after the login page is prompted.




API Documentation
-----------------

- POST **/api/users**

    Register a new user.<br>
    The body must contain a JSON object that defines `username` and `password` fields.<br>
    On success a status code 201 is returned. The body of the response contains a JSON object with the newly added user. A `Location` header contains the URI of the new user.<br>
    On failure status code 400 (bad request) is returned.<br>

- GET **/api/users/&lt;int:id&gt;**

    Return a user.<br>
    On success a status code 200 is returned. The body of the response contains a JSON object with the requested user.<br>
    On failure status code 400 (bad request) is returned.

- GET **/api/token**

    Return an authentication token.<br>
    On success a JSON object containing field `token` set to the authentication token for the user and a field `duration` set to the (approximate) number of seconds the token is valid.<br>
    On failure status code 401 (unauthorized) is returned.

- GET **/api/storefront**

    Once the User is authenticated wither by a token or username/password the storefront page is loaded.<br>
    Return a protected resource.<br>
    On success a JSON object with data for the authenticated user is returned.<br>
    On failure status code 401 (unauthorized) is returned.
