import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
# Creamos el objeto webdriver
driver = webdriver.Chrome()

def test_dropdown():
    # Navegamos a la página de prueba
    driver.get('http://the-internet.herokuapp.com/dropdown')
    time.sleep(5)
    # Buscamos el elemento desplegable por su id
    dropdown_list = Select(driver.find_element(By.ID, 'dropdown'))
    
    # Buscamos todas las opciones dentro del elemento desplegable y seleccionamos la opción con texto "Option 1"
    for option in dropdown_list.options:
        time.sleep(3)
        if option.text == 'Option 1':
            option.click()
            break
    
    # Verificamos que la opción seleccionada sea "Option 1" mediante una aserción de Pytest
    assert dropdown_list.first_selected_option.text == 'Option 1'