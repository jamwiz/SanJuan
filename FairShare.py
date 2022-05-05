from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pprint
import time
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


##variables
PATH = "C:/Program Files (x86)/chromedriver.exe"

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

#password
password_file_location = r"C:\Users\chris\Desktop\SanJuan\password.txt"
global password
password_file = open(password_file_location,"r")
password = password_file.readline()
password_file.close()

#email
email_file_location = r"C:\Users\chris\Desktop\SanJuan\email.txt"
global email
email_file = open(email_file_location,"r")
email = email_file.readline()
email_file.close()
print(email)

global check
check = 0

global loopBool
loopBool = True

global balanceBool
balanceBool = True

global emailBool
emailBool = True

global writeBool
writeBool = True






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
        emailinput = driver.find_element_by_name("email")
        emailinput.send_keys(email)

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



def GetBalance():

    calculations_file_location = r"C:\Users\chris\Desktop\SanJuan\calculations.txt"
    calculations_file = open(calculations_file_location,"r")
    calc_list = calculations_file.readlines()
    calculations_file.close()

    global initial
    global myShare
    global yourShare
    global balance
    global recentGains
    global totalGains

    global cashBalance

    global initialInt
    global myShareInt
    global yourShareInt
    global balanceInt
    global recentGainsInt
    global totalGainsInt

    global cashBalanceInt

    global rate
    

    rez = []
    for x in calc_list:
        rez.append(x.replace("\n", ""))

    initial = rez[0]
    myShare = rez[1]
    yourShare = rez[2]
    balance = rez[3]
    recentGains = rez[4]
    totalGains = rez[5]

    print(initial)
    print(myShare)
    print(yourShare)
    print(balance)
    print(recentGains)
    print(totalGains)


    initialInt = int(initial)
    myShareInt = int(myShare)
    yourShareInt = int(yourShare)
    balanceInt = int(balance)
    recentGainsInt = int(recentGains)
    totalGainsInt = int(totalGains)
    
    balanceObj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[3]/a/div[3]/div[2]")
    balance = balanceObj.text
    balance = balance[:-5]
    balance = balance.split('.',1)[0]
    balance = balance.replace(',', '')
    print(balance)
    balanceInt = int(balance)

    cashBalanceObj = driver.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div[2]/div[1]/div[3]/a/div[3]/div[1]")
    cashBalance = cashBalanceObj.text
    cashBalance = cashBalance[:-3]
    cashBalance = cashBalance.replace(',', '')
    cashBalance = cashBalance.replace('$', '')
    cashBalanceInt = int(cashBalance)

    rate = cashBalanceInt/balanceInt

    print(rate)

    recentGainsInt = int(balanceInt - (initialInt + totalGainsInt))
    myShareInt = int(recentGainsInt/2)
    yourShareInt = int(myShareInt)
    totalGainsInt = int(totalGainsInt + yourShareInt)
    

    if(totalGainsInt > 7296 ):
        myShareInt = myShareInt + initialInt
        initialInt = 0
        
    balanceInt = balanceInt - myShareInt
    cashBalanceInt = balanceInt * rate

    myShare = str(myShareInt)
    yourShare = str(yourShareInt)
    recentGains = str(recentGainsInt)
    totalGains = str(totalGainsInt)
    initial = str(initialInt)
    balance = str(balanceInt)

    

def writeToFile(initial,myShare,yourShare,balance,recentGains,totalGains):
    print("attempting to write to file")
    calculations_file_location = r"C:\Users\chris\Desktop\SanJuan\calculations.txt"
    calculations_file = open(calculations_file_location,"w")

    
    calculations_file.write(initial + "\n")
    calculations_file.write(myShare + "\n")
    calculations_file.write(yourShare + "\n")
    calculations_file.write(balance + "\n")
    calculations_file.write(recentGains + "\n")
    calculations_file.write(totalGains)

    calculations_file.close()
    print("wrote to file")




    
