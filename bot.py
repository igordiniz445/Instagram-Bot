from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from login import Login
from pathlib import Path
import time
import random

class InstagramBot:
    comment_count = 0
    def __init__(self, username, password, url, peopleNumber):

        self.login_index = 0
        self.username = []
        #Vetor de contas
        self.password = []
        #vetor de senhas
        self.igList = []
        #vetor com os ig para marcar

        self.username = username
        self.password = password
        self.url = url
        self.peopleNumber = peopleNumber
        #inicializadores

        self.comment_count = 0
        self.comment_errors = 0
        #contadores de comentário e erros

        self.igList = self.loadIgList()
        #Carrega a lista de ig's para o vetor
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-features=NetworkService")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        #Opcoes para o chrome sem "cabeçalho"

        self.driver = self.createInstanceOfDriver()
        #inicializador do navegador
        #self.driver = webdriver.Firefox(executable_path=str(Path(__file__).parent.absolute())+"\\geckodriver.exe")

    def createInstanceOfDriver(self):
        return webdriver.Chrome(options=self.chrome_options,executable_path=str(Path(__file__).parent.absolute())+"\\chromedriver.exe")

    #Função que carrega o arquivo de texto e salva os ig's no array
    def loadIgList(self):
        print("Carregando lista de pessoas...")
        try:
            filereader = open('lista_ig.txt','r')
            pessoas = []
            for usuarios in filereader:
                pessoas.append(usuarios)
            #Lê o arquivo linha por linha e salva os ig's
            print("Carregado com sucesso.")
            filereader.close()
            return pessoas
        except:
            print("Houve um erro ao carregar sua lista")
            exit()
        

    def relogar(self):
        oldriver = self.driver
        oldriver.close()
        self.driver = self.createInstanceOfDriver()
        #self.driver = webdriver.Firefox(executable_path=str(Path(__file__).parent.absolute())+"\\geckodriver.exe")
        time.sleep(3)
        driver = self.driver
        driver.get("https://www.instagram.com/?hl=pt-br")
        time.sleep(3)

        self.login_index += 1
        if(self.login_index >= len(self.username)):
            print("")
            print("Todas as contas já comentaram, e estão temporariamente sem poder comentar mais.\n")
            print("=====================================")
            print("Iniciando tempo de repouso de 3 horas")
            print("=====================================")
            self.login_index = 0
            time.sleep(10800)
            print("Retornando a tentativa de comentários... \n")

        
        time.sleep(3)
        campo_login = driver.find_element_by_xpath("//input[@name='username']")
        campo_login.click()
        campo_login.clear()
        campo_login.send_keys(self.username[self.login_index])

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password[self.login_index])

        campo_senha.send_keys(Keys.RETURN)    

        time.sleep(4)
        try:
            botao_salvar = driver.find_element_by_xpath("//button[@type='button']")
            #Se achar esse botão, significa que o login foi feito com sucesso.
            botao_salvar.click()
            time.sleep(3)
            print("Retomando os comentarios ...\n")
            time.sleep(2)
            driver.get(self.url)
            time.sleep(3)
            self.comentar_sorteio()
        except:
            print("Falha ao logar")
            exit()
        

        

    def begin(self):
        print("Fazendo Login na conta principal ... \n")
        driver = self.driver
        driver.get("https://www.instagram.com/?hl=pt-br")
        time.sleep(3)
        campo_login = driver.find_element_by_xpath("//input[@name='username']")
        campo_login.click()
        campo_login.clear()
        campo_login.send_keys(self.username[self.login_index])

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password[self.login_index])

        campo_senha.send_keys(Keys.RETURN)        

        time.sleep(4)
        try:
            botao_salvar = driver.find_element_by_xpath("//button[text()='Salvar informações']")
            #Se achar esse botão, significa que o login foi feito com sucesso.
            botao_salvar.click()
            time.sleep(3)
            driver.get(self.url)
            time.sleep(3)
            self.comentar_sorteio()
        except:
            print("Falha ao logar")
            exit()

    def type_like_a_person(self, user, field):
        indice = 0
        i = 0
        while(i < len(user)):
            indice = 0
            nome = user[i]
            while len(user[i])>4 and indice < len(user[i])-3:
                letra = nome[indice]
                field.send_keys(letra)
                time.sleep(random.randint(2,7)/30)
                indice += 1
            time.sleep(3)
            field.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            field.send_keys(Keys.RETURN)
            time.sleep(1)
            field.send_keys(Keys.SPACE)
            i += 1

    def selectPplToMark(self):
        users= []
        pplToMarkCounter = 1
        while(pplToMarkCounter <= self.peopleNumber):
            person = self.igList[random.randint(0,len(self.igList))]
            users.append(person)
            pplToMarkCounter += 1
        return users

    def comentar_sorteio(self):
        driver = self.driver
        
        try:
            campo_comentario = driver.find_element_by_xpath("//textarea[@aria-label='Adicione um comentário...']")
            campo_comentario.click()
            time.sleep(3)

            users = []
            users = self.selectPplToMark()
            i=0
            persons = "Marcando: "
            while(i<len(users)):
                persons += users[i]
                persons += " "
                i+=1
            print(persons)

            campox = driver.find_element_by_class_name('Ypffh')
            self.type_like_a_person(users, campox)

            botao_publicar = driver.find_element_by_xpath("//button[@type='submit']")
            #botao_publicar = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
            botao_publicar.click()
            
            self.comment_count += 1
            tempo_espera = random.randint(3, 6)
            print("Tempo de espera para próximo comentário: ",tempo_espera)
            time.sleep(tempo_espera)
            self.comentar_sorteio()
        except:
            self.comment_count -= 1
            print("Não foi possível comentar. Vamos tentar novamente mais algumas vezes\n")
            print("Quantidade de pessoas marcadas até agora: "+str(self.comment_count)+"\n")
            self.comment_errors += 1
            if(self.comment_errors >= 3):
                print("[===== Conta atual bloqueada, trocando de conta agora. =====]\n")
                self.relogar()
            else:
                driver.refresh()
                self.comentar_sorteio()
            

logins = []
senhas = []
print("")
print("Bem Vindo ao bot de comentários do instagram.\n")
count = int(input("Quantas contas vai logar? "))
i = 1
while(i<=count):
    print("Dados da conta "+str(i)+":")
    user = input("Digite o login: ")
    password = input("Digite a senha: ")
    login = Login(user, password)
    response = login.logar()
    if(response):
        print("Login feito com sucesso.\n")
        logins.append(user)
        senhas.append(password)
        i += 1
    else:
        print("Usuário ou senha incorreto, tente novamente:\n")


url = input("Digite a URL do post do sorteio: ")
peopleNumber = int(input("Quantidade de pessoas para serem marcadas no post: "))

bot = InstagramBot(logins,senhas,url, peopleNumber)
bot.begin()        


