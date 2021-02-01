import pandas as pd
import time
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#Confifuraciones
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30) #tiempo de espera




#datos
url = 'https://plataforma.refacil.co'
urlNequiWallet = 'https://plataforma.refacil.co/#/wallets'

refacilSecondPass = '4712'
numeros = r'C:\Users\Alberto\Documents\refacilSel.ods'
df = pd.read_excel(numeros, engine='odf')
nequiValue = '5000'
user = str(df['userName'][0])
psw = str(df['Psw'][0])
print(nequiValue)

# Selectors

userSelector = '/html/body/div/div[1]/div/form/div/div[2]/div[1]/div/input'
bottonS = '#app > div:nth-child(1) > div > form > div > div:nth-child(4) > div:nth-child(2) > button'
pswSelector = '/html/body/div/div[1]/div/form/div/div[2]/div[1]/div/input'
bottonJoin = '#app > div:nth-child(1) > div > form > div > div:nth-child(4) > div:nth-child(2) > button'
nequiSelB = '/html/body/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div'
nequiSelSend = '/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/button'
nequiSelInputCel = '/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/form/div/div[1]/input'
nequiSelInputValue = '/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/form/div/input'
nequiSelBttSell = '/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/form/div/div[3]/button[2]'
nequiSelBttSub = '/html/body/div[2]/div[1]/div/div/div/div/div[3]/button[2]'
nequiSelInputPass = '/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div/form/div[1]/div/input'
nequiSelBttSub2 = '/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div/form/div[2]/button[2]' 

# Acciones en la pagina

driver.maximize_window()

driver.get(url)
#esperar hasta que el xpath o css_selector aparesca en la pagina

time.sleep(2)
wait.until(ec.visibility_of_element_located((By.XPATH, userSelector)))

driver.find_element_by_xpath(userSelector).send_keys(user)
driver.find_element_by_css_selector(bottonS).click()
time.sleep(2)
#esperar hasta que el xpath o css_selector aparesca en la pagina
wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/div/form/div/div[2]/div[3]/button')))

driver.find_element_by_xpath(pswSelector).send_keys(psw)
driver.find_element_by_css_selector(bottonJoin).click()



notify_result = wait.until(presence_of_element_located((By.CLASS_NAME, "snotifyToast__body")))
print(notify_result.get_attribute("textContent"))

"""
driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
print(first_result.get_attribute("textContent"))
"""