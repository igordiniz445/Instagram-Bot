from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import random
from pathlib import Path

class Login:
    def __init__(self, user, password):
        print("Carregando navegador")
        self.user = user
        self.password = password

        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-features=NetworkService")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.chrome_options.add_argument("--disable-features=VizDisplayCompositor")

        self.driver = webdriver.Chrome(options=self.chrome_options,executable_path=str(Path(__file__).parent.absolute())+"\\chromedriver.exe")
        #self.driver = webdriver.Firefox(executable_path=str(Path(__file__).parent.absolute())+"\\geckodriver.exe")
    def logar(self):
        print("Testando login ... \n")
        driver = self.driver
        driver.get("https://www.instagram.com/?hl=pt-br")
        #//input[@name="username"]
        #//input[@password="password"]
        time.sleep(3)
        campo_login = driver.find_element_by_xpath("//input[@name='username']")
        campo_login.click()
        campo_login.clear()
        campo_login.send_keys(self.user)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)

        campo_senha.send_keys(Keys.RETURN)        

        time.sleep(4)
        try:
            botao_salvar = driver.find_element_by_xpath("//button[text()='Salvar informações']")
            #Se achar esse botão, significa que o login foi feito com sucesso.
            botao_salvar.click()
            driver.close()
            return True
        except:
            print("Falha ao logar")
            driver.close()
            return False

