# Bibliotecas

import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# load the .env variables
load_dotenv()

# access the variables from the dotEnv file
login = os.getenv("LOGIN")
senha = os.getenv("SENHA")
url = os.getenv("URL")




service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)


#close the cookie option button
time.sleep(3)
cookie_button = driver.find_element(by=By.XPATH, value='//*[@id="adopt-accept-all-button"]')
cookie_button.click()


time.sleep(3)

#login

login_box = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[1]/div/div[2]/div/div/input')
login_box.send_keys(login)
time.sleep(3)
password_box = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[2]/div/div[2]/div/div/input')
password_box.send_keys(senha)
time.sleep(3)

send_button = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/button')
send_button.click()
time.sleep(100)


# # LOGIN
# autentica = driver.find_element(
#     by=By.XPATH, value="//*[@id='autenticacao:loginEmpresa']")
# autentica.send_keys(login)

# senha_input = driver.find_element(
#     by=By.XPATH, value="//*[@id='autenticacao:senhaEmpresa']")
# senha_input.send_keys(senha)
# entrar = driver.find_element(
#     by=By.XPATH, value="//*[@id='autenticacao:entrarEmpresa']")
# entrar.click()



# banner = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(By.XPATH, value ='//*[@id="adopt-accept-all-button"]'))
# banner.click()
# time.sleep(200)

#banner = WebDriverWait(driver, 20).until(by=By.XPATH, value='//*[@id="adopt-accept-all-button"]')


# search_box = WebDriverWait(driver, 20).until(
#     EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[1]/div/div[2]/div/div/input'))
# )

#search_box.send_keys("Texto de busca")


#search_box = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[1]/div/div[2]/div/div/input')
# search_box.click()
#time.sleep(20)

# # LOGIN
# autentica = driver.find_element(
#     by=By.XPATH, value="//*[@id='autenticacao:loginEmpresa']")
# autentica.send_keys(login)

# senha_input = driver.find_element(
#     by=By.XPATH, value="//*[@id='autenticacao:senhaEmpresa']")
# senha_input.send_keys(senha)
# entrar = driver.find_element(
#     by=By.XPATH, value="//*[@id='autenticacao:entrarEmpresa']")
# entrar.click()


# # Aguarda até que a página de login seja processada (espera um elemento da próxima página)
# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Todos os direitos reservados')]")) # this text is the signal that the page is loaded
#     )
# except:
#     print("Erro no login ou elemento não encontrado.")
#     driver.quit()

# # Navega para a página desejada
# driver.get("http://sigec.crea-pi.org.br/sigec/servicosOnline/art.jsf") 

# # Pausa para visualização

# time.sleep(2)

# fechar_banner = driver.find_element(
#     by=By.XPATH, value='//*[@id="j_idt39"]/div[1]/a/span')
# fechar_banner.click()




# NOMEL = driver.find_element(by=By.XPATH, value='//*[@id="j_idt70"]/span[2]')
# NOMEL.click()

# time.sleep(600)
