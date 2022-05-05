from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pprint
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


##variables
PATH = "C:/Program Files (x86)/chromedriver.exe"
password_file_location = r"C:\Users\chris\Desktop\SanJuan\password.txt"
loopBool = True
startTime = time.time()
#Removes navigator.webdriver flag
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--start-maximized")
#Open Browser
driver = webdriver.Chrome(executable_path=PATH,options=option)
driver.implicitly_wait(10) # gives an implicit wait for 10 seconds
wait = WebDriverWait(driver,10)

#email
email_file_location = r"C:\Users\chris\Desktop\SanJuan\email.txt"
global email
email_file = open(email_file_location,"r")
email = email_file.readline()
email_file.close()
print(email)

#email_pass
email_password_file_location = r"C:\Users\chris\Desktop\SanJuan\email_password.txt"
global email_password
email_password_file = open(email_password_file_location,"r")
email_password = email_password_file.readline()
email_password_file.close()

password_file = open(password_file_location,"r")
global password
password = password_file.readline()
password_file.close()
global number
number = int(password[-1])
print(number)
if(number > 8):
    number = 1

else:
    number = number + 1





def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_css_selector(cssSelector):
    try:
        driver.find_element_by_css_selector(cssSelector)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_class(item):
    try:
        driver.find_element_by_class_name(item)
    except NoSuchElementException:
        return False
    return True


def login():
    try:
        ##load login page
        driver.get("https://rally.io/resetpassword/")
        time.sleep(2)
        
        #fill email
        email_field = driver.find_element_by_name("email")
        email_field.send_keys(email)


        #click Send button
        loginButton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[1]/form/div/button")
        loginButton.click()

        time.sleep(60)
       
    except:
        print("change password failed")
        return False

    return True



def AccessEmail():
    driver.get("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    time.sleep(2)

    email_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    email_field.send_keys(email)

    loginButton2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
    loginButton2.click()

    time.sleep(3)

    password_field = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    password_field.send_keys(email_password)

    loginButton3 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
    loginButton3.click()

    time.sleep(3)
    search = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[2]/div[2]/form/div[1]/table/tbody/tr/td/table/tbody/tr/td/div/input[1]")
    search.send_keys("rally")

    searchButton = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[2]/div[2]/form/button[4]")
    searchButton.click()

    time.sleep(3)
    
    firstEmail = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div/table/tbody/tr[1]")
    firstEmail.click()

    time.sleep(2)

    
    link = driver.find_element_by_link_text("clicking here")
    link.click()

    time.sleep(3)
    
    p = driver.current_window_handle
    chwd = driver.window_handles

    for w in chwd:
    #switch focus to child window
        if(w!=p):
            driver.switch_to.window(w)
        
    print(password[:-1] + str(number))
    newpass = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[1]/form/div/div[2]/input[1]")
    newpass.send_keys(password[:-1] + str(number))

    newpass2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[1]/form/div/div[2]/input[2]")
    newpass2.send_keys(password[:-1] + str(number))

    
    password_file = open(password_file_location,"w")
    password_file.write(password[:-1] + str(number))
    password_file.close()

    completeButton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[1]/form/div/div[3]/div/button")
    completeButton.click()

    time.sleep(3)
    
    
##run login method
while(not login()):
    continue



AccessEmail()
driver.quit()


