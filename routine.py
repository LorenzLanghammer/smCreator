import time
import pyautogui as pag
from gui_functions import *
import pyscreeze
from helper import*
import zendriver as zd
import asyncio
#from smsActivate import *





#name = generateName()
password = ""
country = ""
phone_id = 0
username = ""
number_first_attempt = True

class Routine:
    def __init__(self, page, identifier):
        self.page = page
        self.identifier = identifier
    async def executeRoutine(self):
        pass



