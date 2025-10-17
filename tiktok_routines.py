
import pyautogui as pag
import sys
import os
from country_values_tt import *
import time
from oxymouse import OxyMouse
import pyperclip

script_dir = os.path.dirname(os.path.abspath(__file__))         # project/folder
scripts_dir = os.path.abspath(os.path.join(script_dir, "..", "scripts"))  # project/scripts
sys.path.append(scripts_dir)
from database.dbInterface import *
from routine import *
from email_interface import *


class ScreenArea():
    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

areas = [ScreenArea(824, 211, 1070, 243), 
         ScreenArea(822, 267, 1088, 300), 
         ScreenArea(815, 532, 1076, 581),
         ScreenArea(821, 600, 1076, 693),
         ScreenArea(820, 785, 1086, 845),
         ScreenArea(780, 880, 1130, 961)
         ]


class EnterCredentials_routine_tt(Routine):
    def __init__(self, tab, proxy_username, proxy_password):
        super().__init__(tab, identifier="")
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password

    async def executeRoutine(self):
        pyautogui.write(self.proxy_username)
        pyautogui.press('tab')
        pyperclip.copy(self.proxy_password)
        pyautogui.hotkey('ctrl', 'v')     
        pyautogui.press('enter')
        return True
        


class EnterEmailRoutine(Routine):
    def __init__(self, page, country):
        super().__init__(page, identifier="https://www.tiktok.com/signup")
        self.country = country

    async def executeRoutine(self):
        print("looking for position of element")
        print(CountryEnterEmail[self.country].value)
        enter_email_position = await get_position_by_text(CountryEnterEmail[self.country].value, self.page)
        await asyncio.sleep(3)
        moveToPoint(enter_email_position.x, enter_email_position.y + 10, 2)
        pag.click()
        await asyncio.sleep(5)
        return True


