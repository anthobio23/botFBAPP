#!/usr/bin/python3

import os
import time 
import pyautogui as ag

class ControlKeyboard:

    def __init__(self, key, num_Product):
        self.key = key
        self.num_Product = num_Product
        pass

    def KEY(self):

        # Entramos a la carpeta de documentos
        time.sleep(2)
        ag.press(self.key)
        ag.press(self.key)
        time.sleep(2)
        if self.num_Product == 6:
            ag.press("down", presses=2)
        else:
            ag.press("down", presses=4)
        time.sleep(2)
        #entrar a la carpeta documentos
        ag.press("enter")
        time.sleep(2)
        ag.press("right", presses=2)
        time.sleep(2)

        # carpeta img_convert
        for iter in range(0, 14): ag.press("down")
        ag.press("enter")
        time.sleep(2)
        # nuevos productos    
        ag.press("down", presses=2)
        ag.press("enter")
        time.sleep(2)
    
        # Carpeta de Zapatos casuales
        ag.press("enter")
        time.sleep(1)
        ag.press("down", presses=self.num_Product)
        time.sleep(1)
        ag.press("enter")
        time.sleep(2)
        for iter in range(0, 2): 
            ag.hotkey("shift", "down", inteval=1)
            time.sleep(2)
            pass
        ag.press("enter", presses=2)
        pass
    pass

 
if __name__ == "__main__":
    pass

