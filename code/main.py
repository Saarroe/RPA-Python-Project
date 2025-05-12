# import necessary libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

def download_csv_file(chrome_options):
    """
    This function downloads the CSV file from the website.
    """
    # Open web browser and navigate to the website
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://rpachallenge.com/")

    # Find the "Download Excel" button and the link to the file
    download_button = driver.find_element(By.XPATH, '//a[contains(text(),"Download Excel")]')
    download_url = download_button.get_attribute('href')

    # Quit the session
    driver.quit()

    # Create a directory to save the downloaded file
    current_wd = os.getcwd()
    #print(f"Current Working Directory: {current_wd}")
    download_folder = os.path.join(current_wd, "downloads")
    #print(f"Download Folder: {download_folder}")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Define file path and name
    file_path = os.path.join(download_folder, "rpa_challenge.xlsx")

    # Download the file
    response = requests.get(download_url)
    response.raise_for_status()  # Raise error for bad status codes

    # Save the file to the specified path
    with open(file_path, "wb") as f:
        f.write(response.content)
        
    #print(f"File downloaded successfully to: {file_path}")
    return pd.read_excel(file_path)

def main(download_csv=True, headless=True):
    """
    This script automates the process of filling out a web form using data from an Excel file.
    download_csv: bool, if True, download the CSV file from the website.
    """
    # Set up Chrome options
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    
    # If the flag is set to False, check if the file exists and load it
    if not download_csv:
        # Check if the file exists
        if not os.path.exists('challenge.xlsx'):
            print("File not found.")
            return
        else:
            # Load the CSV file
            df = pd.read_excel('challenge.xlsx')
            df.columns = df.columns.str.strip()
            #print(df.head())
            #print(df.shape) # Shape of the DataFrame 10,7 so 10 rows:
    else: 
        # Download the CSV file if the flag is set
        df=download_csv_file(chrome_options)
        df.columns = df.columns.str.strip()

    # Open web browser and navigate to the website
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://rpachallenge.com/")

    # Find the "Start" button and click it
    start_button = driver.find_element(By.XPATH, '//button[text()="Start"]')
    start_button.click()

    # Loop through the rows of the DataFrame
    for index, row in df.iterrows():
        #print(f"Filling row {index + 1}")
        for column, value in row.items():
            #print(f"Filling {column} with {value}")

            # Find the input field for the current column
            input_field = driver.find_element(By.XPATH, f'//label[text()="{column}"]//following-sibling::input')
            
            # Clear the input field and enter the value
            input_field.clear()
            input_field.send_keys(value)

        # Press the submit button
        submit_button = driver.find_element(By.XPATH, '//input[@value="Submit"]')
        submit_button.click()
        
    if headless:
        congratulations_message = driver.find_element(By.CLASS_NAME, "message1").text
        success_rate_message = driver.find_element(By.CLASS_NAME, "message2").text
        # Print or check if the success message exists
        print(congratulations_message)  
        print(success_rate_message)  

    time.sleep(30)
    driver.quit()
    

if __name__ == "__main__":
    main(download_csv=True, headless=True)