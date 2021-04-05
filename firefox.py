import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ac




url = 'https://plataforma.refacil.co'

user = 'JAIME722'
psw = 'lasMatasNoComen'
# Selectors

userSelector = '#app > div:nth-child(1) > div > form > div > div:nth-child(4) > div.form-group > div > input'

bottonS = '#app > div:nth-child(1) > div > form > div > div:nth-child(4) > div:nth-child(2) > button'

pswSelector = '#app > div:nth-child(1) > div > form > div > div:nth-child(4) > div.form-group > div > input'

bottonJoin = '#app > div:nth-child(1) > div > form > div > div:nth-child(4) > div:nth-child(2) > button'

productos ='#ddown1__BV_toggle_'

billeteras ='#ddown1 > ul > li:nth-child(8) > a'


driver = webdriver.Firefox()

driver.maximize_window()

driver.get(url)

# Acciones en la pagina

time.sleep(4)

driver.find_element_by_css_selector(userSelector).send_keys(user)
driver.find_element_by_css_selector(bottonS).click()

time.sleep(6)

driver.find_element_by_css_selector(pswSelector).send_keys(psw)
driver.find_element_by_css_selector(bottonJoin).click()
time.sleep(3)

driver.find_element_by_css_selector(billeteras).click()
driver.find_element_by_css_selector(productos).click()