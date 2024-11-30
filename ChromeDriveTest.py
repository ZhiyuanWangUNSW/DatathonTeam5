# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:38:59 2024

@author: os
"""
#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#%%
# Path to ChromeDriver
service = Service("C:\\Tools\\chromedriver.exe")  # Use your path here
#%%
# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode if you don’t need a visible browser
driver = webdriver.Chrome(service=service, options=options)
#%%
# Test ChromeDriver
driver.get("https://www.google.com")
print("Page Title:", driver.title)  # Should print: "Google"
#%%
# Close the driver
driver.quit()
