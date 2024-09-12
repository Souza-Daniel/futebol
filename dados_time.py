from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd 


times = pd.read_csv('Times.csv')['Time']

driver = webdriver.Chrome()
for time_ in times:
    nome_time = time_.replace(' ', '+')
    print(time_)
    driver.get(f"https://www.google.com/search?q=futebol+{nome_time}")
    time.sleep(3)
    try:
        informacoes = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[5]/div[2]/div')
        print('encontreei')
        time.sleep(2)
        link_wikpedia = informacoes.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[5]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/span[2]/a').get_attribute('href')
        print(link_wikpedia)
        time.sleep(2)
        driver.get(link_wikpedia)
        time.sleep(3)
        localizacao = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]/tbody').find_elements(By.TAG_NAME, 'tr')
        #/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody
        print(len(localizacao))
        for loc in localizacao:
            print(loc.text)
    except:
        print('nada')

driver.quit()