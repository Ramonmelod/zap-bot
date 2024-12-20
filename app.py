import os
import json
import random
import time
from telegram import send_message
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

number_succesfull_saves = 0
# access the variables from the dotEnv file
login = os.getenv("LOGIN")
senha = os.getenv("SENHA")
url = os.getenv("URL")
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
chat_id_Gab = os.getenv("GAB_CHAT_ID")



# random variable used in time.sleep()
random_start_time = random.randint(2, 6) # 240s = 4 min - 900s = 15 min
random_action_time = random.randint(1,3) # 240s = 4 min - 900s = 15 min

# randomizing time to call the zap url

message = f"time to start: {random_start_time}" 
send_message(bot_token, chat_id, message)
send_message(bot_token, chat_id_Gab, message) # sends the message to Gab
print(message)
time.sleep(random_start_time)

def remove_cookie_button():
    try:
        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[2]'))
        )
        print("Element found. trying to remove it...")
        driver.execute_script("arguments[0].remove();", elemento)
        print("Element succesfully removed!.")
    except Exception as e:
        print(f"The following error ocurred when tryed to remove the element: {e}")

def save_button_click(item):
    global number_succesfull_saves  # makes this function to use the global variable number_succesfull_saves instead of creating a new one
    try:
        salvar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="top-page"]/div/div[1]/footer/div/div/button[2]'))
        )
        salvar.click()
        number_succesfull_saves += 1 # increments the value of number_succesfull_saves for control of the succes of the whole operation
        print("number_succesfull_saves: " + str(number_succesfull_saves))
        message = f"Anúncio com o Id: {item} foi salvo!" 
        send_message(bot_token, chat_id, message)
    except Exception as e:
        print(f"Erro ao tentar salvar o anúncio: {e}")
        message = f"O erro: {e} ocorreu ao tentar salvar o item de id: {item}"
        send_message(bot_token, chat_id, message)
    
         



file_path = 'ids.json'

# reading the ids.json file
try:
    with open(file_path, 'r') as file: # 'r' is the open mode with 'r' meaning the readable mode
        data = json.load(file)  # Loads the content of the file as a Python object (list/dictionary)
except FileNotFoundError:
    print(f"O arquivo {file_path} não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro ao decodificar o arquivo JSON {file_path}. Verifique o formato do arquivo.")




# sets the browser up
# Configurar as opções para o Chromium
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # path to Chromium
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # run without Grafic interface
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-gpu')  # Needed for some linux distros
options.add_argument('--window-size=1920,1080')  # Define the size of the window


# Sets the service and the driver
service = Service(ChromeDriverManager().install()) # service = Service("/usr/bin/chromedriver") # here is the path of the chromedriver in the current S.O
print(service)
driver = webdriver.Chrome(service=service, options=options)




driver.get(url)
#driver.save_screenshot('screenshot.png') # enable
# accept the cookie options
try: 
    time.sleep(random_action_time)
    cookie_button =  WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="adopt-accept-all-button"]')) # this text is the signal that the page is loaded
    )
    cookie_button.click()
    time.sleep(random_action_time)
    
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
        time.sleep(random_action_time)
        remove_cookie_button()
        time.sleep(random_action_time)
        save_button_click(item["id"])
        time.sleep(random_action_time)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
if len(data) == number_succesfull_saves:
    print(f"todos os {len(data)} anúncios foram atualizados com sucesso!")
    message = f"todos os {len(data)} anúncios foram atualizados com sucesso!"
    send_message(bot_token, chat_id, message)
    send_message(bot_token, chat_id_Gab, message) # sends the message to Gab
else:
    print(f"Dos {len(data)} anúncios, {number_succesfull_saves} foram salvos")
    message = f"Dos {len(data)} anúncios, {number_succesfull_saves} foram salvos" 
    send_message(bot_token, chat_id, message)
    send_message(bot_token, chat_id_Gab, message) # sends the message to Gab

driver.quit()
