from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




def login(browser):
	browser.get("https://www.instagram.com/?hl-=es")
	time.sleep(2)
	username = browser.find_element_by_css_selector("[name='username']")
	password = browser.find_element_by_css_selector("[name='password']")
	login = browser.find_element_by_css_selector("button")
	username.send_keys("lismar_carolina")
	password.send_keys("miclave")
	login.click()

	time.sleep(24)

def main():
	browser = webdriver.Chrome(executable_path='C:\\Users\\camac\\chromedriver.exe')
	
	login(browser)

main()
