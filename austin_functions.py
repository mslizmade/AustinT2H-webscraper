from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def click_when_loads(driver, path_name,time_limit = 100, error_message="website hasn't loaded yet"):
	
	try: #click the "I want to..." button
		element = WebDriverWait(driver, time_limit).until(EC.presence_of_element_located((By.XPATH, path_name)))
		driver.find_element_by_xpath(path_name).click()
	except TimeoutError:
		print(error_message)

def truncwords(words):  
	#turns address into website-compatible address
	newwords = []
	replacer = { 'STREET':'ST','LANE':'LN','AVENUE':'AVE','ROAD':'RD','IH-35':'IH 35',
		'PARKWAY':'PKWY','DRIVE':'DR','BOULEVARD':'BLVD','CIRCLE':'CIR','TRAIL':'TRL'}
	i = 0
	while i< len(words):
		w = words[i].upper()
		if replacer.get(w):
			if w == 'AVENUE' and i != len(words) - 1:
				newwords.append(w)
			else:
				newwords.append(replacer[w])
		else: 
			newwords.append(w)
		i = i + 1
	return newwords

def click_sequence(driver, atx_address):
	
	#"I want to..." button
	path_name = "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div[6]/div/h2/button"	
	click_when_loads(driver, path_name)

	sleep(1)
	#"Find my Council District" button
	path_name = "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div[6]/div/div/div/div/ul[2]/li[1]/button/strong"
	click_when_loads(driver, path_name)

	sleep(1)
	#Input address information and select from drop down menu
	path_name = "//input[@placeholder='Start typing an address']"
	element = WebDriverWait(driver, 120, 1).until(EC.visibility_of_element_located((By.XPATH, path_name)))
	atx_address = truncwords(atx_address.upper().split())
	element.send_keys(" ".join(atx_address))
	sleep(5)
	element.send_keys(Keys.ARROW_DOWN)
	element.send_keys(Keys.ENTER)
	element.send_keys(Keys.TAB)
	element.send_keys(Keys.ENTER)
	
	#Find the district number or send None
	path_name = "//span[2][@style='font-weight: bold']"
	try: 
		element = WebDriverWait(driver,10, 1).until(EC.visibility_of_element_located((By.XPATH, path_name)))
		return driver.find_element_by_xpath(path_name).text
	except TimeoutException:
		return None