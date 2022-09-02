from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



class fe_actions:

    def __init__(self,driver):
        self.driver = driver

    def choosecontestants(self,contestants_number,startrange):
        # choose number of contestants you want to add in team
        end_range = contestants_number + 2
        for i in range(startrange, end_range):
            # Select contestant first selected range contestants
            self.driver.find_element(By.XPATH,
                            f"//*[@id='wrapper']/div/app-create-team/section[2]/div"
                            f"/div/div[2]/table/tbody/tr[{i}]/td[3]/div/div/a").click()

    def choosecaptain(self,contestantnumber,selectioncheck):
        '''selection check 1 means yes and any other value will initiate the check. It will just choose the captain'''
        captain = contestantnumber + 2
        self.driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-create-team/"
                                          f"section[2]/div/div/div[3]/table/tbody/tr[{captain}]/td[3]/a").click()

        if selectioncheck == 1:
            sslcheck = self.driver.find_element(By.XPATH, "//*[@id='wrapper']/div/app-create-team/"
                                               f"section[2]/div/div/div[3]/table/tbody/tr[{captain}]/td[3]/a").is_selected()
            if sslcheck == True:
                assert True
            else:
                assert False
        else:
            pass


    def enterteamname(self,teamname):
        self.driver.find_element(By.XPATH, "/html/body/modal-container/"
                                           "div/div/div/div/form/div/input").send_keys(teamname)

    def enterdetails(self,mobilenumber,emailaddreaa):
        self.driver.find_element(By.XPATH,"//*[@id='user-contact-info-popup']/div/form/div/div[1]/input").send_keys(mobilenumber)
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='user-contact-info-popup']/div/form/div/div[4]/input").send_keys(emailaddreaa)
         #click on submit
        self.driver.find_element(By.XPATH,"//*[@id='user-contact-info-popup']/div/div/button").click()

    def checkforisselected(self,contestant_number,start_range):
        end_range = contestant_number + 2
        for i in range(start_range,end_range):
            if self.driver.find_element(By.XPATH,f"//*[@id='wrapper']/div/app-create-team/section[2]/div/div/div"
                                                 f"[2]/table/tbody/tr[{i}]/td[3]/div/div/a/span[2]").is_displayed() == True:
                assert True
            else:
                self.driver.save_screenshot('Screenshots/ss7.png')
                assert False
