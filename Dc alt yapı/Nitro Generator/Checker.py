import time
import webbrowser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import *
from tkinter.filedialog import askopenfile

print (">>> Discord Nitro Code Checker <<< ")
print (">>> Made by Atlas | Nulled.to <<< ")
webbrowser.open('https://www.nulled.to/user/1229709-atlas')

driver = webdriver.Chrome("C:/chromedriver.exe");
xPath = """//*[@id="app-mount"]/div[1]/div/div[2]/div/section/div/div[1]"""
count = 0
might = 0
attempts = 0

file = askopenfile(filetypes=[("Text files","*.txt")])
codes = file.readlines()
						             
for code in codes:
	print(attempts)
	attempts += 1
	driver.get("http://discord.gift/" + code)
	time.sleep(2)
	try:
		texter = driver.find_element_by_xpath(xPath)
	except NoSuchElementException:
		print ("Might be Valid \n \n \n \n %s - @Atlas - \n \n \n \n" % code)
		might += 1
		continue
	if(texter.text == "Gift Code Invalid"):
		print("Might: %d | Invalid: %d" % (might, attempts))
time.sleep(3);
print("\n\tMight: %d \n\t Invalids: %d" % (might, attempts))
driver.close()
input('Finished')
