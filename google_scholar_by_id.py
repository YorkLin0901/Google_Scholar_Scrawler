from lxml import etree
from selenium import webdriver
import json
from selenium.webdriver.support.select import Select
from scholarly import scholarly
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import csv
import os.path
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
def parse(html,ids,name):
    citation = html.xpath('//*[@id="gsc_rsb_st"]/tbody/tr[1]/td[2]/text()')
    h_index = html.xpath('//*[@id="gsc_rsb_st"]/tbody/tr[2]/td[2]/text()')
    i10_index = html.xpath('//*[@id="gsc_rsb_st"]/tbody/tr[3]/td[2]/text()')
    total_publication = len(html.xpath('//*[@id="gsc_a_b"]/tr'))
    table_len = len(html.xpath('//*[@id="gsc_rsb_cit"]/div/div[3]/div/span'))
    dict_table_len = 17
    table_dict  = {str(k):0 for k in range(2024 - dict_table_len,2024)[::-1]}
    update_dict = {}
    for i in range(1,table_len+1):#//*[@id="gsc_rsb_cit"]/div/div[3]/div/span[1]
        try:
            update_dict[html.xpath(f'//*[@id="gsc_rsb_cit"]/div/div[3]/div/span[{i}]/text()')[0]]=int(html.xpath(f'//*[@id="gsc_rsb_cit"]/div/div[3]/div/a[{i}]/span/text()')[0])
        except:
            pass
    table_dict  = {k:update_dict.get(k,0) for k,v in table_dict.items()}
    # table_dict.update(update_dict) #//*[@id="gsc_rsb_cit"]/div/div[3]/div/a[1]/span

    print(ids)
    dict = {"name":name,"id":ids,"citation":int(citation[0]),"h_index":int(h_index[0]),"i10_index":int(i10_index[0]),"total_publication":total_publication}
    dict.update(table_dict)
    return dict


def get_scholar_data(name="Bradley F Carlson",ids='1eZFEYQAAAAJ'):
    path = f"htmls/{ids}.html"
    if not os.path.isfile(path):
        url=f'https://scholar.google.com/citations?user={ids}&hl=en'
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        html = etree.HTML(driver.page_source)
        button = driver.find_element('xpath','//*[@id="gsc_bpf_more"]')
        while button.is_enabled():
            ActionChains(driver).click(button).perform()
            html = etree.HTML(driver.page_source)
            time.sleep(5)
            button = driver.find_element('xpath','//*[@id="gsc_bpf_more"]')
            Html_file= open(path,"w+")
            Html_file.write(driver.page_source)
            Html_file.close()

            time.sleep(3)
            html = etree.HTML(driver.page_source)
    else:
        HtmlFile = open(path, 'r', encoding='utf-8')
        html = etree.HTML(HtmlFile.read())
    return parse(html,ids,name)

if __name__ == '__main__':
    lis = []
    while True:
        id = input('type in the scholar id: ')
        name = input('type in the scholar name: ')
        if id != "finish":
            try:
                res = get_scholar_data(ids=id,name=name)
                print(res)
                lis.append(res)
            except:
                pass
        else:
            break
    with open("google_scholar_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(lis[0].keys())
        for res in lis:
            writer.writerow(res.values())

            