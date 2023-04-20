from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs 
import time  
import csv 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
url = "https://scholar.google.com/citations?view_op=view_org&org=4770128543809686866&hl=en&oi=io"
driver.get(url)

profiles_umich = []

i=0
while True:
    soup = bs(driver.page_source, "html.parser")
    #find all h3 header with a class that identifies each profile/name 
    names = soup.find_all("h3", class_="gs_ai_name")
    for name in names:
        link = name.find("a")["href"] #pulls links for each profile on the page including the image and name
        if "user" in link:
            #check that link is not already in the user_links list (prevents duplication created from having both image and name)
            if link not in profiles_umich:
                print(link)
                profiles_umich.append(link) #add the profile link
                name_text = name.text.strip() #grab the name associated with the profile link
                #save link and name to csv file
                with open("profiles_umich.csv", mode="a", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([link, name_text])
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Next"]')))
    try:
        next_button.click()
    except:
        break
    time.sleep(2)

driver.quit()

