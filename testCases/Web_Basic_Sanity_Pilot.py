from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from Pagelement.fe_Page_Objects import fe_Objects
from Pagelement.fe_Page_Objects import fe_Sections
from Pagelement.fe_Page_Actions import fe_actions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from Pagelement.fe_Page_Objects import fe_texts

class Test_Websanity:
    service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    leagueurl = "https://fantasyapp.voot.com/kkk-12/10/kkk12/12"
    token = "?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQ" \
            "iOiJKRGNoekYxaU13Q3draDdtblE5R21pZEVrTlVsIiwidXNlck5h" \
            "bWUiOiJOZXcgVXNlIFR3byIsImxvZ2luUHJvdmlkZXIiOiJUcmFkaX" \
            "Rpb25hbCIsImdlbmRlciI6Ik0iLCJhZ2UiOiIzMS0wMy0xOTk1IiwibmFt" \
            "ZSI6Ik5ldyBVc2UgVHdvIiwiZW1haWwiOiJuZXd1c2VyMDAyQHZvb3QuY29t" \
            "IiwiVURJRCI6IkpEY2h6RjFpTXdDd2toN21uUTlHbWlkRWtOVWwiLCJzZXgi" \
            "OiJNIiwiZXh0cmFEYXRhIjoidm9vdCIsImlhdCI6MTY2MDY0MjY5NiwiZXhwIjox" \
            "NjkyMjAwMjk2fQ.HyILC5ZcEDTCtNAHBkXwRw3V0ZSMJ06JeDMjXLgpFJ4"
    driver.get(leagueurl + token)
    driver.maximize_window()
    driver.implicitly_wait(20)
    time.sleep(3)
    contestant_no = 6
    credit_score = "300.00"
    League_Name = "KKK12"
    create_team_url_parameter = "?league_id=12"
    team_preview_url_parameter = "?showId=10&leagueId=12"
    edit_team_url_parameter = "?isEdit=true&league_id=12"

    def test_001(self):
        # Land on the coach card page and check whether the coach card section is present or not.
        # Then check the icon, header and description text is displayed or not along with the continue button.

          try:
              self.driver.find_element(By.XPATH,fe_Sections.createteamicon)
              self.driver.find_element(By.XPATH,fe_Sections.createteamheadersx)
              self.driver.find_element(By.XPATH, fe_Sections.createteamparasx)
              self.driver.find_element(By.XPATH, fe_Sections.manageteamicon)
              self.driver.find_element(By.XPATH, fe_Sections.manageteamheadersx)
              self.driver.find_element(By.XPATH, fe_Sections.manageteamparasx)
              self.driver.find_element(By.XPATH, fe_Sections.trackperformanceicon)
              self.driver.find_element(By.XPATH, fe_Sections.trackperformanceheadersx)
              self.driver.find_element(By.XPATH, fe_Sections.trackperformanceparasx)
              self.driver.find_element(By.XPATH, fe_Objects.coachcardcontinue)
          except NoSuchElementException:
              self.driver.save_screenshot('Screenshots/ss1.png')
              assert False
          else:
              assert True



    def test_002(self):
        # check after clicking on continue the whether the user land on the create team page or not by verifying the url.
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.coachcardcontinue).click()
        if fe_texts.createteam_url == self.driver.current_url:
            assert True
        else:
            assert False

    def test_003(self):
        # check the logo and other header menu options are visible or not along with the create team section.

        try:
            self.driver.find_element(By.XPATH, fe_Objects.vflicon)
            self.driver.find_element(By.XPATH, fe_Objects.createteam2)
            self.driver.find_element(By.XPATH, fe_Objects.myleague)
            self.driver.find_element(By.XPATH, fe_Objects.leaderboard)
            self.driver.find_element(By.XPATH, fe_Objects.bonuspoint)
            self.driver.find_element(By.XPATH, fe_Objects.profileicon)
            self.driver.find_element(By.XPATH, fe_Sections.createteamsx)
        except NoSuchElementException:
            self.driver.save_screenshot('Screenshots/ss2.png')
            assert False
        else:
            assert True

    def test_004(self):
        # check the footer element is present or not
        try:
            self.driver.find_element(By.XPATH,fe_Sections.footersx)
            self.driver.find_element(By.XPATH,fe_Objects.terms_and_conditions)
            self.driver.find_element(By.XPATH,fe_Sections.reservedrightssx)
        except NoSuchElementException:
            self.driver.save_screenshot('Screenshots/ss3.png')
        else:
            assert True

    def test_005(self):
        time.sleep(2)
        # to check whether total no. of added contesntants are displayed or not by validating that number of contestant trays
        try:
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray1)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray2)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray3)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray4)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray5)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray6)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray7)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray8)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray9)
        except NoSuchElementException:
            self.driver.save_screenshot('Screenshots/ss4.png')
            assert False
        else:
            assert True

    def test_006(self):
        # to check the league name in create team section

        if self.driver.find_element(By.XPATH,fe_Sections.leaguenamesx2).text == self.League_Name:
            assert True
        else:
            assert False

    def test_007(self):
        # to check the credti score given to users
        expected_creditscore = "300.00"
        if self.driver.find_element(By.XPATH,fe_Sections.creditleftsx).text == self.credit_score:
            assert True
        else:
            assert False

    def test_008(self):
        # to check the league rules hyperlink by click on it and check whether the pop up appears or not.
        # to check when clicked on the cross icon, the league rule section disappear
        try:
            self.driver.find_element(By.XPATH,fe_Objects.leaguerulehyperlink).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,fe_Sections.leaguerulessx)
            time.sleep(1)
            self.driver.find_element(By.XPATH,fe_Objects.closeleaguerule).click()
        except NoSuchElementException:
            self.driver.save_screenshot('Screenshots/ss5.png')
            assert False
        else:
            assert True


    def test_009(self):
        # to check whether the create team button is disabled or not as the required number of contestant is not selected.
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        except WebDriverException:
            assert True
        else:
            assert False

    def test_011(self):
        # to check whether the user lands on my league page when clicked on my league from header options.
        # The check is done by comparing the url.
        self.driver.find_element(By.XPATH,fe_Objects.myleague).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.closedetails).click()
        if self.driver.current_url == fe_texts.myleague_url:
            assert True
        else:
            assert False

    def test_012(self):
        # To check when clicked on create team from my leage page then user lands on create team page or not.
        # this will be verified by comparing URL.
        time.sleep(15)
        self.driver.find_element(By.XPATH,fe_Objects.createteam3).click()
        time.sleep(1)
        if self.driver.current_url == (fe_texts.createteam_url + self.create_team_url_parameter):
            assert True
        else:
            assert False

    def test_013(self):
        # to check the when admin clicks on leaderbaord from header then user lands on it.
        # This will be done by comparing urls
        self.driver.find_element(By.XPATH,fe_Objects.leaderboard).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.leaderoard_url:
            assert True
        else:
            assert False

    def test_014(self):
        # to check the default validation message of leaderbaord page when team is not created
        if self.driver.find_element(By.XPATH,fe_Sections.leaderboardvalidtxtsx).text == fe_texts.leaderboardvalidationtxt:
            assert True
        else:
            assert False

    def test_015(self):
        # to check the when admin clicks on bonuspoint from header then user lands on it.
        # This will be done by comparing urls
        self.driver.find_element(By.XPATH,fe_Objects.bonuspoint).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.bonuspoints_url:
            assert True
        else:
            assert False

    def test_016(self):
        # to check the default validation message of Bonus page when team is not created
        if self.driver.find_element(By.XPATH,fe_Sections.bonusvalidtxtsx).text == fe_texts.bonusvalidationtxt:
            assert True
        else:
            assert False

    def test_017(self):
        # to check the when admin clicks on userprofile from header then user lands on it.
        # this will be checked by comparing url
        self.driver.find_element(By.XPATH,fe_Objects.profileicon).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.userprofile_url:
            assert True
        else:
            assert False

    def test_010(self):
        # to check when required number of contestant is selected then the create team button gets enabled or not.

        self.driver.find_element(By.XPATH,fe_Objects.createteam2).click()
        time.sleep(2)
        fe_actions.choosecontestants(self,self.contestant_no,startrange=2)
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        except WebDriverException:
            assert False
        else:
            assert True

    def test_0018(self):
        # to check the selected no. contestants are present for captain selection\
        # this check is done by comparing the  total no. of contestant trays present with the total no. added in team
        try:
            self.driver.find_element(By.XPATH,fe_Sections.contenstanttraycap1)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap2)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap3)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap4)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap5)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap6)
        except NoSuchElementException:
            self.driver.save_screenshot('Screenshots/ss6.png')
            assert False
        else:
            assert True

    def test_019(self):
        # to check the back button in choose captain page
        # this will checked by clicking on back and then veriy whether the previous seected contestants are still selected or not.
        self.driver.find_element(By.XPATH,fe_Objects.back3).click()
        time.sleep(1)
        fe_actions.checkforisselected(self,self.contestant_no,start_range=2)
        # if assert failed then ss will saved with name ss7

    def test_020(self):
        # to check when submit button is clcked without choosing captain, then validation message pop up appears or not
        # this is done by checking whether the pop up section
        self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        self.driver.find_element(By.XPATH,fe_Objects.submit1).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.choosecapvalidtionsx)
        except NoSuchElementException:
            assert False
        else:
            assert True

    def test_021(self):
        # to check when clicked on the ok button of captain validation message pop up, it disappears or not
        # this will be checked in a similar way the test_020, difference will on exception error it will be passed.
        self.driver.find_element(By.XPATH,fe_Objects.ok1).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        self.driver.find_element(By.XPATH,fe_Objects.submit1).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.choosecapvalidtionsx)
        except NoSuchElementException:
            assert True
        else:
            assert False

    def test_022(self):
        # to test whether the captain selected or not.
        # this will be checked by selecting the captain and then checking the same is selected or not.
        fe_actions.choosecaptain(self,1,1)

    def test_023(self):
        # to test the submkt button when captain is selcted
        # will be checked by validating the Name Your Team pop up.
        self.driver.find_element(By.XPATH,fe_Objects.submit1).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.nameyourteampopupsx)
        except NoSuchElementException:
            assert False
        else:
            assert True

    def test_024(self):
        # to check when the user tries click on start playing without putting up the team name.
        # this will be validated bu checking the presence of validation message section along with whether the message is correct or not
        self.driver.find_element(By.XPATH,fe_Objects.startplaying).click()
        try:
            tnvstxt = self.driver.find_element(By.XPATH,fe_Sections.teamnamevalidationsx).text
        except NoSuchElementException:
            assert False
        else:
            if tnvstxt == fe_texts.teamnamerequiredtxt:
                assert True
            else:
                assert False

    def test_025(self):
        # to check when team name entered and clicked on submit, it opens save team pop up
        # this will be done by checking the availability of Save Team Pop up
        fe_actions.enterteamname(self,"automated team 01")
        self.driver.find_element(By.XPATH,fe_Objects.startplaying).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.saveteampopupsx)
        except NoSuchElementException:
            assert False
        else:
            assert True

    def test_026(self):
        # to test when clicked on edit user lands on the create team section.
        # this will be done by comparing the presence of create team section.
        self.driver.find_element(By.XPATH,fe_Objects.back4).click()
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH,fe_Sections.createteamsx)
        except NoSuchElementException:
            assert False
        else:
            assert True

    def test_027(self):
        # to test when clicked on submit at save team the congratulations pop up comes or not.
        # this will be done by checking the congratulation pop up section presence.
        self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.submit1).click()
        self.driver.find_element(By.XPATH,fe_Objects.startplaying).click()
        self.driver.find_element(By.XPATH,fe_Objects.submit2).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.congratsteamcreated)
        except NoSuchElementException:
            assert False
        else:
            assert True

    def test_028(self):
        # to check when clicked on ok of congratuation pop up then user land on team preview opage
        # will be checked by comparing the url
        self.driver.find_element(By.XPATH,fe_Objects.ok1).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.teampreview_url + self.team_preview_url_parameter:
            assert True
        else:
            assert False

    def test_029(self):
        # to check for edit button in team preview page
        # this will be checked by comparing the url
        if self.driver.current_url == fe_texts.createteam_url + self.edit_team_url_parameter:
            assert True
        else:
            assert False

    def test_030(self):
        # to check conitnur to my league button
        # this will be done by comparing the url
        self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.submit1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.startplaying).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.submit2).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.ok1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.continuetomyleague).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.myleague_url:
            assert True
        else:
            assert False
