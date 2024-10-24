from selenium import webdriver
import selenium.common
from selenium.webdriver.common.by import By
import selenium
import time
import pandas as pd 


df = pd.read_csv('Estadios.csv', sep=',')
estadios = df[df['Localização'].isna()][df['Estadio'].notna()]['Estadio']
print(estadios)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
for estadio in estadios:
    local = ''
    print('----'*50)
    nome_estadio = estadio.replace('-', ' ').replace(' ', '_')
    print(estadio)
    driver.get(f"https://pt.wikipedia.org/wiki/{nome_estadio}")
    print(f"https://pt.wikipedia.org/wiki/{nome_estadio}")
    time.sleep(2)
    try:
        print('primeiro try')
        # //*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[1]
        # //*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td[1]
        #//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[1]
        if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[1]').text == 'Local':
            print('Terceiro')
            print('217')
            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[2]').text
            
            print(local)
        if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[7]/td[1]').text == 'Local':
            print('213')
            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[7]/td[2]').text
            print(local)

        elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[5]/td[1]').text == 'Local':
            print('214')
            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[5]/td[2]').text
            print(local)
        elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[1]').text == 'Local':
            print('215')
            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[2]').text
            
            print(local)
        
        print('dentro dos if')

    except selenium.common.exceptions.NoSuchElementException:
        print('segundo try')
        try:
            print(driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[1]').text)
            if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[1]').text == 'Local':
                print('Terceiro')
                print('217')
                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[2]').text
                
                print(local)
            #//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[8]/td[1]
            if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[1]').text == 'Local':
                
                print('Terceiro')
                print('****')
                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[2]').text
                print('-------')
                print(local)

            elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td[1]').text == 'Local':
                print('Terceiro')
                print('218')
                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[6]/td[2]').text
                
                print(local)
            # print('a')
            elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td[1]').text == 'Local':
                print('Terceiro')
                print('218')
                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td[2]').text
                
                print(local)
            # print('b')

            elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[1]').text == 'Local':
                print('Terceiro')
                print('225')
                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[2]').text
                
                print(local)
        
            # //*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[1]

        except selenium.common.exceptions.NoSuchElementException:
            print('terceiro try')
            try:
                if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[8]/td[1]').text == 'Local':
                    print('Segundo')
                    print('****')
                    local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[8]/td[2]').text
                    print('-------')
                    print(local)

                if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[7]/td[1]').text == 'Local':
                    print('Segundo')
                    print('****')
                    local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[7]/td[2]').text
                    print('-------')
                    print(local)

                if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[8]/td[1]').text == 'Local':
                        
                        print('Quarto')
                        print('****')
                        local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[8]/td[2]').text
                        print('-------')
                        print(local)
                

                

            except selenium.common.exceptions.NoSuchElementException:
                try:
                    print('quarto try')
                    print(driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[8]/td[1]').text)
                    # //*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[4]/td[1]
                    
                    if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[1]').text == 'Local':
                        
                        print('Quarto')
                        print('****')
                        local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[2]').text
                        print('-------')
                        print(local)

                    elif driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[4]/td[1]').text == 'Local':
                        
                        print('Quarto')
                        print('****')
                        local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[4]/td[2]').text
                        print('-------')
                        print(local)

                    
                except selenium.common.exceptions.NoSuchElementException:
                    try:
                        print('quinto try')
                        if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[1]').text == 'Local':
                            
                            local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[9]/td[2]').text
                            
                            print(local)
                    except selenium.common.exceptions.NoSuchElementException:
                        try:
                            if driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[4]/td[1]').text == 'Local':
                                print('Segundo')
                                print('****')
                                local = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[4]/td[2]').text
                                print('-------')
                                print(local)
                        except selenium.common.exceptions.NoSuchElementException:
                            pass
                except selenium.common.exceptions.InvalidSelectorException:
                    pass

    time.sleep(1)
    # //*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[5]/td[1]
    # //*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[7]/td[2]
    # //*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[7]/td[2]
    # //*[@id="mw-content-text"]/div[1]/table/tbody/tr[7]/td[2]
    # //*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[8]/td[2]
    # //*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[5]/td[2]
    if local:
        df.loc[df['Estadio'] == estadio, 'Localização'] = local
    else:
        df.loc[df['Estadio'] == estadio, 'Localização'] = "Não Encontrado"

    time.sleep(2)

# Salvar o DataFrame atualizado no CSV
df.to_csv('Estadios.csv', index=False)

print(df)

   