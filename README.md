# Instagram-Bot
A python script to tag people into a post, using as many accounts the user has

### Installation
First, install python3 on your machine, then run the following command to install Selenium
```
pip3 install selenium
```

After that, run the bot.py file to start the script
```
python bot.py
```

### Requirements
To work properly, you will need to fill the file 
```
lista_ig
```
with your own users following the exemple inside the file(You might want to delete the exemple on it)

You also need to have the Google Chrome installed on your machine
(For now, the script only works on Windows, but soon will be added the right files to work on linux too)



### Instructions
The bot will ask you :
#### How many accounts do you want to sign in
#### The user and passowd for each account
For each account, the bot will try to log in, make sure to allow it on your app. If you input the wrong login or password, the bot will keep asking the correct information, until you the loggin be successfull
#### The URL from the post that you want to tag the people
#### And how many people you want to tag in each commentary

