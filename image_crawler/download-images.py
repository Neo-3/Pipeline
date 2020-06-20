import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def download(name, limit):
    images = []
    count = 0

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")

    browser = webdriver.Chrome(options=options, executable_path ="./chromedriver")
    browser.get("https://www.google.com/")

    # search on google
    search = browser.find_elements_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')[0]
    search.send_keys(name, Keys.ENTER)

    # Switch to images
    elem = browser.find_element_by_link_text("Imagens")   
    elem.get_attribute("href")
    elem.click()

    # get images
    for i in range(1,(limit+1)):
        try:
            images.append(browser.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div["+str(i)+"]/a[1]/div[1]/img"))
        except: 
            # scroll the page
            browser.execute_script("scrollBy(0,"+ str(1000) +");")

    # Create download folder
    try:
        os.mkdir("downloads")
    except FileExistsError:
        pass
    
    file_name = name.replace(" ", "_")
    for image in images:
        src = image.get_attribute('src')
        if src != None:
            try:
                count+=1
                urllib.request.urlretrieve(str(src), os.path.join('downloads', file_name+str(count)+'.jpg'))
            except:
                print('fail')

download("Medidor de energia analogico", 500)