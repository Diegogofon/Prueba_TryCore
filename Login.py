from selenium import webdriver
from selenium.webdriver.common.by import By

# Configura el controlador de Selenium para Chrome
driver = webdriver.Chrome()

# Navega a la página de inicio de sesión
driver.get("https://the-internet.herokuapp.com/login")

# Define la lista de credenciales
credenciales = [
    {"usuario": "usuario1", "contraseña": "password1"},
    {"usuario": "usuario2", "contraseña": "password2"},
    {"usuario": "tomsmith", "contraseña": "SuperSecretPassword!"}
]

# Itera a través de cada conjunto de credenciales y realiza el inicio de sesión
for credencial in credenciales:
    # Encuentra los campos de usuario y contraseña y envía las credenciales correspondientes
    usuarios = driver.find_element(By.ID, "username")
    usuarios.send_keys(credencial["usuario"])
    contraseñas = driver.find_element(By.ID, "password")
    contraseñas.send_keys(credencial["contraseña"])

    # Encuentra el botón de inicio de sesión y haz clic en él
    boton_login = driver.find_element(By.XPATH, "//form[@id='login']/button/i")
    boton_login.click()

    # Realiza alguna acción para verificar que el inicio de sesión fue exitoso
titulo=driver.title
print("El título de la página es: " + titulo)

# Comprobar si el inicio de sesión fue exitoso
titulo = driver.title
if titulo == "Secure Area":
    print("Inicio de sesión exitoso")
else:
    print("Inicio de sesión fallido")


# Cierra la sesión del navegador
driver.quit()
