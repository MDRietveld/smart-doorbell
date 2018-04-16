import sys
import telepot
import RPi.GPIO as GPIO
import subprocess
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    
    if GPIO.input(10) == GPIO.HIGH:
        bot = telepot.Bot(TOKEN)
        bot.sendMessage(CHAT_ID, 'Ring Ring')
        os.system('fswebcam image.jpg -S 2')
        bot.sendPhoto(CHAT_ID, open('image.jpg', 'rb'))
