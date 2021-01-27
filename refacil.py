import pandas as pd
import time
import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options


#guardar y acceder a la sesion
"""
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") 
driver = webdriver.Chrome(chrome_options=chrome_options)
"""
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

#Confifuraciones
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30) #tiempo de espera


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

######  Funciones #####

# nequi
def Nequi():
    
    if internet == True:
        
        driver.maximize_window()

        driver.get(url)

        # Acciones en la pagina

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


        for i in df.index:
            cel = str(df['Numero'][i])
            time.sleep(3)
            driver.get(urlNequiWallet)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelB)))
            driver.find_element_by_xpath(nequiSelB).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelSend)))
            driver.find_element_by_xpath(nequiSelSend).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelInputCel)))
            driver.find_element_by_xpath(nequiSelInputCel).send_keys(cel)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelInputValue)))
            driver.find_element_by_xpath(nequiSelInputValue).send_keys(nequiValue)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelBttSell)))
            driver.find_element_by_xpath(nequiSelBttSell).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelBttSub)))
            driver.find_element_by_xpath(nequiSelBttSub).click()
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelInputPass)))
            time.sleep(2)
            
            driver.find_element_by_xpath(nequiSelInputPass).send_keys(refacilSecondPass)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelBttSub2)))
            driver.find_element_by_xpath(nequiSelBttSub2).click()
            time.sleep(5)
            print(cel)
            #iniciar otra vez
            driver.get('https://plataforma.refacil.co/#/sms')
    else:
        Internet()
    
    driver.get(urlNequiWallet)

#Verificar si hay coneccion a internet

def Internet():
    global internet
    internet = False
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        try:
            s.connect(("www.google.com", 80))
        except (socket.gaierror, socket.timeout):
            print("Sin conexión a internet")
            time.sleep(10)
        else:
            print("Con conexión a internet")
            internet = True
            s.close()
            break

    return(internet)

def Loggin():
    if internet == True:

        driver.maximize_window()

        driver.get(url)

        # Acciones en la pagina

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


        alert = wait.until(ec.alert_is_present((By.CSS_SELECTOR, '#app > div:nth-child(2) > div.snotify.snotify-rightBottom > div > div > div')))
        print(alert.get_attribute("textContent"))
    
    else:
        Internet()





Internet()
print(internet)

if internet == True:

        driver.maximize_window()

        driver.get(url)

        # Acciones en la pagina

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


        for i in df.index:
            try:
                cel = str(int(df['Numero'][i]))
            except:
                #En caso de que el indice de la tabla de mande mas de los campos que hay.
                driver. quit()
            print('iteracion: ',i+1,", al Numero: ",cel)
            time.sleep(5)
            print(1)
            driver.get(urlNequiWallet)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelB)))
            try:
                driver.find_element_by_xpath(nequiSelB).click()
            except:
                driver.find_element_by_css_selector('#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-7.mb-4 > div.box-recharge > div > div > div:nth-child(1) > div').click()
            print("Ok")
            time.sleep(5)
            print(2)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelSend)))
            try:
                driver.find_element_by_xpath(nequiSelSend).click()
            except:
                driver.find_element_by_css_selector('#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-5.mb-4 > div > div > div:nth-child(1) > button').click()
                
            print("Ok")
            time.sleep(5)
            print(3)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelInputCel)))
            try:
                driver.find_element_by_xpath(nequiSelInputCel).send_keys(cel)
            except:
                driver.find_element_by_css_selector('#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-5.mb-4 > div > div > form > div > div.form-group > input').send_keys(cel)
                
            print("Ok")
            time.sleep(5)
            print(4)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelInputValue)))
            try:
                driver.find_element_by_xpath(nequiSelInputValue).send_keys(nequiValue)
            except:
                driver.find_element_by_css_selector('#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-5.mb-4 > div > div > form > div > input').send_keys(nequiValue)
            print("Ok")
            time.sleep(5)
            print(5)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelBttSell)))
            
            try:
                driver.find_element_by_xpath(nequiSelBttSell).click()
            except:
                driver.find_element_by_css_selector('#app > div.recharge > div:nth-child(2) > div > div > div.col-lg-5.mb-4 > div > div > form > div > div.box-btn > button.btn-primary.btn-recharge.btn-send').click()
            print("Ok")
            time.sleep(5)
            print(6)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelBttSub)))
            try:
                driver.find_element_by_xpath(nequiSelBttSub).click()
            except:
                driver.find_element_by_css_selector('#modalConfirmSale___BV_modal_body_ > div > div.text-center > button:nth-child(2)').click()
            print("Ok")
            time.sleep(5)
            print(7)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelInputPass)))
            
            try:
                driver.find_element_by_xpath(nequiSelInputPass).send_keys(refacilSecondPass)
            except:
                driver.find_element_by_css_selector('#modal3FA___BV_modal_body_ > form > div.form-group > div > input').send_keys(refacilSecondPass)
            print("Ok")
            time.sleep(5)
            print(8)
            wait.until(ec.visibility_of_element_located((By.XPATH, nequiSelBttSub2)))
            
            try:
                driver.find_element_by_xpath(nequiSelBttSub2).click()
            except:
                driver.find_element_by_css_selector('#modal3FA___BV_modal_body_ > form > div.box-btn.text-center.mt-4 > button.btn-primary.btn-recharge.btn-send').click()
            print("Ok")
            """
            alert = wait.until(ec.alert_is_present((By.CSS_SELECTOR, '#app > div:nth-child(2) > div.snotify.snotify-rightBottom')))
            print(alert.get_attribute("textContent"))
            time.sleep(5)
            """
            
            #iniciar otra vez
            driver.get('https://plataforma.refacil.co/#/sms')
