# import necessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)
time.sleep(5)
driver.quit()


# Load the CSV file
df = pd.read_excel('challenge.xlsx')
print(df.head())

