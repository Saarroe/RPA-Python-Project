# import necessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


def main():
    # Load the CSV file
    df = pd.read_excel('challenge.xlsx')
    df.columns = df.columns.str.strip()
    print(df.head())
    print(df.shape) # Shape of the DataFrame 10,7 so 10 rows:
    
    # Open web browser and navigate to the website
    driver = webdriver.Chrome()
    driver.get("https://rpachallenge.com/")

    # Find the "Start" button and click it
    start_button = driver.find_element(By.XPATH, '//button[text()="Start"]')
    start_button.click()



    # Loop through the rows of the DataFrame
    for index, row in df.iterrows():
        print(f"Filling row {index + 1}")
        for column, value in row.items():
            print(f"Filling {column} with {value}")

            # Find the input field for the current column
            input_field = driver.find_element(By.XPATH, f'//label[text()="{column}"]//following-sibling::input')
            
            # Clear the input field and enter the value
            input_field.clear()
            input_field.send_keys(value)

        # Press the submit button
        submit_button = driver.find_element(By.XPATH, '//input[@value="Submit"]')
        submit_button.click()

    time.sleep(5)
    driver.quit()



if __name__ == "__main__":
    main()