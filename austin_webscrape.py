from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import austin_functions as AF

"""
user requirements:
chrome and comparable chromedriver installed
chromedriver location replaces DRIVER_PATH variable
"""

print("Chrome errors expected, may ignore")

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.set_page_load_timeout(30)

url = 'https://www.austintexas.gov/GIS/CouncilDistrictMap/'
driver.get(url)

#fh = open("seleniumdata.txt") #full data set
fh = open("seleniumdata_sample.txt")
successful_scrapes = open("atxcouncildistricts.txt", "w") 
errata_check = open("atxcouncildistricts_errata.txt", "w")

for line in fh:
	street_address = line.strip()
	district_result = AF.click_sequence(driver, street_address)
	if district_result:
		print(street_address+', '+district_result, file = successful_scrapes)
		print(street_address+', '+district_result)
	else:
		print(street_address, file = errata_check)
		print(street_address, "not found")