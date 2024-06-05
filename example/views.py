# example/views.py
from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_tweet_heads():
    heads = []
# User credentials
    id = '9625401776'  # Enter phonenumber, email, or username
    password = 'mayjon1372'  # Enter password

    # Create instance of Chrome webdriver
    chromedriverpath = ChromeDriverManager().install()
    options = Options()
    driver = webdriver.Chrome(service=Service(chromedriverpath), options=options)
    driver.get("https://x.com/i/flow/login")
    driver.maximize_window()
    time.sleep(5)

    # Perform login
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').click()
    time.sleep(5)

    # Locate parent element
    parent_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/section/div/div/div[3]')
    ))

    # Locate innermost span elements
    innermost_spans = parent_element.find_elements(By.XPATH, './/span[not(.//span)]')

    # Print text of each innermost span element
    print(innermost_spans[1].text)
    heads.append(innermost_spans[1].text)
    # Locate parent element
    parent_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/section/div/div/div[4]')
    ))
    # Locate innermost span elements
    innermost_spans = parent_element.find_elements(By.XPATH, './/span[not(.//span)]')

    # Print text of each innermost span element
    print(innermost_spans[1].text)
    heads.append(innermost_spans[1].text)

    # Locate parent element
    parent_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/section/div/div/div[5]')
    ))
    # Locate innermost span elements
    innermost_spans = parent_element.find_elements(By.XPATH, './/span[not(.//span)]')

    # Print text of each innermost span element
    print(innermost_spans[1].text)  
    heads.append(innermost_spans[1].text)

    # Locate parent element
    parent_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/section/div/div/div[6]')
    ))
    # Locate innermost span elements
    innermost_spans = parent_element.find_elements(By.XPATH, './/span[not(.//span)]')

    # Print text of each innermost span element
    print(innermost_spans[1].text)
    heads.append(innermost_spans[1].text)

    # Locate parent element
    parent_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/div/section/div/div/div[7]')
    ))
    # Locate innermost span elements
    innermost_spans = parent_element.find_elements(By.XPATH, './/span[not(.//span)]')

    # Print text of each innermost span element
    print(innermost_spans[1].text)
    heads.append(innermost_spans[1].text)

    # Close the browser
    driver.quit()
    return heads
    




def index(request):
    now = datetime.now()
    heads = get_tweet_heads()
    # heads = ['Head 1', 'Head 2', 'Head 3', 'Head 4', 'Head 5']
    return render(request, "twitter.html", {
        'head1': heads[0],
        'head2': heads[1],
        'head3': heads[2],
        'head4': heads[3],
        'head5': heads[4]
    })
    