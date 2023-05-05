import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Inicializar el driver de Selenium
driver = webdriver.Chrome()

# Abrir la página web que queremos probar
driver.get("https://the-internet.herokuapp.com/inputs")
time.sleep(5)
# Encontrar el input numérico por su atributo "id"
input_numerico1 = driver.find_element(By.CSS_SELECTOR ,"input")

# Lista de valores numéricos para introducir en el campo
valores_numericos = ["123", "456", "1234e567g", "789", "abcde12345!#$%&/"]

# Bucle para recorrer la lista de valores numéricos y enviarlos al campo
for valor in valores_numericos:
    input_numerico1.clear()  # Limpiar el campo antes de introducir el nuevo valor
    time.sleep(2)
    input_numerico1.send_keys(str(valor))
    # input_numerico1.send_keys(str(valor))  # Convertir el valor numérico a string antes de enviarlo
    if valor.isnumeric():
        print("El campo acepta correctamente la entrada " + valor)
    else:
        print("El campo acepta incorrectamente la entrada no numérica " + valor)

    # Comprobar que el valor introducido en el campo es correcto


# Cerrar el driver de Selenium
time.sleep(10)
driver.quit()
