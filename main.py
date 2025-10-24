from camoufox.sync_api import Camoufox
import asyncio
import time
from proxy import *
from helper import *
from gui_functions import *
from country_values_tt import *
from tiktok_routines import *
from routine import *
import pyautogui as pag
from camoufox import AsyncCamoufox
import asyncio
import multiprocessing



WINDOWS_FONT_POOL = [
    "Arial", "Calibri", "Cambria", "Candara", "Consolas", "Courier New",
    "Georgia", "Helvetica", "Impact", "Lucida Sans Unicode", "Palatino Linotype",
    "Segoe UI", "Tahoma", "Times New Roman", "Trebuchet MS", "Verdana",
    "Roboto", "Noto Sans", "Segoe UI Emoji",
    "Corbel", "Constantia", "Ebrima", "Leelawadee UI", "Malgun Gothic",
    "Microsoft YaHei", "Microsoft JhengHei", "SimSun", "Yu Gothic UI", "Meiryo UI",
    "Lucida Console", "Cascadia Mono", "Comic Sans MS", "Book Antiqua", "Century Gothic",
    "Franklin Gothic Medium", "Gill Sans MT", "Calibri Light", "Nirmala UI",
    "Segoe Script", "Segoe Print", "Arial Black", "Arial Unicode MS", "Myanmar Text"
]

USER_AGENTS_FIREFOX = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"

]

LANG_PRESETS = [
    #{"locale": "de-DE,en-US", "languages": ["de-DE", "de"], "accept_language": "de-DE,de;q=0.9"},
    {"locale": "de-DE", "languages": ["de-DE", "de"], "accept_language": "de-DE,de;q=0.9"},
    {"locale": "de-DE", "languages": ["de-DE", "en-US", "de"], "accept_language": "de-DE,de;q=0.9,en-US;q=0.8"},
    #{"locale": "en-US", "languages": ["en-US", "de-DE"], "accept_language": "en-US,en;q=0.9,de-DE;q=0.8"},
    #{"locale": "de-DE", "languages": ["de-DE", "en-GB", "en"], "accept_language": "de-DE,en-GB;q=0.9,en;q=0.8"},
]

LANG_PRESETS_PL = [
    {"locale": "pl-PL", "languages": ["pl-PL", "pl"], "accept_language": "pl-PL,pl;q=0.9"},
    {"locale": "pl-PL", "languages": ["pl-PL", "pl", "en-US"], "accept_language": "pl-PL,pl;q=0.9,en-US;q=0.8"},
]


COMMON_WINDOWS = [
    (1920,1080),
    (1600,900),
    (1440,900),
    (1366,1050),
    (1920,1050),
]

COUNTRIES = [
    "GERMANY",
    "POLAND",
    #"SPAIN",
    "GREECE",
    #"FRANCE",
    "ITALY",
    "BULGARIA",
    #"NETHERLANDS",
    "SWEDEN",
    "ROMANIA",
    "CZECH",
    "FINLAND"
]


def random_lang():
    return random.choice(LANG_PRESETS_PL)


def random_font_list(pool):
    n = random.randint(7, 12)
    return random.sample(pool, n)


async def main():
    country = random.choice(COUNTRIES)
    lang_presets = CountryLanguageSettings[country].value
    proxyProvider = RayobyteProxy(country)
    ua = random.choice(USER_AGENTS_FIREFOX)
    lang_cfg = random.choice(lang_presets)
    fonts = random_font_list(CountryFonts[country].value)
    sample_rate = random.choice([44100, 48000])
    window_size=random.choice(COMMON_WINDOWS)
    
    print("Session fingerprint preview:")
    print(" UA:", ua)
    print(" Locale:", lang_cfg["locale"])
    print(" Accept-Language:", lang_cfg["accept_language"])
    print(" Fonts:", fonts)
    print(" Window:", window_size)

    async with AsyncCamoufox(
        geoip=True,
        headless=False,
        os="windows",
        locale=lang_cfg["locale"],
        block_webrtc=True,
        fonts=fonts,
        window=window_size,
        i_know_what_im_doing=True,
        proxy={
            'server': proxyProvider.getProxy(),
            'username': proxyProvider.getUsername(),
            'password': proxyProvider.getPassword()
        },
        config={
            "navigator.userAgent": ua,
            "navigator.languages": lang_cfg["languages"],
            "headers.Accept-Language": lang_cfg["accept_language"]
        }
    ) as browser:
        
        name = generateName()
        email = get_gmx_tt()
        username = generateEmail(name[0], name[1], 2)
        password = generate_password()
        page = await browser.new_page()
        

        routines = [EnterEmailRoutine(page, country), 
                    EnterDetailsRoutine(page, email, country, password, username), 
                    EnterUsernameRoutine(page, email, username, country),
                    AddProfileRoutine(page, username, password, email, country)]

        await page.goto("https://tiktok.com/signup")


        current_url = page.url
        restart = False

        while True:
            for routine in routines:
                if routine.identifier == current_url:
                    print("found a routine")
                    #print(routine.identifier)
                    result = await routine.executeRoutine()
                    if not result:
                        print("result was false")
                        restart=True
                        break
                    try:
                        current_url = await wait_for_url(page, current_url)
                        print("the current url is")
                        print(current_url)
                        break
                    except:
                        print("wait for url timeout")
                        restart = True
                        break        
            else:
                print("no routine found")
                break
            if restart:
                print("restarting")
                await page.close()
                break

        return



async def main_loop():
    while True:
        await main()
        print("Browser closed. Restarting...")
        
if __name__ == "__main__":
    asyncio.run(main_loop())
