from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import time
import pandas as pd 

# Carregar o CSV em um DataFrame
df = pd.read_csv('Times.csv')

times = df['Time']
print(times)
# Configurações do Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()

for time_ in times:
    link_wikipedia = ''
    localizacao = ''
    nome_time = time_.replace(' ', '+')
    print(time_)
    driver.get(f"https://www.google.com/search?q=futebol+{nome_time}")
    time.sleep(3)
    print(f"https://www.google.com/search?q=futebol+{nome_time}")
    # Cpturando link do Wikpedia para pegar os estados

    try:
        informacoes = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[5]/div[2]/div')
        link_wikipedia = informacoes.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[5]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/span[2]/a').get_attribute('href')
        print('encontrei - primeiro try')
        time.sleep(2)

    except selenium.common.exceptions.NoSuchElementException:
        try:
            informacoes = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[5]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div')
            print('encontrei - segundo try')
            link_wikipedia = informacoes.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[5]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/span[2]/a').get_attribute('href')
            time.sleep(2)

        except selenium.common.exceptions.NoSuchElementException:
            try:
                informacoes = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div')
                print('encontrei - terceiro try')
                link_wikipedia = informacoes.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/span[2]/a').get_attribute('href')
                time.sleep(2)

            except selenium.common.exceptions.NoSuchElementException:

                try:
                    informacoes = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[4]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div')
                    print('encontrei - quarto try')
                    link_wikipedia = informacoes.find_element(By.XPATH, '/html/body/div[3]/div/div[13]/div[4]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/span[2]/a').get_attribute('href')
                    time.sleep(2)

                except selenium.common.exceptions.NoSuchElementException:

                    try:
                        print('estou aqui')
                        resultados = driver.find_element(By.ID, 'rso').find_elements(By.TAG_NAME, 'div')
                        ##                                         /html/body/div[3]/div/div[13]/div/div[2]/div[2]/div/div
                        print(len(resultados))
                        cont = 0
                        for resultado in resultados:
                            cont += 1
                            # /html/body/div[3]/div/div[13]/div[4]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/span[2]/a                        
                            try:
                                x = resultado.find_element(By.XPATH, f'/html/body/div[3]/div/div[13]/div/div[2]/div[2]/div/div/div[{cont}]/div/div/div[1]/div/div/span/a')
                                if 'wikipedia' in x.get_attribute('href'):
                                    link_wikipedia = x.get_attribute('href')
                                    break
                            except selenium.common.exceptions.NoSuchElementException:
                                try:
                                    x = driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/span/a')
                                    if 'wikipedia' in x.get_attribute('href'):
                                        link_wikipedia = x.get_attribute('href')
                                        break
                                except selenium.common.exceptions.NoSuchElementException:
                                    pass
                    except selenium.common.exceptions.NoSuchElementException:
                        pass
    
    print(link_wikipedia)
    
    # Coletar a localização do time no Wikipedia
    if link_wikipedia:
        driver.get(link_wikipedia)
        time.sleep(2)
        try:

            if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[11]/td[1]').text == "Localização":
                localizacao = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[11]/td[2]').text


            elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[9]/td[1]').text == "Localização":
                localizacao = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[9]/td[2]').text
            
            elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[10]/td[1]').text == "Localização":
                localizacao = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[10]/td[2]').text

        except selenium.common.exceptions.NoSuchElementException:

            try:

                if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[11]/td[1]').text == "Localização":
                    localizacao = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[11]/td[2]').text

            except selenium.common.exceptions.NoSuchElementException:
                try:
                    if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[11]/td[1]').text == "Localização":
                        localizacao = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[11]/td[2]').text

                except selenium.common.exceptions.NoSuchElementException:

                    if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[4]/tbody/tr[11]/td[1]').text == "Localização":
                        localizacao = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[4]/tbody/tr[11]/td[2]').text
                        #                                           //*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[10]/td[2]
                           

        print(localizacao)

    
    df.loc[df['Time'] == time_, 'Estado'] = localizacao

    time.sleep(2)

# Salvar o DataFrame atualizado no CSV
df.to_csv('Times.csv', index=False)

print(df)




    #     localizacao = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[2]/tbody').find_elements(By.TAG_NAME, 'tr')
    #     #/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody
    #     print(len(localizacao))
    #     for loc in localizacao:
    #         print(loc.text)
    # except:
    #     print('nada')
