
# Welcome to Al Amin Khan's Github - "(Auto Message for Messenger)" Code
# you have to install 'pyautogui' package first, then you get your desire output from this code
# The 'PyAutoGui' package install code is ------ pip install PyAutoGui
# You just copy this code, and paste in the terminal

# ====================================================================================================
# ====================================================================================================
# ====================================================================================================


# Using FOR LOOP in this code
# Code Number: 1
# Code Start

import pyautogui as pu
import time

message = str(input("Enter your message: "))
num_messages = int(input("How many times you want to send message? "))

for _ in range(num_messages):
    time.sleep(3)
    pu.typewrite(message)
    pu.press('Enter')


# Code Finished
# --------------------------

# Using WHILE LOOP in this code ---------------
# Code Number: 2
# Code Start


import pyautogui as pu
import time

message = str(input("Enter your message: "))
num_messages = int(input("How many times you want to send message? "))
i = 1

while i <= num_messages:
    time.sleep(3)
    pu.typewrite(message)
    pu.press('Enter')
    i = i + 1


# Code Finished
# --------------------------