def EmailReport():
    driver.get("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    time.sleep(2)

    email2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    email2.send_keys(email)

    loginButton2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
    loginButton2.click()

    time.sleep(3)

    password2 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    password2.send_keys("bachlava1")

    loginButton3 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
    loginButton3.click()

    time.sleep(3)

    act9 = ActionChains(driver)
    composeButton = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div")
    act9.move_to_element(composeButton).perform()
    composeButton.click()
    time.sleep(3)

    email3 = driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[1]/div[5]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/textarea")
    email3.send_keys(email)
    time.sleep(1)

    email3.submit
    time.sleep(1)
    
    subject = driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[1]/div[5]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/input")
    subject.send_keys("Gains Report")
    time.sleep(1)


    content = driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[1]/div[5]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div")
    cashBalanceInt = rate * balanceInt
    cashBalance = str(cashBalanceInt)
    content.send_keys("Balance: $" + str(round(cashBalanceInt)) + "\n" + "Recent Gains: $" + str(round(yourShareInt * rate, 2)) + "\n" + "Total Gains: $" + str(round(totalGainsInt * rate, 2)))

    time.sleep(1)


    act12 = ActionChains(driver)
    sendButton = driver.find_element_by_xpath("/html/body/div[17]/div/div/div/div[1]/div[5]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]")
    act12.move_to_element(sendButton).perform()
    sendButton.click()
    time.sleep(3)
    
    


    
    


    
def BuyTilt():
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


    #click on choose creator coin
    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/p[2]")))
    act4 = ActionChains(driver)
    button4 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/p[2]")
    act4.move_to_element(button4).perform()
    ##click
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div/div[2]/div/p[2]"))).click()


    #get list of coins
    list_of_elements = driver.find_elements_by_class_name("style_covertCoinName__qj_WJ")
 
        
    for elements in (list_of_elements):
                 
        if (elements.text != "$TILT") :
            
            pass
            
        else:

            #click on coin
            act5 = ActionChains(driver)
            act5.move_to_element(elements).perform()
            elements.click()


            #click on continue
            wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[3]/div/button/span[1]")))
            act6 = ActionChains(driver)
            button5 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div/button/span[1]")
            act6.move_to_element(button5).perform()
            button5.click()
            
            wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[2]/div/input")))



            print("attempting to find input")
            email = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/input")
            email.send_keys(myShare)
            
            #click on continue to confirmation
            wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div[3]/div/button/span[1]")))
            act7 = ActionChains(driver)
            button6 = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div/button/span[1]")
            act7.move_to_element(button6).perform()
            ##click
            WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/button/span[1]"))).click()
            
            
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,"MuiButton-label")))
            
            #click on final confirm
            act8 = ActionChains(driver)
            button7 = driver.find_element_by_class_name("MuiButton-label")
            act8.move_to_element(button7).perform()
            ##WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, "MuiButton-label"))).click()
            print("final confirm clicked - no limit buy")
            time.sleep(5)

             
            
            print ("bought TILT")
            
            
            
            break
                    
                    






##run login method
while(not login()):
    check = check + 1
    if(check > 5):
        driver.quit()
        exit()
    else:
        continue
    


check = 0

while(balanceBool):
    try:
        
        GetBalance()
        balanceBool = False

    except:
        continue
        
        


while(writeBool):
    try:
        
        writeToFile(initial,myShare,yourShare,balance,recentGains,totalGains)
        writeBool = False

    except:
        continue
        


while(loopBool):
    
    print("start loop")
    time.sleep(1)


    try:
        BuyTilt()
        loopBool = False

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
                check = check + 1
                if(check > 4):
                    break
                else:
                    continue


    
    print ("refreshing")
    driver.refresh()
    ##restart loop

while(emailBool):
    try:
        
        EmailReport()
        emailBool = False

    except:
        continue
        


print("end program")
driver.quit()

