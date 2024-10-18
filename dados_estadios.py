from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import time
import pandas as pd 


times = pd.read_csv('Times.csv')['Time']

# times = ['guarani', 'Joinville-SC', 'Santo André']


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
link_wikpedia = ''
driver.get(f"https://www.google.com/search?q=futebol+Flamengo")
time.sleep(3)