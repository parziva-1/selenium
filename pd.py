import pandas as pd
import socket
import time


#numeros = r'C:\Users\Alberto\Documents\refacilSel.ods'
#df = pd.read_excel(numeros, engine='odf')
#for i in df.index:
#    numero = str(df['Numero'][i])
#    print(numero)

internet = False
while internet == False:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect(("www.google.com", 80))
    except (socket.gaierror, socket.timeout):
        print("Sin conexión a internet")
        internet= False
        time.sleep(10)
    else:
        print("Con conexión a internet")
        internet = True
        s.close()