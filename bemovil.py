import pyautogui
import pyperclip
import time
import pandas as pd

#numeros = r'C:\Users\Alberto\Documents\refacilSel.ods'
df = pd.read_excel(r'C:\Users\Alberto\Documents\refacilSel.ods', engine='odf')
nequiValue = '5000'


screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

""" #Entrar al emulador
pyautogui.click(711, 740)
time.sleep(2)
#entrar a la app 
pyautogui.click(380, 280)
time.sleep(4)
#entrar a la parte de multiproducto de la app
pyautogui.click(760, 120)
time.sleep(2)
#entramos a nequi envio
pyautogui.click(620, 380)
time.sleep(2)
#click en el input de valor de envio
pyautogui.click(600, 150)
pyperclip.copy(nequiValue)
time.sleep(2)
#pegar el nequivalue
pyautogui.hotkey('ctrl', 'v', interval = 0.15)
time.sleep(2)
#click en numero
pyautogui.click(630, 222)
time.sleep(2)
#pegar el cel
pyperclip.copy(cel)
pyautogui.hotkey('ctrl', 'v', interval = 0.15)
time.sleep(2)
#click en generar
pyautogui.click(600, 270)
#click en generar x2 o da error
time.sleep(2)
pyautogui.click(600, 270)
time.sleep(5)
#click en generar confirmar ventana modal
pyautogui.click(600, 500)
time.sleep(2)
#click para salir de la ventana modal
pyautogui.click(600, 650)





pyautogui.moveTo(620, 380)
time.sleep(2)
 """





print(screenHeight,screenWidth)
def sendBe():
    print("Bemovil")
    #Entrar al emulador
    pyautogui.click(711, 740)
    time.sleep(2)
    #entrar a la app 
    pyautogui.click(380, 280)
    time.sleep(10)
    #entrar a la parte de multiproducto de la app
    pyautogui.click(760, 120)
    time.sleep(2)
    #entramos a nequi envio
    pyautogui.click(620, 380)

    for i in df.index:
        cel = str(int(df['Numero'][i]))
        print(f'Enviando {nequiValue}, al numero {cel}')
            
        
        time.sleep(2)
        #click en el input de valor de envio
        pyautogui.doubleClick(530, 150)
        pyperclip.copy(nequiValue)
        time.sleep(2)
        #pegar el nequivalue
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        time.sleep(2)
        #click en numero
        pyautogui.doubleClick(545, 222)
        time.sleep(2)
        #pegar el cel
        pyperclip.copy(cel)
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        time.sleep(2)
        #click en generar
        pyautogui.click(600, 270)
        #click en generar x2 o da error
        time.sleep(2)
        pyautogui.click(600, 270)
        time.sleep(5)
        #click en generar confirmar ventana modal
        pyautogui.click(600, 500)
        time.sleep(10)
        #click para salir de la ventana modal
        pyautogui.click(730, 415)
        time.sleep(2)
        pyautogui.click(600, 650)
        time.sleep(2)

sendBe()