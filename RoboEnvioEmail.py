from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

site = "http://gmail.com"
email = "SEU EMAIL"
senha = "SUA SENHA"
assunto = "ASSUNTO DO EMAIL"
corpoEmail = "CORPO DO EMAIL"

#driver = webdriver.Opera()
driver = webdriver.Firefox()
time.sleep(2)
driver.get(site)
time.sleep(1)

#inserir email
emailgmail = driver.find_element_by_id("identifierId")
emailgmail.clear()
emailgmail.send_keys(email)
emailgmail.send_keys(Keys.RETURN)

#senrir senha
time.sleep(5)
senhagmail = driver.find_element_by_name("password")
senhagmail.clear()
senhagmail.send_keys(senha)
senhagmail.send_keys(Keys.RETURN)

#abrir campo de email
time.sleep(5)
driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
time.sleep(3)

#preencher o email
para = driver.find_element_by_name("to")
para.clear()
para.send_keys(email)

#preencher o assunto
assuntogmail = driver.find_element_by_name("subjectbox")
assuntogmail.clear()
assuntogmail.send_keys(assunto)

#preencher o corpo do email
corpo = driver.find_element_by_xpath("//div[@role='textbox']")
corpo.clear()
corpo.send_keys(corpoEmail)

#enviar o email
enviar = driver.find_element_by_xpath("//div[@aria-label='Enviar ‪(Ctrl-Enter)‬']")
enviar.click()

#fechar navegador
time.sleep(2)
driver.close()