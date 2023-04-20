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
import pandas as pd
from google_scholar_by_id import get_scholar_data
from google_scholar_by_id import parse
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")

scholar_id_list = pd.read_csv('/Users/linyukai/Downloads/profiles_umich.csv',names=['url','name'])
scholar_id_dict = scholar_id_list.to_dict()
lis=[]
for i in range(100):
    url = scholar_id_dict['url'][i]
    y = scholar_id_dict['name'][i] # name
    print(y)
    x = url.split('=')[-1]
    print(x)
    try:
        res = get_scholar_data(ids=x,name=y)
        print(res)
        lis.append(res)
    except:
        pass
with open("google_scholar_data_id.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(lis[0].keys())
    for res in lis:
        writer.writerow(res.values())


import numpy as np
avg_citation = np.mean([x['citation'] for x in lis])
avg_h_index = np.mean([x['h_index'] for x in lis])
avg_i10_index = np.mean([x['i10_index'] for x in lis])
avg_total_publication = np.mean([x['total_publication'] for x in lis])


class TreeNode:
    def __init__(self, content=None, value=None):
        self.content = content
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(content='Are those authors have their citation above the average?',value=avg_citation)
root.left = TreeNode(content='Are those authors have their h_index above the average?',value=avg_h_index)
root.right = TreeNode(content='Are those authors have their h_index above the average?',value=avg_h_index)
root.left.left = TreeNode(content='Are those authors have their total_publication above the average?',value=avg_total_publication)
root.left.right = TreeNode(content='Are those authors have their total_publication above the average?',value=avg_total_publication)
root.right.left = TreeNode(content='Are those authors have their total_publication above the average?',value=avg_total_publication)
root.right.right = TreeNode(content='Are those authors have their total_publication above the average?',value=avg_total_publication)

root.left.left.left = TreeNode(content=[])
root.left.left.right = TreeNode(content=[])
root.left.right.left = TreeNode(content=[])
root.left.right.right = TreeNode(content=[])
root.right.left.left = TreeNode(content=[])
root.right.left.right = TreeNode(content=[])
root.right.right.left = TreeNode(content=[])
root.right.right.right = TreeNode(content=[])


for data in lis:
    node = root
    while node.right is not None:
        if data[node.content.split(' ')[5]] > node.value:
            node = node.right
        else:
            node = node.left
    node.content.append(data)





while True:
    node = root
    while node.right is not None:
        factor = node.content.split(' ')[5]
        if input(f'Is the {factor} of this person above average?') == 'yes':
            node = node.right
        elif input(f'Is the {factor} of this person above average?') == 'no':
            node = node.left
        else:
            print('Invalid input, search end!')
    if node.value is None:
        print('The result for the search is shown below:')
        print([x['name'] for x in node.content])
        while True:
            name = input('Which person you would would like to have more infromation or finish')
            if name == 'finish':
                break
            else:
                try:
                    print([x for x in node.content if x['name'] == name][0])
                except:
                    print('Invalid Input!')
    if input('Would you like to search for someone else based on his academic performance?')=='yes':
        continue
    else:
        print('Search End')
        break
