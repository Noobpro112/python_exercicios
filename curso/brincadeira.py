from selenium import webdriver
import time

# Crie uma nova instância do navegador
driver = webdriver.Edge(executable_path='C:\\Drivers\\msedgedriver.exe')

# Vá para a página da web que você quer
driver.get('https://github.com/Noobpro112')

while True:
    # Espere 5 segundos
    time.sleep(10)
    
    # Recarregue a página
    driver.refresh()
