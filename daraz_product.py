from selenium import webdriver
import urllib.request
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request
service = Service(executable_path='E:/Ml_eshikhon2/web_scrapping/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
import time



driver.get('https://www.daraz.com.bd/products/menz-solid-color-full-sleeve-tshirt-tshirt-t-shirt-i214457900-s1163410501.html')

height = driver.execute_script('return document.body.scrollHeight')
for k in range(0, height + 300, 30):
    driver.execute_script(f'window.scrollTo(0, {k});')
    time.sleep(0.1)
title = driver.find_element(By.XPATH,'//*[@id="module_product_title_1"]/div/div/span').text
rating= driver.find_element(By.XPATH,'//*[@id="module_product_review_star_1"]/div/a').text
price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span').text
discount = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/div/span[2]').text

point= driver.find_element(By.XPATH,'//*[@id="module_product_review"]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/span[1]').text


pic = []

for i in range(1, 4):
    photos = driver.find_element(By.XPATH, f'//*[@id="module_item_gallery_1"]/div/div[2]/div/div[1]/div/div[{i}]/div/img')
    image_url = photos.get_attribute('src')
    pic.append(image_url)


for index, image_url in enumerate(pic):
    image_name = f"image_{index}.jpg"  
    urllib.request.urlretrieve(image_url, image_name)
   
    print(f"Image {image_name} downloaded.")

comment_list=[]

for comment in driver.find_elements(By.CSS_SELECTOR, '.mod-reviews .content'):
    comment_list.append(comment.text)
print(len(driver.find_elements(By.CSS_SELECTOR, '.mod-reviews .content')))

Rating= rating.split(' ')



print(title)
print(Rating[0])
print(point)
print(price)
print(discount)
print(comment_list)

import pandas as pd
title_dic={"title":title,"rating":Rating[0],"point":point,"price":price,"discount":discount,"comment":comment_list}
df = pd.DataFrame(title_dic)

df.to_csv('output.csv', index=False)

time.sleep(20)+
