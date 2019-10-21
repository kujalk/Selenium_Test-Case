#import required modules
from selenium import webdriver
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

#Specifiy the browser driver location
driver = webdriver.Chrome("C:/Users/jana/Downloads/chromedriver_win32/chromedriver.exe")

#Web page links
driver.get("https://accounts.google.com/signin")

if driver.title!="Sign in – Google accounts":
    print ("Error opening page!!!!")
    sys.exit(1)

else:

    #Login into page
    try:

        #Adding user login name
        username = driver.find_element_by_id("identifierId")
        username.clear()
        username.send_keys("Testmail@gmail.com")
        time.sleep(2) # Actually no need but to see in slow motion

        #Clicking "Next"
        #Wait until particular web element is loaded
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "CeoRYc", " " ))]')))
        element=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "CeoRYc", " " ))]')
        driver.execute_script("arguments[0].click();", element)

        print ("Successfully moved to password page")

    except Exception as E:
        print ("Problem while moving to other page : "+str(E))
        sys.exit(1)
      
    #Going to insert password
    try:

        #Adding password for login
        #Wait until particular web element is loaded
        time.sleep(2)
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.NAME, 'password')))
        password = driver.find_element_by_name("password")
        password.clear()  
        #Password
        password.send_keys("xxxxxx")
        time.sleep(2) # Actually no need but to see in slow motion

        #Clicking "Next"
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "CeoRYc", " " ))]')))
        element=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "CeoRYc", " " ))]')
        driver.execute_script("arguments[0].click();", element)

        if driver.title!="Google accounts":
            print ("Error opening page!!!!")
            sys.exit(1)
        else:
            print ("Successfully logged into GMail")
        
    except Exception as E:
        print ("Problem while moving to emailpage : "+str(E))
        sys.exit(1)

