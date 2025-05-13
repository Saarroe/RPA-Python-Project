# RPA-Python-Project
This repository contains a Python automation script using Selenium to solve the RPA Challenge [Input Forms](https://rpachallenge.com/) task.

## Installation and Setup:

All dependencies are defined in the `environment.yml` file. To set up the environment:

<pre>```
conda env create -f environment.yml
conda activate rpa-challenge
``` </pre>

In addition, make sure you have Google Chrome installed.

To run the script:
<pre>```
python .\code\main.py --download_csv --headless
``` </pre>

Or run the main.py in your preferred Python IDE with defaults. 

### Dependencies: 
- **Python 3.11**
- **Selenium 4.32.0**
- **Requests** – for downloading files
- **Pandas** – for handling input data

All dependencies are managed with Conda and listed in environment.yml.

## Design Decisions

All automation logic is implemented in main.py.

There are two parameters, which are implemented as CLI flags for better flexibility and usability using argparse. 

- **download_csv** – Determines whether to download the Excel file or use an existing local copy.
- **headless** – Runs Chrome in headless mode if set to True.

The code automates the form filling task with 100% accuracy. The newest release of Selenium is used to ensure there is no need to manually install the correct version of the Chromedriver. This is handled automatically by Selenium (Manager), which makes the setup process smoother and more reliable. 

It downloads the Excel file by extracting the link from the website and saving the Excel to the downloads/ folder.
Downloading the excel file is implemented in separate function called download_csv_file(), to keep file handling logic isolated from the form automation logic.
The requests library is used to download the file, ensuring that the file is saved properly and efficiently.  

The CLI flags need to be provided to run the code in headless mode or to download the Excel from the site. 
