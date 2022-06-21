from selenium import webdriver
import time
def getInput():
    who = input("To whom: ")
    theMessage = input("What is the message: ")
    howMany = int(input("How many times: "))
    return who, theMessage, howMany

def goToWhatsapp():
    driver = webdriver.Chrome("C:\webdrivers\chromedriver_win32\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    return driver

def waitForQRcode(driver):
    # for each in range(150):
    #     print("Countdown {} sec.".format((150 - each - 1)/10))
    #     time.sleep(0.1)
    # print("Here you go ;)")
    ready = input("are you ready? y/n ")
    while True:
        if ready == "n":
            continue
        else:
            break
        
def sendMessage(driver,howMany,theMessage,who):
    driver.find_element_by_xpath("""//*[@id="side"]/div[1]/div/label/div/div[2]""").send_keys(who + "\n")
    startTime = time.time()
    for each in range(howMany):
        driver.find_element_by_xpath("""//*[@id="main"]/footer/div[1]/div[2]/div/div[2]""").send_keys(theMessage + "\n")
    print("Done spamming in {} seconds".format(time.time() - startTime))

def Whatsapp(who,theMessage,howMany):
    driver = goToWhatsapp()
    waitForQRcode(driver)
    sendMessage(driver,howMany,theMessage,who)

def AreYouReady():
    while True:
        rdy = input("Are you ready? y or n \n")
        if rdy == "y":
            break
        else:
            continue

def goToTeleAndLogin():
    driver = webdriver.Chrome("C:\webdrivers\chromedriver_win32\chromedriver.exe")
    driver.maximize_window()
    driver.get("""https://web.telegram.org/#/login""")
    time.sleep(6)
    driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[1]/div""").click()
    driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[1]/input""").send_keys("iran")
    driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/div[2]/div/div[1]/ul/li/a""").click()
    driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input""").send_keys("9398328523\n")
    driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]""").click()
    return driver

def sendMessageInTele(who,theMessage,howMany,driver):
    startTime = time.time()
    for each in range(howMany):
        driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]""").send_keys(theMessage + "\n")   
    print("Done spamming in {} seconds".format(time.time() - startTime))
    

def Telegram(who,theMessage,howMany):
    driver = goToTeleAndLogin()
    AreYouReady()
    driver.find_element_by_xpath("""//*[@id="ng-app"]/body/div[1]/div[2]/div/div[1]/div[1]/div/input""").send_keys(who + "\n")
    sendMessageInTele(who,theMessage,howMany,driver)

def bothTeleWhatsapp(who,theMessage,howMany):
    driverTele = goToTeleAndLogin()
    driverWa = goToWhatsapp()
    AreYouReady()
    driverTele.find_element_by_xpath("""//*[@id="ng-app"]/body/div[1]/div[2]/div/div[1]/div[1]/div/input""").send_keys(who + "\n")
    driverWa.find_element_by_xpath("""//*[@id="side"]/div[1]/div/label/div/div[2]""").send_keys(who + "\n")
    for each in range(howMany):
        driverTele.find_element_by_xpath("""//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]""").send_keys(theMessage + "\n")   
        driverWa.find_element_by_xpath("""//*[@id="main"]/footer/div[1]/div[2]/div/div[2]""").send_keys(theMessage + "\n")
        time.sleep(1)

    
if __name__ == '__main__':
    whichOne = int(input("Whatsapp (1) or telegram (2) or both (3)? \n"))
    who , theMessage , howMany = getInput()
    if whichOne == 1:
        Whatsapp(who,theMessage,howMany)
    elif whichOne == 2:
        Telegram(who,theMessage,howMany)
    elif whichOne == 3:
       bothTeleWhatsapp(who,theMessage,howMany)