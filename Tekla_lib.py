import re
import json
import time
import pyautogui        # type: ignore
import pytesseract      # type: ignore


def load_config():
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("config.json not found")
        exit(1)


config = load_config()


def locate_png():
    try:
        return pyautogui.locateOnScreen("mark.png", confidence=0.9)
    except pyautogui.ImageNotFoundException:
        return None


def locate_center():
    locate = locate_png()
    if locate:
        center_png = pyautogui.center(locate)
        pyautogui.moveTo(center_png)
    else: print("not found")


def find_pixel():
    search = config["search"]
    color = config["color"]

    print("Started searching...")
    screenshot = pyautogui.screenshot()
    pixel = screenshot.load()
    width, height = screenshot.size
    for x in range(width - search["start_x"], search["end_x"], search["step"]):
        for y in range(height - search["start_y"], search["end_y"], search["step"]):
            r, g, b = pixel[x, y]
            if r == color["red"] and g == color["green"] and b == color["blue"]:
                print(f"Found at: {x, y}")
                return x, y
    return None

def to_integer():
    while True:
        try:
            return int(input().strip())
        except ValueError:
            print("only integer")