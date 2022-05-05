from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pprint
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import sys

##variables
PATH = "C:/Program Files (x86)/chromedriver.exe"
coin_list_location = r"C:\Users\chris\Desktop\SanJuan\coinlist.txt"
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
global coinArray
coin_list_file = open(coin_list_location,"r")
coinArray = coin_list_file.readlines()
coin_list_file.close()
global newCoin

global password
password_file = open(password_file_location,"r")
password = password_file.readline()
print(password)

#email
email_file_location = r"C:\Users\chris\Desktop\SanJuan\email.txt"
global email
email_file = open(email_file_location,"r")
email = email_file.readline()
email_file.close()


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
        driver.get("https://rally.io/login/")
        time.sleep(2)
        
        #fill email
        email_field = driver.find_element_by_name("email")
        email_field.send_keys(email)

        #fill password
        passwordinput = driver.find_element_by_name("password")
        passwordinput.send_keys(password)

        #click login button
        loginButton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/section/div/div[1]/form/div[3]/button")
        loginButton.click()

        time.sleep(2)
        warningButton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/img[2]")
        warningButton.click()
        
        print("login successful")
        time.sleep(5)
    except:
        print("login failed")
        return False

    return True




    

    
def BuyProcess():
    ##time.sleep(1)
    #click on trade menu
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/nav/div/div/ul[2]/li[2]/a")))
    act1 = ActionChains(driver)
    button1 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/nav/div/div/ul[2]/li[2]/a")
    act1.move_to_element(button1).perform()
    ##click
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/nav/div/div/ul[2]/li[2]/a"))).click()
    

    #click on convert
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div/div/div[2]/div/ul/div[2]/a/div[2]")))
    act2 = ActionChains(driver)
    button2 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/ul/div[2]/a/div[2]")
    act2.move_to_element(button2).perform()
    ##click
    button2.click()


##    #click on swap
##    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[2]/div/div[1]/div[2]/img")))
##    act3 = ActionChains(driver)
##    button3 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div[1]/div[2]/img")
##    act3.move_to_element(button3).perform()
##    ##click
##    button3.click()


    #click on choose creator coin
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/p[2]")))
    act4 = ActionChains(driver)
    button4 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/p[2]")
    act4.move_to_element(button4).perform()
    ##click
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/p[2]"))).click()


## get coinlist
    time.sleep(1)
    list_of_elements = driver.find_elements_by_class_name("style_covertCoinName__qj_WJ")
    coin_list_file = open(coin_list_location,"w")

    for elements in (list_of_elements):
        coin_list_file.write(elements.text + "\n")

    coin_list_file.close()
    driver.quit()
    

    
    ##read coin-file and place into list
    
    

    #get list of coins
    list_of_elements = driver.find_elements_by_class_name("style_covertCoinName__qj_WJ")
    for elements in (list_of_elements):
        
        ##check each element against filed list in reverse
                
        if (elements.text + "\n") in (coinArray):
            
            pass
            
        else:

            ##write new coin to file
            newCoin = elements.text + "\n"
            coinArray.append(elements.text +"\n")
            
            #click on coin
            act5 = ActionChains(driver)
            act5.move_to_element(elements).perform()
            elements.click()


            #click on continue
            wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[3]/div/button/span[1]")))
            act6 = ActionChains(driver)
            button5 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div/button/span[1]")
            act6.move_to_element(button5).perform()
            ##click
            ##WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/button/span[1]"))).click()
            button5.click()

            driver.implicitly_wait(1)
            
            wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[2]/div/input")))
            ##limit buy
            if(check_exists_by_class("style_fairLaunchTextWrap__165nU")):
                #click on max
                print("trying max")
                act7 = ActionChains(driver)
                parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div[4]/p[4]")
                act7.move_to_element(parent_level_menu).perform()
                ##click
                WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div[4]/p[4]"))).click()

                
                #click on continue to confirmation
                act8 = ActionChains(driver)
                parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div/button/span[1]")
                act8.move_to_element(parent_level_menu).perform()
                ##click
                WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/button/span[1]"))).click()

                wait.until(EC.presence_of_element_located((By.CLASS_NAME,"MuiButton-label")))
                
                #click on final confirm
                act8 = ActionChains(driver)
                button7 = driver.find_element_by_class_name("MuiButton-label")
                act8.move_to_element(button7).perform()
                ##click
                ##button7.click()
                WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, "MuiButton-label"))).click()
                print("final confirm clicked - limit buy")

        
                

            ##no limit buy - $1000
            else:

                print("attempting to find input")
                email = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/input")
                email.send_keys("4000")
                
                #click on continue to confirmation
                wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[3]/div/button/span[1]")))
                act7 = ActionChains(driver)
                button6 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div/button/span[1]")
                act7.move_to_element(button6).perform()
                ##click
                WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/button/span[1]"))).click()
                ##button6.click()
                
                wait.until(EC.presence_of_element_located((By.CLASS_NAME,"MuiButton-label")))
                
                #click on final confirm
                act8 = ActionChains(driver)
                button7 = driver.find_element_by_class_name("MuiButton-label")
                act8.move_to_element(button7).perform()
                ##click
                ##button7.click()
                WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, "MuiButton-label"))).click()
                print("final confirm clicked - no limit buy")

             
            
            print ("bought new coin")
            coin_list_file = open(coin_list_location,"a")
            coin_list_file.write(newCoin)
            coin_list_file.close()
            wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[2]/div/img")))
            
            break
                    
                    






##run login method
while(not login()):
    continue


##run buy loop
while(loopBool):

    print("start loop")
    time.sleep(1)


    try:
        BuyProcess()

    except:

        print ("Something went wrong...")   
        driver.refresh()
        driver.implicitly_wait(5) 

        ##checking if still logged in
        if check_exists_by_xpath("/html/body/div[1]/div[2]/nav/div/div/ul[2]/li[1]/a"):
            print("trade available, refreshing")
            continue
        else:
            while(not login()):
                continue


    
    print ("refreshing")
    driver.refresh()
    ##restart loop
    

    if (time.time()-startTime) > 60*60*5:
        loopBool = False



print("end program")
driver.quit()

