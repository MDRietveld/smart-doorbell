# Smart Doorbell Project
With this code your doorbell sends an image to your telegram app

Install telepot to send messages to telegram

> pip install telepot


Test telepot in your terminal
Type the following lines: 

>>> python

>>> import telepot

>>> bot = telepot.Bot('***** PUT YOUR TOKEN HERE *****')

>>> bot.getMe()


With this you get the information of the Telegram bot 

This link is to get the chat_id for sending images to yourself

https://api.telegram.org/bot **TOKEN HERE** /getUpdates


Install fswebcam to make photo's

>>> sudo apt-get install fswebcam


Making a picture

>>> fswebcam image.jpg
