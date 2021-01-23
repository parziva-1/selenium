import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

#guardar y acceder a la sesion

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") 
driver = webdriver.Chrome(chrome_options=chrome_options)

#datos
url = 'https://plataforma.refacil.co'
urlNequiWallet = 'https://plataforma.refacil.co/#/wallets'
nequiValue = '1000'
user = 'JAIME722'
psw = 'lasMatasNoComen'
#cel = '3058166789'
refacilSecondPass = '4712'
numeros = r'C:\Users\Alberto\Documents\refacilSel.ods'
df = pd.read_excel(numeros, engine='odf')


# Selectors

userSelector = '/html/body/div/div[1]/div/form/div/div[2]/div[1]/div/input'

bottonS = '#app > div:nth-child(1) > div > form > div > div:nth-child(4) > div:nth-child(2) > button'

pswSelector = '/html/body/div/div[1]/div/form/div/div[2]/div[1]/div/input'

bottonJoin = '#app > div:nth-child(1) > div > form > div > div:nth-child(4) > div:nth-child(2) > button'

nequiSelB = '#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-7.mb-4 > div.box-recharge > div > div > div:nth-child(1) > div'

nequiSelSend = '#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-5.mb-4 > div > div > div:nth-child(1) > button'

nequiSelInputCel = '#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-5.mb-4 > div > div > form > div > div.form-group > input'


nequiSelInputValue = '#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-5.mb-4 > div > div > form > div > input'

nequiSelBttSell = '#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-5.mb-4 > div > div > form > div > div.box-btn > button.btn-primary.btn-recharge.btn-send'

nequiSelBttSub = '#modalConfirmSale___BV_modal_body_ > div > div.text-center > button:nth-child(2)'

nequiSelInputPass = '#modal3FA___BV_modal_body_ > form > div.form-group > div > input'

nequiSelBttSub2 = '#modal3FA___BV_modal_body_ > form > div.box-btn.text-center.mt-4 > button.btn-primary.btn-recharge.btn-send' 

driver = webdriver.Chrome()

driver.maximize_window()

driver.get(url)

# Acciones en la pagina

#esperar hasta que el xpath o css_selector aparesca en la pagina
time.sleep(2)
wait = WebDriverWait(driver,10)
wait.until(ec.visibility_of_element_located((By.XPATH, userSelector)))

driver.find_element_by_xpath(userSelector).send_keys(user)
driver.find_element_by_css_selector(bottonS).click()
time.sleep(2)
#esperar hasta que el xpath o css_selector aparesca en la pagina
wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div/div[1]/div/form/div/div[2]/div[3]/button')))

driver.find_element_by_xpath(pswSelector).send_keys(psw)
driver.find_element_by_css_selector(bottonJoin).click()





# nequi
def Nequi():
    
    
    for i in df.index:
        cel = str(df['Numero'][i])
        time.sleep(3)
        driver.get(urlNequiWallet)
        driver.find_element_by_css_selector(nequiSelB).click()
        driver.find_element_by_css_selector(nequiSelSend).click()
        driver.find_element_by_css_selector(nequiSelInputCel).send_keys(cel)
        driver.find_element_by_css_selector(nequiSelInputValue).send_keys(nequiValue)
        driver.find_element_by_css_selector(nequiSelBttSell).click()
        driver.find_element_by_css_selector(nequiSelBttSub).click()
        time.sleep(2)
        driver.find_element_by_css_selector(nequiSelInputPass).send_keys(refacilSecondPass)
        driver.find_element_by_css_selector(nequiSelBttSub2).click()
        time.sleep(5)
        print(cel)
        #iniciar otra vez
        driver.get('https://plataforma.refacil.co/#/sms')

    





Nequi()
