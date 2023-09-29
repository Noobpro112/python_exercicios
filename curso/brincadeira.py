import os
from selenium import webdriver
import time

# Adicione o caminho do driver ao PATH
os.environ['PATH'] += os.pathsep + 'C:\\Drivers'

# Crie uma nova instância do navegador
driver = webdriver.Edge()

# Vá para a página da web que você quer
driver.get('https://github.com/Noobpro112')

while True:
    # Espere 5 segundos
    time.sleep(0)
    
    # Recarregue a página
    driver.refresh()
