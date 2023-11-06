from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

nav = webdriver.Chrome()

# Acessando a página
nav.get("https://benchpromos.com")

# Esperando o carregamento da página
time.sleep(6)

# Localizando e clicando no botão "Entrar" utilizando XPath
elemento_entrar = WebDriverWait(nav, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//a[@href="/sign-in" and contains(text(), "Entrar")]'))
)
elemento_entrar.click()

# Esperando um tempo para a página de login ser carregada
time.sleep(6)

# Localizando e preenchendo o campo de email
campo_email = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.NAME, 'email'))  # Altere 'email' para o nome real do campo de email
)
campo_email.send_keys('testefaculdade804@gmail.com')
time.sleep(2)

# Localizando e preenchendo o campo de senha
campo_senha = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.NAME, 'password'))  # Altere 'password' para o nome real do campo de senha
)
campo_senha.send_keys('1234567#')
time.sleep(2)
# Enviando o formulário de login (clicar no botão "Entrar")
campo_senha.submit()

# Esperando um tempo para observar o comportamento após o envio dos dados
time.sleep(6)

# Fechando o navegador
nav.quit()
