from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import time
import pandas as pd 


times = pd.read_csv('Times.csv')['Time']

# times = ['guarani', 'Joinville-SC', 'Santo André']


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
link_wikpedia = ''
for time_ in times:
    nome_time = time_.replace(' ', '+')
    print(time_)
    driver.get(f"https://www.google.com/search?q=futebol+{nome_time}")
    time.sleep(3)
    print(f"https://www.google.com/search?q=futebol+{nome_time}")


    try:
        informacoes = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[5]/div[2]/div')
        print('encontreei')
        link_wikpedia = informacoes.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[5]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/span[2]/a').get_attribute('href')
        print(link_wikpedia)
        time.sleep(2)


    except selenium.common.exceptions.NoSuchElementException:

        try:
            informacoes = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div')
            print('encontreei')
            link_wikpedia = informacoes.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/span[2]/a').get_attribute('href')
            print(link_wikpedia)
            time.sleep(2)


        except selenium.common.exceptions.NoSuchElementException:
            print('estou aqui ')
            resultados = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div/div[2]/div[2]/div/div').find_elements(By.TAG_NAME, 'div')
            cont = 0
            for resultado in resultados:
                cont += 1
                try:
                #tentativa de achar o wikpedia
                    x = resultado.find_element(By.XPATH, f'/html/body/div[3]/div/div[13]/div/div[2]/div[2]/div/div/div[{cont}]/div/div/div[1]/div/div/span/a')
                    if 'wikipedia' in x.get_attribute('href'):
                        print(x.get_attribute('href'))
                        link_wikpedia = x.get_attribute('href')
                        break
                except:
                    pass


    print(link_wikpedia)
    if link_wikpedia:
        driver.get(link_wikpedia)
        time.sleep(15)

    #     localizacao = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]/tbody').find_elements(By.TAG_NAME, 'tr')
    #     #/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody
    #     print(len(localizacao))
    #     for loc in localizacao:
    #         print(loc.text)
    # except:
    #     print('nada')
