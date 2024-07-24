from Credentials import *
import Naukri_Utilities as nu
import LinkedIn_Utilities as lu
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
'''
Apply only 20 jobs per hour
Apply at random intervals
logout for every one hour and ogin again after random intervals 
'''

def naukri():
    for i in range(0,10000):

        ## login to Naukri
        driver = nu.login_naukri(driver_path,naukri_login_id,naukri_password)

        ##update Profile Name and waits for 15min for next update
        nu.update_profileName(driver,driver_path,naukri_login_id,naukri_password)

        ## login to Naukri
        nu.logout_naukri(driver)

        sleep_time = random.randint(600, 900)
        time.sleep(sleep_time)

def linkedIn():

    ##login to LinkedIn
    driver = lu.login_linkedin(driver_path,linkedin_login_id,linkedin_password)

    ##Apply jobs
    lu.apply_jobs_linkedin(driver)

    ##logout
    lu.logout_linkedin(driver)

if __name__ == '__main__':
        naukri()
        # linkedIn()
