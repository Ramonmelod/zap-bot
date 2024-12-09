import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# access the variables from the dotEnv file
login = os.getenv("LOGIN")
senha = os.getenv("SENHA")
url = os.getenv("URL")



service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get(url)



try:
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="adopt-accept-all-button"]')) # this text is the signal that the page is loaded
    )
except:
    print("Botão de cookies não encontrado.")
    driver.quit()

time.sleep(3)

try: 
    #close the cookie option button
    cookie_button = driver.find_element(by=By.XPATH, value='//*[@id="adopt-accept-all-button"]')
    cookie_button.click()
    time.sleep(3)
except NoSuchElementException:
    print("Botão de cookies não encontrado.")
except ElementNotInteractableException:
    print("Botão de cookies encontrado, mas não pode ser interagido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[1]/div/div[2]/div/div/input')) # this text is the signal that the page is loaded
    )
except:
    print("Botão de cookies não encontrado.")
    driver.quit()


#login

login_box = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[1]/div/div[2]/div/div/input')
login_box.send_keys(login)
time.sleep(1)
password_box = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/div[2]/div/div[2]/div/div/input')
password_box.send_keys(senha)
time.sleep(1)
send_button = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[2]/div/div/div/div/section[1]/div/section/form/button')                                               
send_button.click()

#listings


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="top-page"]/div/section[1]/div[1]/button')) # holds the program flow until this element is present
    )
except:
    print("Botão de cookies não encontrado.")
    driver.quit()

driver.get('https://canalpro.grupozap.com/ZAP_OLX/0/listings')

#####################################################################################

#?pageNumber=2

#//*[@id="top-page"]/section/div[4]/div/div/section/div/div/div/div[1]/div/section/div[2]/section[2]/section[2]/section[1]/ul/li[1]/a
#//*[@id="top-page"]/section/div[4]/div/div/section/div/div/div/div[2]/div/section/div[2]/section[2]/section[2]/section[1]/ul/li[1]/a
#//*[@id="top-page"]/section/div[4]/div/div/section/div/div/div/div[3]/div/section/div[2]/section[2]/section[2]/section[1]/ul/li[1]/a

#page 2
#//*[@id="top-page"]/section/div[4]/div/div/section/div/div/div/div[1]/div/section/div[2]/section[2]/section[2]/section[1]/ul/li[1]/a


#//*[@id="top-page"]/section/div[4]/div/div/section/div/div/div/div[8]/div/section/div[2]/section[2]/section[2]/section[1]/ul/li[1]/a


##############time.sleep(1000)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="top-page"]/section/div[4]/div/div/section/div/div/div/div[1]/div/section/div[2]/section[2]/section[2]/section[1]/div')) # holds the program flow until the edit button is present
    )
except:
    print("Botão de cookies não encontrado.")
    driver.quit()


options = driver.find_element(by=By.XPATH, value='//*[@id="top-page"]/section/div[4]/div/div/section/div/div/div/div[1]/div/section/div[2]/section[2]/section[2]/section[1]/div')
options.click()

time.sleep(10)

editar = driver.find_element(by=By.XPATH, value='//*[@id="top-page"]/section/div[4]/div/div/section/div/div/div/div[1]/div/section/div[2]/section[2]/section[2]/section[1]/ul/li[1]/a')
editar.click()

time.sleep(10)
try:
    elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div[2]'))
    )
    print("Elemento encontrado. Tentando ocultá-lo...")
    driver.execute_script("arguments[0].remove();", elemento)
    print("Elemento ocultado com sucesso.")
except Exception as e:
    print(f"Erro ao tentar ocultar o elemento: {e}")




#//*[@id="category-0"]/div[2]/span[1]/label
#//*[@id="572"]
#//*[@id="app"]/div[2]/div[1]/div[2]/div/div/a/div/svg

# time.sleep(8)
# //*[@id="adopt-controller-button"]/svg/path[2]
# //*[@id="adopt-controller-button"]/svg
# //*[@id="adopt-controller-button"]/svg
#//*[@id="adopt-controller-button"]
#/html/body/div[2]


salvar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="top-page"]/div/div[1]/footer/div/div/button[2]'))
)
salvar.click()


# salvar = driver.find_element(by=By.XPATH, value='//*[@id="top-page"]/div/div[1]/footer/div/div/button[2]')
# salvar.click()

time.sleep(1000)





