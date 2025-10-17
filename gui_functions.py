import pyautogui
import os
import webbrowser
import random
import math
import time
import numpy as np
import zendriver as zd
import asyncio
from oxymouse import OxyMouse

sqrt3 = np.sqrt(3)
sqrt5 = np.sqrt(5)

source_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_path = r"C:\Programme\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

timeOffsetLowerBound = 0.000648996353149414
timeOffsetUpperBound = 0.02896112442016602

maxX = 1901
maxY = 998

class ScreenPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def moveToPoint_bezier(dest_x, dest_y, overshoot_distance=2):
    mouse = OxyMouse(algorithm="bezier")
    start_x, start_y = pyautogui.position()
    dx = dest_x - start_x
    dy = dest_y - start_y
    overshoot_x = dest_x + int(dx * 0.1) + random.randint(-overshoot_distance, overshoot_distance)
    overshoot_y = dest_y + int(dy * 0.1) + random.randint(-overshoot_distance, overshoot_distance)

    overshoot_path = mouse.generate_coordinates(int(start_x), int(start_y), int(overshoot_x), int(overshoot_y))
    settle_path = mouse.generate_coordinates(int(overshoot_x), int(overshoot_y), int(dest_x), int(dest_y))

    def move_path(path, min_delay=0.001, max_delay=0.008, skip_rate=2):
        total_points = len(path)
        for i, (x, y) in enumerate(path[::skip_rate]):
            progress = i / (total_points // skip_rate)

            speed_factor = progress * progress * (3 - 2 * progress)
            delay = min_delay + (max_delay - min_delay) * (1 - speed_factor)
            if i % 5 == 0:
                jitter_x = x + random.uniform(-0.5, 0.5)
                jitter_y = y + random.uniform(-0.5, 0.5)
            else:
                jitter_x, jitter_y = x, y
            pyautogui.moveTo(jitter_x, jitter_y)
            time.sleep(delay)

    move_path(overshoot_path, skip_rate=3)
    time.sleep(random.uniform(0.03, 0.08))
    move_path(settle_path, skip_rate=2, min_delay=0.001, max_delay=0.005)
 



def perlin_mouse_move(x_min, y_min, x_max, y_max, moves = 2, skip_rate = 3):
    mouse = OxyMouse(algorithm="perlin")
    start_x, start_y = pyautogui.position()

    for _ in range(moves):
        target_x = random.randint(x_min, x_max)
        target_y = random.randint(y_min, y_max)

        raw_path = mouse.generate_coordinates(int(start_x), int(start_y), int(target_x), int(target_y))
        path = raw_path[::skip_rate]

        move_duration = random.uniform(0.2, 0.8)
        delay = move_duration / max(1, len(path))

        for x, y in path:
            pyautogui.moveTo(x, y)
            time.sleep(delay)

        start_x, start_y = path[-1]
        time.sleep(random.uniform(0.1, 0.3))


def smooth_path(path, smooth_factor=5):
    """Downsample and smooth a raw path"""
    path = path[::smooth_factor]  # skip points
    smoothed = []
    for i in range(len(path)-1):
        x1, y1 = path[i]
        x2, y2 = path[i+1]
        # simple linear interpolation for smoother glide
        steps = max(2, int(np.hypot(x2-x1, y2-y1)))
        for t in np.linspace(0, 1, steps):
            smoothed.append((int(x1 + (x2-x1)*t), int(y1 + (y2-y1)*t)))
    return smoothed



def moveToPoint(dest_x, dest_y, speed):
    start_x = pyautogui.position().x
    start_y = pyautogui.position().y

    G_0=9
    W_0=3
    M_0=15
    D_0=12
    points = []

    current_x,current_y = start_x,start_y
    v_x = v_y = W_x = W_y = 0
    while (dist:=np.hypot(dest_x-start_x,dest_y-start_y)) >= 1:
        W_mag = min(W_0, dist)
        if dist >= D_0:
            W_x = W_x/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
            W_y = W_y/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
        else:
            W_x /= sqrt3
            W_y /= sqrt3
            if M_0 < 3:
                M_0 = np.random.random()*3 + 3
            else:
                M_0 /= sqrt5
        v_x += W_x + G_0*(dest_x-start_x)/dist
        v_y += W_y + G_0*(dest_y-start_y)/dist
        v_mag = np.hypot(v_x, v_y)
        if v_mag > M_0:
            v_clip = M_0/2 + np.random.random()*M_0/2
            v_x = (v_x/v_mag) * v_clip
            v_y = (v_y/v_mag) * v_clip
        dynamic_speed = speed * min(1.0, dist / D_0)  # D_0 is your decay threshold
        start_x += dynamic_speed*v_x
        start_y += dynamic_speed*v_y
        move_x = int(np.round(start_x))
        move_y = int(np.round(start_y))
        if current_x != move_x or current_y != move_y:
            #move_mouse(current_x:=move_x,current_y:=move_y)
            points.append([move_x, move_y])

    for i, point in enumerate(points):
        pyautogui.moveTo(point[0], point[1], duration=random.uniform(1/(1000*speed), 1/(100*speed)))


def generateTimeOffset():
    return random.uniform(timeOffsetLowerBound, timeOffsetUpperBound)



def randomMouseMovement(targetX, targetY):
    num_points = random.randint(2, 5)

    startX = pyautogui.position().x
    startY = pyautogui.position().y
    newX = 0
    newY = 0
    for i in range(num_points):
        if (i == num_points - 1):
            moveToPoint(targetX, targetY, 4)
        else:
            newX = random.randint(0, maxX)
            newY = random.randint(0, maxY)
            moveToPoint(newX, newY, 4)
            startX = newX
            startY = newY


'''
async def get_position_by_selector(text, tab):
    start_time = time.time()
    while time.time() - start_time < 30:
        try:
            element = await tab.select(text, timeout=2)
            if element:
                try:
                    position = await element.get_position(abs=False)
                    return ScreenPosition((position.x + 35) + position.width / 2, (position.y + 85) + position.height / 2)
                except:
                    print("could not find position")
        except Exception:
            pass
        await asyncio.sleep(0.5)
    raise TimeoutError(f"Timeout waiting for selector: {text}")
'''




async def get_position_by_selector(selector, page):
    start_time = time.time()
    
    while time.time() - start_time < 30:
        try:
            element = page.locator(selector).first
            await element.wait_for(state="attached", timeout=1000)
            if element:
                try:
                    box = await element.bounding_box()
                    if box:
                        x = (box['x']) + box['width'] / 2
                        y = (box['y'] + 50) + box['height'] / 2
                        return ScreenPosition(x, y)
                    else:
                        print("could not find position")
                except Exception as e:
                    print(f"could not find position: {e}")
        except Exception:
            pass
        time.sleep(0.5)
    raise TimeoutError(f"Timeout waiting for selector: {selector}")


async def get_position_by_selector_exact(text, tab):
    start_time = time.time()
    while time.time() - start_time < 20:
        try:
            element = await tab.select(text, timeout=2)
            if element:
             
                try:
                    position = await element.get_position(abs=False)
                    return ScreenPosition((position.x), (position.y))
                except:
                    print("could not find position")
        except Exception:
            pass
        await asyncio.sleep(0.5)

    raise TimeoutError(f"Timeout waiting for selector: {text}")



'''
async def get_position_by_text(text, tab):
    await asyncio.sleep(3)
    try:
        element = await tab.find_element_by_text(text, best_match=True)
        if not element:
            return
    except:
        return
    position = await element.get_position(abs=False)
    return ScreenPosition((position.x + 35) + position.width / 2, (position.y + 85) + position.height / 2)
'''


async def get_position_by_text(text, page):
    await asyncio.sleep(3)  # Changed from time.sleep
    
    try:
        element = page.get_by_text(text, exact=False).first
        if not await element.is_visible():
            return None
            
    except Exception:
        return None
    
    box = await element.bounding_box()
    
    if not box:
        return None
    
    x = (box['x'] + 35) + box['width'] / 2
    y = (box['y'] + 40) + box['height'] / 2
    
    return ScreenPosition(x, y)


async def wait_for_selector(tab, selector, timeout=30, poll_interval=0.5):
    await tab.wait_for_ready_state("complete", timeout=30)
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            element = await tab.select(selector)
            if element:
                return element
        except Exception:
            pass
        await asyncio.sleep(poll_interval)

    raise TimeoutError(f"Timeout waiting for selector: {selector}")



async def is_element_on_page(selector, tab):
    #await tab.wait_for_ready_state("complete", timeout=10)
    await asyncio.sleep(1)
    try:
        element = await tab.select(selector, timeout = 5)
        if element:
            "found element on page"
            return True
        else:
            "could not find element on page"
            return False
    except:
        "exception finding element"
        return False



def click(x, y):
    events = []
    return events


def scrollDown(num_scrolls):
    for _ in range(num_scrolls):
        pyautogui.scroll(-100)
        time.sleep(random.uniform(0.09, 0.4))


def pauseAt():
    pyautogui.sleep(random.uniform(0.1, 3))

def type(text):
    for char in text:
        if random.random() < 0.02 and char.isalpha():
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
            pyautogui.write(wrong_char)
            time.sleep(random.uniform(0.1, 0.25))
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.15))
        pyautogui.write(char)
        time.sleep(get_typing_delay(char))



def get_typing_delay(char):
    if char in ' .,;:-':
        return random.uniform(0.05, 0.15)
    elif char in '!@#$%^&*()_+{}[]<>?|':
        return random.uniform(0.15, 0.35)
    elif char.isupper():
        return random.uniform(0.15, 0.3)
    else:
        return random.uniform(0.07, 0.2)


def maybe_make_typo(char):
    if random.random() < 0.02:  # 2% chance of typo
        wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
        pyautogui.write(wrong_char)
        time.sleep(random.uniform(0.1, 0.25))
        pyautogui.press('backspace')
        time.sleep(random.uniform(0.1, 0.2))
