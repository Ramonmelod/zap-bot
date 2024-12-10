import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def remove_cookie_button():
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[2]'))
        )
        print("Elemento encontrado. Tentando ocultá-lo...")
        driver.execute_script("arguments[0].remove();", elemento)
        print("Elemento ocultado com sucesso.")
    except Exception as e:
        print(f"Erro ao tentar ocultar o elemento: {e}")

def save_button_click():
    try:
        salvar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="top-page"]/div/div[1]/footer/div/div/button[2]'))
        )
        salvar.click()
    except Exception as e:
        print(f"Erro ao tentar salvar o anúncio: {e}")



file_path = 'ids.json'

# reading the ids.json file
try:
    with open(file_path, 'r') as file: # 'r' is the open mode with 'r' meaning the readable mode
        data = json.load(file)  # Loads the content of the file as a Python object (list/dictionary)
except FileNotFoundError:
    print(f"O arquivo {file_path} não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro ao decodificar o arquivo JSON {file_path}. Verifique o formato do arquivo.")


# access the variables from the dotEnv file
login = os.getenv("LOGIN")
senha = os.getenv("SENHA")
url = os.getenv("URL")


# sets the browser up
# Configurar as opções para o Chromium
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # path to Chromium
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#options.add_argument('--headless')  # run without Grafic interface
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-gpu')  # Needed for some linux distros
options.add_argument('--window-size=1920,1080')  # Define the size of the window


# Configurar o serviço e o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)
#driver.save_screenshot('screenshot.png')
# accept the cookie options
try: 
    time.sleep(2)
    cookie_button =  WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="adopt-accept-all-button"]')) # this text is the signal that the page is loaded
    )
    cookie_button.click()
    time.sleep(3)
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

# waits the presence of one element of the page wich shows that it was loaded
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[1]/div/div[2]/div/div/input')) # this text is the signal that the page is loaded
    )
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    driver.quit()

#login
try:
    login_box = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[1]/div/div[2]/div/div/input')
    login_box.send_keys(login)
    time.sleep(1)
    password_box = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[2]/div/div[2]/div/div/input')
    password_box.send_keys(senha)
    time.sleep(1)
    send_button = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/button')                                               
    send_button.click()
except Exception as e:
    print(f"Ocorreu um erro inesperado no login: {e}")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="top-page"]/div/section[1]/div[1]/button')) # holds the program flow until this element is present
)

# opening the edit pages of the ads and saving them
for item in data:
    try:
        driver.get(f'https://canalpro.grupozap.com/ZAP_OLX/0/listings/update/{item["id"]}') # calling the page with list the ads
        print(item["id"])
        time.sleep(5)
        remove_cookie_button()
        time.sleep(5)
        save_button_click()
        time.sleep(3)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

driver.quit()
