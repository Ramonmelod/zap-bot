import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager


# Options of the chromium configuration
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # path to Chromium
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')  # run without Grafic interface
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-gpu')  # Needed for some linux distros
options.add_argument('--window-size=1920,1080')  # Define the size of the window

driver = None  # Gives a default value for the driver

try:
    # Sets the service and starts the driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


    driver.get("https://www.example.com")
    driver.save_screenshot('screenshot.png')
    print("Acessou a URL com sucesso!")


    time.sleep(5)

except WebDriverException as e:
    print("Ocorreu um erro ao iniciar o navegador:", e)

finally:
    # close the driver
    if driver:
        driver.quit()

