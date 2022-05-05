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
coin_list_location = r"C:\Users\chris\Desktop\SanJuan\coins_to_sell.txt"
hold_list_location = r"C:\Users\chris\Desktop\SanJuan\coins_to_hold.txt"
loopBool = True
global startTime
global success
global no_coins
global coins_to_sell
#Removes navigator.webdriver flag
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("--start-maximized")
#Open Browser
driver = webdriver.Chrome(executable_path=PATH,options=option)
driver.implicitly_wait(10) # gives an implicit wait for 10 seconds

password_file_location = r"C:\Users\chris\Desktop\SanJuan\password.txt"
global password
password_file = open(password_file_location,"r")
password = password_file.readline()
print(password)
global check
check = 0
 
#email
email_file_location = r"C:\Users\chris\Desktop\SanJuan\email.txt"
global email
email_file = open(email_file_location,"r")
email = email_file.readline()
email_file.close()

def check_exists_by_css_selector(cssSelector):
    try:
        driver.find_element_by_css_selector(cssSelector)
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
        
        time.sleep(5)
        return True
        ##return CheckIfLoggedIn()
    
    except:
        print("login failed")
        return False

    

def CheckIfLoggedIn():
    if check_exists_by_css_selector("#__next > div.jsx-2883048944.app-layout > nav > div > div > ul.Navigation_actions__1u2Lu > li.Navigation_withBox__ViOBo > a > span"):
        print("logged in")
        return True
            
    else:
        print("username not detected...")
        return False
    



def GetSellList():

    try:
    
        #click on trade menu
        act1 = ActionChains(driver)
        parent_level_menu = driver.find_element_by_xpath("//*[@id='__next']/div[2]/nav/div/div/ul[2]/li[2]/a")
        act1.move_to_element(parent_level_menu).perform()
        ##click
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/nav/div/div/ul[2]/li[2]/a"))).click()
    

        #click on convert
        act2 = ActionChains(driver)
        parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[1]/div/ul/div[4]/a/div[2]/span/p")
        act2.move_to_element(parent_level_menu).perform()
        ##click
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/div/ul/div[4]/a/div[2]/span/p"))).click()

        #click on choose creator coin
        act4 = ActionChains(driver)
        parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/p[2]")
        act4.move_to_element(parent_level_menu).perform()
        ##click
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/p[2]"))).click()
        time.sleep(1)
        #get list of coins
        
        coins_to_sell = driver.find_elements_by_class_name("style_covertCoinName__qj_WJ")
        print("coins added to list")


        if not coins_to_sell:
            print("no coins to sell...")
            startTime = time.time()
            no_coins = True
            return True
        


        coin_list_file = open(coin_list_location,"w")
        for elements in(coins_to_sell):
        ##write new coin to file
            
            print(elements.text)
            coin_list_file.write(elements.text + "\n")
            

        coin_list_file.close()

        print("wrote to file")

        return True
    


    except:
        print("get list failed... trying again")
        ##while(not CheckIfLoggedIn()):
            ##login()

            
        return False





def SellCoins():
    print("attempting to sell")

    driver.refresh()
    time.sleep(2)
    


    try:
        #click on trade menu
        act1 = ActionChains(driver)
        parent_level_menu = driver.find_element_by_xpath("//*[@id='__next']/div[2]/nav/div/div/ul[2]/li[2]/a")
        act1.move_to_element(parent_level_menu).perform()
        ##click
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div[2]/nav/div/div/ul[2]/li[2]/a"))).click()
    

        #click on convert
        act2 = ActionChains(driver)
        parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[1]/div/ul/div[4]/a/div[2]/span/p")
        act2.move_to_element(parent_level_menu).perform()
        ##click
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/div/ul/div[4]/a/div[2]/span/p"))).click()

        #click on choose creator coin
        act4 = ActionChains(driver)
        parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/p[2]")
        act4.move_to_element(parent_level_menu).perform()
        ##click
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div/div/div[1]/div/p[2]"))).click()
        time.sleep(1)



        
        coins_to_sell = driver.find_elements_by_class_name("style_covertCoinName__qj_WJ")
        print("coins added to list again")

        ##read coin-file and place into list
        coin_list_file = open(coin_list_location,"r")
        filedList = coin_list_file.readlines()
        coin_list_file.close()


        holdFile = open(hold_list_location,"r")
        holding_coins = holdFile.readlines()
        holdFile.close()

        for element in filedList:
            if element in holding_coins:
                filedList.remove(element)
        
    
        for elements in coins_to_sell:

            ##check each element against filed list in
            if (elements.text + "\n") not in filedList:
                pass

            
            
            else:            
        
                print("did we get to the first one?")
                time.sleep(2)
                #click on coin
                act12 = ActionChains(driver)
                print("act 12 activated")
                time.sleep(1)
                act12.move_to_element(elements).perform()
                print("located coin")
                elements.click()
                print("clicked")
                
                time.sleep(1)
                #click on continue
                act13 = ActionChains(driver)
                parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div/button/span[1]")
                print("continue button located")
                act13.move_to_element(parent_level_menu).perform()
                ##click
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/button/span[1]"))).click()
                print("clicked")

                
                time.sleep(1)
                #click on max
                print("trying max")
                act14 = ActionChains(driver)
                parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/div/div[3]/p[4]")
                act14.move_to_element(parent_level_menu).perform()
                ##click
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[2]/div/div[3]/p[4]"))).click()

                time.sleep(1)
                #click on continue to confirmation
                act15 = ActionChains(driver)
                parent_level_menu = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div/button/span[1]")
                act15.move_to_element(parent_level_menu).perform()
                ##click
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div[3]/div/button/span[1]"))).click()
                
                time.sleep(1)
                #click on confirm
                act16 = ActionChains(driver)
                parent_level_menu = driver.find_element_by_css_selector("body > div.jss6 > div.TransactionModal_modal__2SZ5b > div.TransactionModal_footerWrap__2_NJj > div > button > span.MuiButton-label")
                act16.move_to_element(parent_level_menu).perform()
                ##click
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.jss6 > div.TransactionModal_modal__2SZ5b > div.TransactionModal_footerWrap__2_NJj > div > button > span.MuiButton-label"))).click()
                print("final confirm clicked - sell")

                time.sleep(2)
                

                coin_list_file = open(coin_list_location,"w")
                for number, line in enumerate(filedList):
                    if number not in [0]:
                        coin_list_file.write(line)

                        
                
                coin_list_file.close()
                print("wrote to file")
                return False



        return True


        
    except:
        print("Sell Coins Failed...trying again")
        
        return False




startTime = time.time()
success = False
no_coins = False
coins_to_sell = []


while(not login()):
    check = check + 1
    if(check > 4):
        driver.quit()
        exit()
        break
    else:
        continue
    


time.sleep(2)

while(not GetSellList()):   
    driver.refresh()
    continue



if(no_coins):
    driver.quit()

    

while(not SellCoins()):
    continue


print("finished")
driver.quit()



