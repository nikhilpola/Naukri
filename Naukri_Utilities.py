import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def login_naukri(driver_path,naukri_login_id,naukri_password):
    service = Service(executable_path=driver_path)

    options = webdriver.EdgeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Edge(options=options, service=service)

    driver.get("https://www.naukri.com/mnjuser/homepage")
    driver.switch_to.window(driver.window_handles[-1])
    driver.maximize_window()
    time.sleep(5)

    user_name = driver.find_element("xpath","/html/body/div[3]/div/div/div/div/div/div/div/div[2]/div/form/div[2]/div[1]/div/input")
    pwd = driver.find_element("xpath","/html/body/div[3]/div/div/div/div/div/div/div/div[2]/div/form/div[2]/div[2]/div/input")

    user_name.send_keys(naukri_login_id)
    time.sleep(0.5)
    pwd.send_keys(naukri_password)
    time.sleep(0.5)

    ##Click on Login
    Login_button = driver.find_element("xpath","/html/body/div[3]/div/div/div/div/div/div/div/div[2]/div/form/div[2]/div[3]/div/button[1]")
    Login_button.click()
    time.sleep(5)
    return driver

def update_profileName(driver,driver_path,naukri_login_id,naukri_password):

    ##Click on Profile
    homepage_profile_button = driver.find_element("xpath","/html/body/div[3]/div[2]/div[4]/div")
    homepage_profile_button.click()
    time.sleep(2)

    ##Click on View&Update profile
    view_updateprofile = driver.find_element("xpath","/html/body/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[1]/div[2]/a")
    view_updateprofile.click()
    time.sleep(5)

    ## Click on Edit button Beside name
    Name_edit_button = driver.find_element("xpath","/html/body/div[3]/div/div/span/div/div/div/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/em")
    Name_edit_button.click()
    time.sleep(2)

    ##Name input
    name_input = driver.find_element("xpath","/html/body/div[6]/div[10]/div[2]/div/form/div[2]/div/input")
    current_name = name_input.get_attribute("value")
    if current_name == "Nikhil Kumar Pola":
        new_name = "Nikhil Kumar"
    else:
        new_name = "Nikhil Kumar Pola"
    name_input.clear()
    name_input.send_keys(new_name)
    time.sleep(0.5)


    ##Click on Save button
    save_button = driver.find_element(By.ID, "saveBasicDetailsBtn")  # Replace with actual ID
    save_button.click()
    time.sleep(3)



def logout_naukri(driver):

    ## click on profile button
    profile_button = driver.find_element("xpath","/html/body/div[2]/div[3]/div[2]/div[4]/div/div[2]/img")
    profile_button.click()
    time.sleep(0.5)

    ## click on logout
    logout_button = driver.find_element("xpath","/html/body/div[2]/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[3]/div/div[1]/div[4]/a")
    logout_button.click()
    time.sleep(3)


    driver.quit()


