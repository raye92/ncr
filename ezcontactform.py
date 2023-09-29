import webbrowser
import time
from pynput.mouse import Button, Controller
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController

import os
os.environ['DISPLAY'] = ':0'

keyboard = KeyboardController()
mouse = MouseController()

def autofill ():
    webbrowser.open('https://lijingtuzhi.com')

    time.sleep(10)

    #move to contact button and click
    x_absolute = 1370
    y_absolute = 200
    mouse.position = (x_absolute, y_absolute)
    mouse.click(Button.left, 1)

    time.sleep(8)

    #move to first name input box and click
    x_absolute = 500
    y_absolute = 750
    mouse.position = (x_absolute, y_absolute)
    mouse.click(Button.left, 1)
    #inputs
    keyboard.type('First \tLast \tEmail \tComment')

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type('WOW ENTER')

    '''
    #Code for moving to and clicking last name, not needed with tab from keyboard type
    y_absolute = 755
    mouse.position = (x_absolute, y_absolute)
    mouse.click(Button.left, 1)

    #Code for printing mouse coordinates
    x, y = mouse.position
    print(f"Mouse coordinates: X={x}, Y={y}")
    '''

autofill()
