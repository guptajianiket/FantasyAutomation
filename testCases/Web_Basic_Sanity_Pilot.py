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
import allure
from allure_commons.types import AttachmentType

'''Please make sure that the token which you are using has filled the user detail form.
Also review the data as in the score, league name, show and league id, user detail properly before initiating the test.
Also the user should not already have a team in this league.'''

# Currently the user detail test scenario has been removed in due to the feature change.

@allure.severity(allure.severity_level.NORMAL)
class Test_Websanity:
    service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    leagueurl = "https://fantasyapp.voot.com/sanity-check-show/7/form-check-league/14"
    token = "?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiJBV0VtTHJ0elpkR09ES1lYcXoxb3lsbXZzd3lSIiwidXNlck5hbWUiOiJUZXN0IEZvdXIiLCJsb2dpblByb3ZpZGVyIjoiVHJhZGl0aW9uYWwiLCJnZW5kZXIiOiJNIiwiYWdlIjoiMzEtMDMtMTk5NSIsIm5hbWUiOiJUZXN0IEZvdXIiLCJlbWFpbCI6InRlc3QwMDRAdm9vdC5jb20iLCJVRElEIjoiQVdFbUxydHpaZEdPREtZWHF6MW95bG12c3d5UiIsInNleCI6Ik0iLCJleHRyYURhdGEiOiJ2b290IiwiaWF0IjoxNjcxMTA0OTU1LCJleHAiOjE3MDI2NjI1NTV9.Y2pe-sH0qyWWLRtdXJyFARPFS-NsSiIIuSI8JwuKWPI"
    driver.get(leagueurl + token)
    driver.maximize_window()
    driver.implicitly_wait(20)
    time.sleep(3)
    contestant_no = 6 # match the number of trays in test case 005.
    credit_score = "1000.00"
    League_Name = "Form Check League"
    create_team_url_parameter = "?league_id=14"
    team_preview_url_parameter = "?showId=7&leagueId=14"
    edit_team_url_parameter = "?isEdit=true&league_id=14"
    user_name = "Test Four"
    user_email = "test004@voot.com"
    user_DOB = "31-03-1995"
    user_updated_email = ""
    user_number = "0870870870"
    user_rank = ""
    user_score = ""
    Name = "Test Four Updated"
    Mobile = "7987142066"
    Email = "test004updated@voot.com"
    City = "Kolkata"

    @allure.severity(allure.severity_level.MINOR)
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
              allure.attach(self.driver.get_screenshot_as_png(),name="SSTC_001",attachment_type=AttachmentType.PNG)
              assert False
          else:
              assert True


    @allure.severity(allure.severity_level.BLOCKER)
    def test_002(self):
        # check after clicking on continue the whether the user land on the create team page or not by verifying the url.
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.coachcardcontinue).click()
        if fe_texts.createteam_url == self.driver.current_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_002", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
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
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_003", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_004(self):
        # check the footer element is present or not
        try:
            self.driver.find_element(By.XPATH,fe_Sections.footersx)
            self.driver.find_element(By.XPATH,fe_Objects.terms_and_conditions)
            self.driver.find_element(By.XPATH,fe_Sections.reservedrightssx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_004", attachment_type=AttachmentType.PNG)
        else:
            assert True

    @allure.severity(allure.severity_level.CRITICAL)
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

        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_005", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_006(self):
        # to check the league name in create team section

        if self.driver.find_element(By.XPATH,fe_Sections.leaguenamesx2).text == self.League_Name:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_006", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_007(self):
        # to check the credit score given to users
        if self.driver.find_element(By.XPATH,fe_Sections.creditleftsx).text == self.credit_score:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_007", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
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
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_008", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_009(self):
        # to check whether the create team button is disabled or not as the required number of contestant is not selected.
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        except WebDriverException:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_009", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_011(self):
        # to check whether the user lands on my league page when clicked on my league from header options.
        # The check is done by comparing the url.
        self.driver.find_element(By.XPATH,fe_Objects.myleague).click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH,fe_Objects.closedetails).click() # need to think about this as the behaviour of closed details is been changed
        if self.driver.current_url == fe_texts.myleague_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_011", attachment_type=AttachmentType.PNG)
            assert False

    # since new implementation has been done wherein if the user detail pop up appear, the user must fill all the details, this test case has been introduced.

    @allure.severity(allure.severity_level.NORMAL)
    def test_049(self):
        # to check whether the pop up is there or not which is will be validated by checking the presence of the pop up section.
        try:
            self.driver.find_element(By.XPATH,fe_Sections.userdetailpopupsx)
        except WebDriverException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_049", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_050(self):
        # need to check the validation for every field when tried to submit the form.
        # this will be done, by clicking on submit button and then checking the presence of validation msg sectipn for every field.
        self.driver.find_element(By.XPATH,fe_Objects.udsubmitbutton).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.udnamevalidationsx)
            self.driver.find_element(By.XPATH,fe_Sections.udemailaddressvalidtionsx)
            self.driver.find_element(By.XPATH,fe_Sections.udmobilenumbervalidationsx)
            self.driver.find_element(By.XPATH,fe_Sections.udcityvalidationsx)
        except WebDriverException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_050", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_051(self):
        # need to test whether the form can be submitted or not after filling all the details.
        # that can be checked by filling all the fields and then clicking on submit, and then checking if the user detail pop is still there or not.
        self.driver.find_element(By.XPATH,fe_Objects.udnameinput).send_keys(self.Name)
        self.driver.find_element(By.XPATH,fe_Objects.udmobileinout).send_keys(self.Mobile)
        self.driver.find_element(By.XPATH,fe_Objects.udemailaddress).send_keys(self.Email)
        self.driver.find_element(By.XPATH,fe_Objects.udcity).send_keys(self.City)
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.udsubmitbutton).click()

        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH,fe_Sections.userdetailpopupsx)
        except WebDriverException:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_051", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_012(self):
        # To check when clicked on create team from my leage page then user lands on create team page or not.
        # this will be verified by comparing URL.
        time.sleep(15)
        self.driver.find_element(By.XPATH,fe_Objects.createteam3).click()
        time.sleep(1)
        if self.driver.current_url == (fe_texts.createteam_url + self.create_team_url_parameter):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_012", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_013(self):
        # to check the when admin clicks on leaderbaord from header then user lands on it.
        # This will be done by comparing urls
        self.driver.find_element(By.XPATH,fe_Objects.leaderboard).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.leaderoard_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_013", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_014(self):
        # to check the default validation message of leaderbaord page when team is not created
        if self.driver.find_element(By.XPATH,fe_Sections.leaderboardvalidtxtsx).text == fe_texts.leaderboardvalidationtxt:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_014", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_015(self):
        # to check the when admin clicks on bonuspoint from header then user lands on it.
        # This will be done by comparing urls
        self.driver.find_element(By.XPATH,fe_Objects.bonuspoint).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.bonuspoints_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_015", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_016(self):
        # to check the default validation message of Bonus page when team is not created
        if self.driver.find_element(By.XPATH,fe_Sections.bonusvalidtxtsx).text == fe_texts.bonusvalidationtxt:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_016", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_017(self):
        # to check the when admin clicks on userprofile from header then user lands on it.
        # this will be checked by comparing url
        self.driver.find_element(By.XPATH,fe_Objects.profileicon).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.userprofile_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_017", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_010(self):
        # to check when required number of contestant is selected then the create team button gets enabled or not.

        self.driver.find_element(By.XPATH,fe_Objects.createteam2).click()
        time.sleep(7)
        fe_actions.choosecontestants(self,self.contestant_no,startrange=2)
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        except WebDriverException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_010", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_018(self):
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
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_018", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_019(self):
        # to check the back button in choose captain page
        # this will checked by clicking on back and then veriy whether the previous seected contestants are still selected or not.
        self.driver.find_element(By.XPATH,fe_Objects.back3).click()
        time.sleep(1)
        fe_actions.checkforisselected(self,self.contestant_no,start_range=2)
        allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_019", attachment_type=AttachmentType.PNG)
        # if assert failed then ss will saved with name ss7

    @allure.severity(allure.severity_level.NORMAL)
    def test_020(self):
        # to check when submit button is clcked without choosing captain, then validation message pop up appears or not
        # this is done by checking whether the pop up section
        self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.submit1).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.choosecapvalidtionsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_020", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_021(self):
        # to check when clicked on the ok button of captain validation message pop up, it disappears or not
        # this will be checked in a similar way the test_020, difference will on exception error it will be passed.
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.ok1).click()
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH,fe_Sections.choosecapvalidtionsx)
        except NoSuchElementException:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_021", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_022(self):
        # to test whether the captain selected or not.
        # this will be checked by selecting the captain and then checking the same is selected or not.
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']/div/app-create-team/"
                                           "section[2]/div/div/div[3]/table/tbody/tr[2]/td[3]/a").click()

        sslcheck = self.driver.find_element(By.CLASS_NAME, 'sel-captain.selected').is_enabled()
        if sslcheck == True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_022", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_023(self):
            # to test the submkt button when captain is selcted
            # will be checked by validating the Name Your Team pop up.
            time.sleep(2)
            self.driver.find_element(By.XPATH,fe_Objects.submit1).click()
            try:
                self.driver.find_element(By.XPATH,fe_Sections.nameyourteampopupsx)
            except NoSuchElementException:
                allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_023", attachment_type=AttachmentType.PNG)
                assert False
            else:
                assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_024(self):
        # to check when the user tries click on start playing without putting up the team name.
        # this will be validated bu checking the presence of validation message section along with whether the message is correct or not
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.startplaying).click()
        try:
            tnvstxt = self.driver.find_element(By.XPATH,fe_Sections.teamnamevalidationsx).text
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_024NoSchElmnt", attachment_type=AttachmentType.PNG)
            assert False
        else:
            if tnvstxt == fe_texts.teamnamerequiredtxt:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_024Others", attachment_type=AttachmentType.PNG)
                assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_025(self):
        # to check when team name entered and clicked on submit, it opens save team pop up
        # this will be done by checking the availability of Save Team Pop up
        time.sleep(2)
        fe_actions.enterteamname(self,"automated team 01")
        self.driver.find_element(By.XPATH,fe_Objects.startplaying).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.saveteampopupsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_025", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_026(self):
        # to test when clicked on edit user lands on the create team section.
        # this will be done by comparing the presence of create team section.
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.back4).click()
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH,fe_Sections.createteamsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_026", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_027(self):
        # to test when clicked on submit at save team the congratulations pop up comes or not.
        # this will be done by checking the congratulation pop up section presence.
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.createteam1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.submit1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.startplaying).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.submit2).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.congratsteamcreated)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_027", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_028(self):
        # to check when clicked on ok of congratuation pop up then user land on team preview opage
        # will be checked by comparing the url
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.ok1).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.teampreview_url + self.team_preview_url_parameter:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_028", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_029(self):
        # to check for edit button in team preview page
        # this will be checked by comparing the url
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.edit1).click()
        if self.driver.current_url == fe_texts.createteam_url + self.edit_team_url_parameter:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_029", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_030(self):
        # to check continue to my league button
        # this will be done by comparing the url
        # in this user is clicking from team edit page till team preview page
        time.sleep(2)
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
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_030", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_031(self):
        # to check whether the league tray is present or not
        # this will be by checking the availability of the league tray section
        try:
            self.driver.find_element(By.XPATH,fe_Sections.leaguetraysx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_031", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_032(self):
        # to check the league name
        if self.driver.find_element(By.XPATH,fe_Sections.leaguenamesx3).text == self.League_Name:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_032", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_033(self):
        # to check the total score info pop up
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.leaguepointsview).click()
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH,fe_Sections.totalscoreinfosx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_033", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.NORMAL)
    def test_034(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Objects.ok3).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,fe_Sections.teamdetailsx).click()
        time.sleep(1)
        # to check whether the number of added contestants are there or not in the league
        fe_actions.checkforaddedcontenstant(self,self.contestant_no,1)
        allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_034", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.MINOR)
    def test_035(self):
        # to check the presence of captain tag in the first contestant
        # this will be done by checking the presennce of captain tag section
        try:
            self.driver.find_element(By.XPATH,fe_Sections.captaintagsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_035", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.BLOCKER)
    def test_036(self):
        # to check the user profile icon functionality
        # this will be checked by clicking on it and the comparing the url

        self.driver.find_element(By.XPATH,fe_Objects.profileicon).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.userprofile_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_036", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_037(self):
        # to verify the user name
        if self.driver.find_element(By.XPATH,fe_Sections.username2sx).text == self.user_name:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_037", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_038(self):
        # to verify the user email address
        # now since this was written before, the new mandatory user detail pop up implementation, the test cases is written in a way that it will give
        # true only when the updated email address is there and if the old one or anyother is there it will give false.
        # In future there will be case added wherein the user profile will be checked twice, once before user filling the user detal pop up and one after.
        if self.driver.find_element(By.XPATH,fe_Sections.useremailsx).text == self.user_email:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_038useremail", attachment_type=AttachmentType.PNG)
            assert False
        elif self.driver.find_element(By.XPATH,fe_Sections.useremailsx).text == self.Email:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_038Email", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_039(self):
        # to verify the user DOB
        if self.driver.find_element(By.XPATH,fe_Sections.DOBsx).text == self.user_DOB:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_039", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_040(self):
        # tp verify the user joined league status
        try:
            joined_league = self.driver.find_element(By.XPATH,fe_Sections.no_of_joined_league).text
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_040NoSchElmnt", attachment_type=AttachmentType.PNG)
            assert False
        else:
            if joined_league == "1":
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_040not1status", attachment_type=AttachmentType.PNG)
                assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_041(self):
        # to verify the looged in user's name, rank and score in leader board in comparision to the data given in my league page.
        self.driver.find_element(By.XPATH, fe_Objects.myleague).click()
        time.sleep(2)
        self.user_rank = self.driver.find_element(By.XPATH, fe_Sections.rank1sx).text
        self.user_score= self.driver.find_element(By.XPATH, fe_Objects.leaguepointsview).text
        # to verify the user name
        self.driver.find_element(By.XPATH,fe_Objects.leaderboard).click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH,fe_Sections.username1sx).text == self.user_name:
            un = 1
        else:
            un = 0

        # to verify the user rank
        if self.driver.find_element(By.XPATH,fe_Sections.rank2sx).text == self.user_rank:
            ur = 1
        else:
            ur = 0

        # to verify the user score
        if self.driver.find_element(By.XPATH,fe_Sections.pointssx).text == self.user_score:
            us = 1
        else:
            us = 0

        if un and us and ur == 1:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_041", attachment_type=AttachmentType.PNG)
            assert False, f"Value of un:,{un}" \
                          f"Value of us:, {us}" \
                          f"Value of ur:, {ur}"

    @allure.severity(allure.severity_level.MINOR)
    def test_042(self):
        # to check the terms and conditions hypoerlink text
        # will be checked by comparing urls
        self.driver.find_element(By.XPATH,fe_Objects.terms_and_conditions).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.termsandcondtions_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_042", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_043(self):
        # to check the presence of TnC section in TnC Page
        try:
            self.driver.find_element(By.XPATH,fe_Sections.tnc_sx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_043", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_044(self):
        # to check the back button functionality of the TnC Page
        # will be cchecked by comparing the url of the previous visited page i.e. leaderboard page
        self.driver.find_element(By.XPATH,fe_Objects.back1).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.leaderoard_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_044", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_045(self):
        # tp check when user after creating team lands again on the create team page, the already created pop up appears or not
        # this will checked by validating the presence of the pop up section
        self.driver.find_element(By.XPATH,fe_Objects.createteam2).click()
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, fe_Sections.alreadycreateamteam_sx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_045", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_046(self):
        # to check when the already created team validation message
        if self.driver.find_element(By.XPATH,fe_Sections.alreadycreatedteamtxt_sx).text == fe_texts.alreadycreateteam_txt:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_046", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_047(self):
        # to check the fucntionality of back button in already created team pop up
        self.driver.find_element(By.XPATH,fe_Objects.back2).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.leaderoard_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_047", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_048(self):
        # to check the go to my legaue button functionality of the already created team pop up
        # this will be checked when the user will land again on the create team page by clicking on create team in header
        # and then go to my legaue button will be clicked and url will be compared
        self.driver.find_element(By.XPATH,fe_Objects.createteam2).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,fe_Objects.gotomyleague).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.myleague_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_048", attachment_type=AttachmentType.PNG)
            assert False

