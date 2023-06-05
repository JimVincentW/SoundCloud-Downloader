import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver



# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser

def download_soundcloud_links(file_path):
    # Read the links from the text file
    with open(file_path, 'r') as f:
        links = [line.strip() for line in f.readlines()]

    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser

    for link in links:
        try:
            driver.get('https://www.klickaud.co/')
            
            # Find the input field and enter the link
            input_field = driver.find_element(By.CSS_SELECTOR, '#header > div > div > div.content > form > input[type=text]:nth-child(1)')
            input_field.clear()
            input_field.send_keys(link)

            time.sleep(5)

            # Wait for the submit button to be clickable and click it
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/section/div/div/div[1]/form/input[3]'))
            )
            submit_button.click()

            # wait
            time.sleep(5)

            # Click the download button
            download_button = driver.find_element(By.XPATH, '/html/body/section/div/div/div[1]/div/div[3]/table/tbody/tr/td[1]/div/div')
            download_button.click()

            # Wait for the download link to appear
            time.sleep(5)  # Adjust the sleep time based on your internet speed
        except Exception as e:
            print("An error occurred, skipping the current link:", e)
            continue

    # Close the browser window
    driver.quit()

# Call the function with the path to your text file containing the links
download_soundcloud_links('links.txt')
