from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
import getpass
import time 
from anticaptchaofficial.recaptchav2proxyless import *


keyboard = Controller()

# email = input('Adresse email : ')
password = getpass.getpass('Password:')

driver = webdriver.Firefox() 


url = 'https://play-stasis.net/login'
driver.get(url)

driver.maximize_window() 
time.sleep(2) 

button = driver.find_element(By.ID, 'email')
button.click()
button.send_keys('#adresse_email')

button2 = driver.find_element(By.ID, 'password')
button2.click()
button2.send_keys(password)

time.sleep(1)

connectButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/form/button')
connectButton.click()

time.sleep(5)

buttonVote = driver.find_element(By.CSS_SELECTOR, 'main aside .butt.vote')
buttonVote.click()

time.sleep(5)

# cookies = driver.get_cookies()
# name = cookies[1]['name']
# token = cookies[1]['value']
driver2 = webdriver.Firefox()
driver2.get("https://serveur-prive.net/dofus/stasis/vote")
# driver.add_cookie({
#     'name' : name,
#     'value' : token
# })

time.sleep(5)

buttonVote = driver2.find_element(By.CLASS_NAME, 'fc-cta-consent')
buttonVote.click()

time.sleep(15)

# lameumeu
pseudo = '#pseudo_perso_main'

pseudonyme = driver2.find_element(By.ID, 'username')
pseudonyme.click()
pseudonyme.send_keys(pseudo)

time.sleep(4)

vote = driver2.find_element(By.ID, 'voteBtn')
vote.click()

if driver2.find_elements(By.ID, 'email') : 
    emailBtn = driver2.find_element(By.ID, 'email')
    emailBtn.send_keys('#adresse_email')

    send_verification = driver2.find_element(By.ID, 'send_verification')
    send_verification.click()

    firefoxDriver = webdriver.Firefox() 
    firefoxDriver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=22&ct=1711828862&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26RpsCsrfState%3d8a64e9cf-2568-1460-aaf9-216cd8b3e7d6&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c')
    
    time.sleep(3)
    
    emailInput = firefoxDriver.find_element(By.ID, 'i0116')
    emailInput.send_keys('#adresse_email')

    sub = firefoxDriver.find_element(By.ID, 'idSIButton9')
    sub.click()

    time.sleep(3)
    passwordInput = firefoxDriver.find_element(By.ID, 'i0118')
    passwordInput.send_keys('#mdp_adresse-email')

    sub = firefoxDriver.find_element(By.ID, 'idSIButton9')
    sub.click()
    
    time.sleep(3)

    cancel = firefoxDriver.find_element(By.ID, 'declineButton')
    cancel.click()

    time.sleep(30)
    firstEmail = firefoxDriver.find_element(By.CSS_SELECTOR, 'div.XG5Jd')
    firstEmail.click()

    time.sleep(10)

    td = firefoxDriver.find_element(By.CSS_SELECTOR, 'td.x_content-cell')
    p = td.find_elements(By.TAG_NAME, 'p')

    print(p[1].text)

    code = p[1].text.split(':')[1].replace(" ", "")

    print(code)

    firefoxDriver.close()

    inputCode = driver2.find_element(By.ID, 'code')
    inputCode.send_keys(code)

    validation = driver2.find_element(By.ID, 'send_validation')
    validation.click()

    time.sleep(3)
    vote.click()

    time.sleep(5)
    vote.click()

    time.sleep(3)

btnSuccess = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/form/button')
btnSuccess.click()




time.sleep(100) 
# Close the driver
driver.close()


