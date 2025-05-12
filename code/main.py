# import necessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# Open web browser and navigate to the website
driver = webdriver.Chrome()
driver.get("https://rpachallenge.com/")
print(driver.title)

# Find the "Start" button and click it
start_button = driver.find_element(By.XPATH, '//button[text()="Start"]')
start_button.click()

# Find the column headers and fill the input fields
#input1 = driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelAddress"]')
input1 = driver.find_element(By.XPATH, '//label[text()="Address"]//following-sibling::input')
input1.send_keys("Test address")

time.sleep(5)
driver.quit()


# Load the CSV file
df = pd.read_excel('challenge.xlsx')
print(df.head())

