from lxml import html
import requests
import webbrowser as wb
from tkinter import messagebox as tkMessageBox

# page = requests.get('http://femc.gehealthcare.com/femc/partorder/orderParts.do?fromPage=main')
# tree = html.fromstring(page.content)
#
# wb.open_new_tab('http://femc.gehealthcare.com/femc/partorder/orderParts.do?fromPage=main')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




username = "212668889"
password = "tRUE08bLUE"
partNumber = "5499513"

chrome_options = Options()
chrome_options.add_argument("--headless")

#driver = webdriver.Chrome()
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
driver.get("http://femc.gehealthcare.com/femc/main")





element = driver.find_element_by_id("username")
element.send_keys(username)
element = driver.find_element_by_id("password")
element.send_keys(password)

try:
    element.send_keys(Keys.RETURN)
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

#element = driver.find_element_by_name("format")
#print(element.text)
#
driver.get("http://femc.gehealthcare.com/femc/partorder/orderParts.do?fromPage=main")
element = driver.find_element_by_name("partId")
element.send_keys(partNumber)

try:
    element.send_keys(Keys.RETURN)
    print("PN is ready!")
except TimeoutException:
    print("Loading took too much time!")

try:
    element = driver.find_element_by_class_name("ui-dialog-buttonset")
    element.click()
    #element.send_keys(Keys.RETURN)
    # if driver.find_element_by_id("cru-message"):
    #     try:
    #         button = driver.find_element_by_
    #     element.send_keys(Keys.RETURN)
    #     element = driver.find_element_by_id("cru-message")
    #     element.send_keys(Keys.RETURN)
except TimeoutException:
    print("Loading took too much time!")

   # element.send_keys(Keys.RETURN)
    #element = driver.find_element_by_id("cru-message")
#     element.send_keys(Keys.RETURN)
#     print("CRU is ready!")

#element.send_keys(partNumber)

partInfo =  driver.find_element_by_name("partInfo")
partInfoText = partInfo.text

statusStartIndex = partInfoText.find('Status')
statusEndIndex = partInfoText.find('Buy')

descriptionStartIndex = partInfoText.find('Description')
descriptionEndIndex = partInfoText.find('FRU')

partNumberStartIndex = partInfoText.find('Part #')
partNumberEndIndex = partInfoText.find('Part Type:')

wrhsStartIndex = partInfoText.find('Wrhse')
wrhsEndIndex = partInfoText.find('===')

partNumber = partInfoText[partNumberStartIndex:partNumberEndIndex]
partDescription = partInfoText[descriptionStartIndex:descriptionEndIndex]
partStatus = partInfoText[statusStartIndex:statusEndIndex]
partWrhs = partInfoText[wrhsStartIndex:wrhsEndIndex]

fullPartInfo = partNumber + partDescription + partStatus + partWrhs

# print(partInfoText[partNumberStartIndex:partNumberEndIndex-1])
# print(partInfoText[descriptionStartIndex:descriptionEndIndex-1])
# print(partInfoText[statusStartIndex:statusEndIndex-1])
# print(partInfoText[wrhsStartIndex:wrhsEndIndex-1])

tkMessageBox.showinfo(title="Full part information", message=fullPartInfo)
