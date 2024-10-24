from selenium import webdriver
import selenium.common
from selenium.webdriver.common.by import By
import selenium
import time
import pandas as pd 


df = pd.read_csv('Estadios.csv', sep=',')
estadios = df[df['Localização'].isna()][df['Estadio'].notna()]['Estadio']

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
for estadio in estadios:
    local = ''
    print('----'*50)
    nome_estadio = estadio.replace('-', ' ').replace(' ', '_')
    print(estadio)
    driver.get(f"https://pt.wikipedia.org/wiki/{nome_estadio}")
    time.sleep(2)
    try:

        if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[1]').text == 'Local':

            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[2]').text
            
        if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[7]/td[1]').text == 'Local':

            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[7]/td[2]').text

        elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[5]/td[1]').text == 'Local':

            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[5]/td[2]').text

        elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[1]').text == 'Local':

            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[2]').text

    except selenium.common.exceptions.NoSuchElementException:

        try:
            if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[1]').text == 'Local':

                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[2]').text
                
            if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[1]').text == 'Local':

                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[2]').text


            elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td[1]').text == 'Local':

                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td[2]').text

            elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td[1]').text == 'Local':

                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td[2]').text

            elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[1]').text == 'Local':

                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[2]').text

        except selenium.common.exceptions.NoSuchElementException:

            try:
                if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[8]/td[1]').text == 'Local':

                    local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[8]/td[2]').text

                if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[7]/td[1]').text == 'Local':

                    local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[7]/td[2]').text

                if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[8]/td[1]').text == 'Local':
                        
                        local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[8]/td[2]').text
                        
            except selenium.common.exceptions.NoSuchElementException:
                try:
                                        
                    if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[1]').text == 'Local':
                        
                        local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[2]').text

                    elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[4]/td[1]').text == 'Local':
                        
                        local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[4]/td[2]').text
                   
                except selenium.common.exceptions.NoSuchElementException:
                    try:

                        if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[1]').text == 'Local':
                            
                            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[2]').text
                            
                    except selenium.common.exceptions.NoSuchElementException:
                        try:
                            if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[4]/td[1]').text == 'Local':

                                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[4]/td[2]').text

                        except selenium.common.exceptions.NoSuchElementException:
                            pass
                except selenium.common.exceptions.InvalidSelectorException:
                    pass

    time.sleep(1)
    if local:
        df.loc[df['Estadio'] == estadio, 'Localização'] = local
    else:
        df.loc[df['Estadio'] == estadio, 'Localização'] = "Não Encontrado"

    time.sleep(2)

# Salvar o DataFrame atualizado no CSV
df.to_csv('Estadios.csv', index=False)

print(df)

   