
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def login_linkedin(driver_path,linkedin_login_id,linkedin_password):

    service = Service(executable_path=driver_path)

    options = webdriver.EdgeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Edge(options=options, service=service)

    driver.get("https://www.linkedin.com/home")
    driver.switch_to.window(driver.window_handles[-1])
    driver.maximize_window()
    time.sleep(5)

    ##click on signin button
    signin_button = driver.find_element("xpath","/html/body/nav/div/a[2]")
    signin_button.click()
    time.sleep(5)

    userid_textbox = driver.find_element("xpath","/html/body/div/main/div[2]/div[1]/form/div[1]/input")
    time.sleep(0.5)
    userid_textbox.send_keys(linkedin_login_id)

    pwd_textbox = driver.find_element("xpath","/html/body/div/main/div[2]/div[1]/form/div[2]/input")
    time.sleep(0.5)
    pwd_textbox.send_keys(linkedin_password)


    click_login = driver.find_element("xpath","/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    time.sleep(0.3)
    click_login.click()
    time.sleep(8)

    return driver

def apply_jobs_linkedin(driver):

    driver.get("https://www.linkedin.com/jobs/")

    role_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", '/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]'))
    )
    # click_job_button = driver.find_element("xpath","")
    role_filter.send_keys("Data Analyst")
    role_filter.send_keys(Keys.RETURN)
    time.sleep(4)

    # Apply "Easy Apply" filter
    # easy_apply_filter = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(("XPATH", '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button'))
    # )
    easy_apply_filter = driver.find_element("xpath","/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button")
    easy_apply_filter.click()
    time.sleep(4)


    # Date posted
    # date_posted = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(("XPATH", '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label/p/span[1]'))
    # )
    date_posted = driver.find_element("xpath","/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/span/button")
    date_posted.click()
    time.sleep(1)

    click_on_pas_week = driver.find_element("xpath","/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label/p/span[1]")
    click_on_pas_week.click()
    time.sleep(2)

    # Clcik Show results
    # show_results = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(("XPATH", '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span'))
    # )
    show_results = driver.find_element("xpath","/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]/span")
    show_results.click()
    time.sleep(3)
def logout_linkedin(driver):

    ## click on profile button
    profile_button = driver.find_element("xpath","/html/body/div[5]/header/div/nav/ul/li[6]/div/button/img")
    profile_button.click()
    time.sleep(0.5)

    ## click on logout
    logout_button = driver.find_element("xpath","/html/body/div[5]/header/div/nav/ul/li[6]/div/div")
    # logout_button = driver.find_element("ID","ember18")
    logout_button.click()
    time.sleep(3)


    driver.quit()


