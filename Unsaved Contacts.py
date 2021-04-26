# Whatsaap Text Message (Unsaved Numbers)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
time.sleep(3)
input("If logged in press Enter")
numbers = [123456789, 987654321] # Replace this numbers by the numbers you want to send message to sepereated by (,)
message = "Hello this is a test message" # Replace this by the message you want to send
for i in range(len(numbers)):
    driver.get("https://web.whatsapp.com/send?phone={}&text={}".format(numbers[i],message))
    time.sleep(8)
    pyautogui.press("Enter")