class EnterDetailsRoutine(Routine):
    def __init__(self, page, email, country, password, username):
        super().__init__(page, identifier="https://www.tiktok.com/signup/phone-or-email/phone")
        self.email = email
        self.country = country
        self.password = password
        self.username = username

    async def executeRoutine(self):
        '''
        reject_position = await get_position_by_text("Optionale Cookies ablehnen", self.tab)
        moveToPoint(reject_position.x + random.randint(-10, 20), reject_position.y + random.randint(-5, 5), 2)
        pag.click()
        '''

        month_position = await get_position_by_selector("#loginContainer > div.tiktok-aa97el-DivLoginContainer.exd0a430 > form > div.tiktok-owmehc-DivAgeSelector.e18rms3f0 > div:nth-child(1) > div.tiktok-1leicpq-DivSelectLabel.e1phcp2x1", self.page)
        moveToPoint(month_position.x, month_position.y, 2)
        pag.click()
        moveToPoint(pag.position().x + random.randint(-10, -2), random.randint(360, 610), 2)
        pag.click()
        day_position = await get_position_by_selector("#loginContainer > div.tiktok-aa97el-DivLoginContainer.exd0a430 > form > div.tiktok-owmehc-DivAgeSelector.e18rms3f0 > div:nth-child(2)", self.page)
        moveToPoint(day_position.x, day_position.y, 2)
        pag.click()
        moveToPoint(pag.position().x + random.randint(-3, 3), random.randint(360, 610), 2)
        pag.click()
        year_position = await get_position_by_selector("#loginContainer > div.tiktok-aa97el-DivLoginContainer.exd0a430 > form > div.tiktok-owmehc-DivAgeSelector.e18rms3f0 > div:nth-child(3)", self.page)
        moveToPoint(year_position.x, year_position.y, 2)
        pag.click()
        moveToPoint(pag.position().x, 365, 2)
        scrollDown(7)
        moveToPoint(pag.position().x + random.randint(-3, 3), random.randint(360, 610), 2)
        pag.click()

        use_email_position = await get_position_by_text(CountryUseEmail[self.country].value, self.page)
        moveToPoint(use_email_position.x, use_email_position.y + 30, 2)
        pag.click()

        email_position = await get_position_by_selector("#loginContainer > div.tiktok-aa97el-DivLoginContainer.exd0a430 > form > div.tiktok-1tkbt83-DivEmailContainer.e1419m800 > div > input", self.page)
        moveToPoint(email_position.x, email_position.y, 2)
        pag.click()
        email_prefix = self.email[1].split("@")[0]
        type(email_prefix)
        #pag.write(email_prefix)
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('alt')
        pyautogui.press('q')  
        pyautogui.keyUp('alt')
        pyautogui.keyUp('ctrl')
        type("gmx.com")
        pag.press("tab")

        password_position = await get_position_by_selector("#loginContainer > div.tiktok-aa97el-DivLoginContainer.exd0a430 > form > div.tiktok-15iauzg-DivContainer.e1bi0g3c0 > div > input", self.page)
        moveToPoint(password_position.x, password_position.y, 2)
        pag.click()
        pag.write(self.password)
        pag.press("tab")

        random_position = ScreenPosition(random.randint(490, 750), random.randint(300, 560))
        moveToPoint(random_position.x, random_position.y, 2)
        pag.click()

        code_button_position = await get_position_by_text(CountryCodeButton[self.country].value, self.page)
        moveToPoint(code_button_position.x, code_button_position.y + 10, 2)
        pag.click()

        enter_code_position = await get_position_by_selector("#loginContainer > div.tiktok-aa97el-DivLoginContainer.exd0a430 > form > div:nth-child(8) > div > div > input", self.page)
        moveToPoint(enter_code_position.x, enter_code_position.y, 2)
        pag.click()

        email_interface = GmxTiktokImapInterface(self.email[1], self.email[2])
        start_time = time.time()
        timeout = 30
        while (True):
            code = await email_interface.getCode(self.email[1], self.email[2])
            if(code):
                await asyncio.sleep(random.randint(3, 10))
                type(code)
                pag.press("enter")
                await asyncio.sleep(5)
                break
            else:
                print("No code found, retrying...")
            
            if time.time() - start_time > timeout:             
                break

        set_tt_used_gmx(self.email[0])
        return True
        #next_button_position = await get_position_by_text(CountryNextButton[self.country].value, self.tab)
        #moveToPoint(next_button_position.x, next_button_position.y, 2)
        #pag.click()
        '''
        username_field = await get_position_by_selector(f'[placeholder="{CountryUsernameField[self.country].value}"]', self.page)
        moveToPoint_bezier(username_field.x, username_field.y, 2)
        pag.click()

        pag.write(self.username)
        pag.press("tab")

        #register_button_position = await get_position_by_text(CountryRegisterButton[self.country].value, self.tab)
        register_button_position = await get_position_by_selector('[type="submit"]' ,self.page)
        moveToPoint_bezier(register_button_position.x, register_button_position.y, 2)
        pag.click()
        return True
        '''
    

class EnterUsernameRoutine(Routine):
    def __init__(self, page, email, username, country):
        super().__init__(page, identifier="https://www.tiktok.com/signup/create-username")
        self.email = email
        self.username = username
        self.country = country

    async def executeRoutine(self):
        username_field = await get_position_by_selector(f'[placeholder="{CountryUsernameField[self.country].value}"]', self.page)
        moveToPoint_bezier(username_field.x, username_field.y, 2)
        pag.click()
        pag.write(self.username)
        pag.press("tab")

        #register_button_position = await get_position_by_text(CountryRegisterButton[self.country].value, self.tab)
        register_button_position = await get_position_by_selector('[type="submit"]' ,self.page)
        moveToPoint_bezier(register_button_position.x, register_button_position.y, 2)
        pag.click()
        return True
    

class AddProfileRoutine(Routine):
    def __init__(self, page, username, password, email, country):
        super().__init__(page, identifier=CountryLoggedInUrl[country].value)
        self.username = username
        self.password = password
        self.email = email

    async def executeRoutine(self):
        add_tiktok_account(self.username, self.password, self.email[0])
        return False