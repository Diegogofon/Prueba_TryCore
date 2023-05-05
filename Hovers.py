import pytest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Inicializar el driver de Selenium
driver = webdriver.Chrome()

# Abrir la página web que queremos probar
driver.get("https://the-internet.herokuapp.com/hovers")
time.sleep(5)
# Encontrar el elemento que queremos hacer hover y mover el cursor sobre él
hover = driver.find_element(By.CLASS_NAME, "figure")
accion = ActionChains(driver).move_to_element(hover)
time.sleep(5)
accion.perform()

# Verificar que la información adicional se muestra correctamente
figcaption = driver.find_element(By.CLASS_NAME, 'figcaption')
if figcaption.is_displayed() == True:
    print("La información adicional se muestra después de hacer hover en el elemento")
else:
    print("La información adicional no se muestra después de hacer hover en el elemento")

# Cerrar el driver de Selenium
driver.quit()
