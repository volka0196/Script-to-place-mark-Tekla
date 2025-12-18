import pytesseract      # type: ignore
import pyautogui        # type: ignore
import re
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

region = (500, 0, 1000, 30)
screen = pyautogui.screenshot(region=region)
text = pytesseract.image_to_string(screen)
if mark := re.search(r"\[(.+)_\[(.+)\]\]", text, re.IGNORECASE):
    current_time = time.strftime("%H.%M.%S", time.localtime())
    with open(f"{current_time}_mark_list-.txt", "a") as file:
        file.write(f"{mark.group(2).replace(".","-")}\n")

    with open(f"{current_time}_mark_list..txt", "a") as file:
        file.write(f"{mark.group(2)}\n")

    print(mark.group(2).replace(".","-"))
    print(mark.group(2))
else:
    print("No mark found")


#   C:\TeklaStructuresModels\GCC-SOX-DDD-13260-15-2100-KMD3-MOD-01001.01 -[A_[B.1]]
