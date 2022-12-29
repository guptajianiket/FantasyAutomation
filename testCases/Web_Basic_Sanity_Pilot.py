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

# TO DO
'''
17-12-2022
1. Need to put a check for user detail pop up in testcases for my league page. 
'''

# Currently, the user detail test scenario has been removed in due to the feature change.

@allure.severity(allure.severity_level.NORMAL)
class Test_Websanity:

    # Test Case Documentation URLs
    # This section is for allure reports
    testcasereport = "https://moraviait-my.sharepoint.com/:x:/g/personal/anigupta_moravia_com/EfP285he4TZMkmbtv7qCVIUBlZ32Jf-tfggx7CD1JJMKUg?e=S9BFmB"
    testcasedocument = "https://moraviait-my.sharepoint.com/:w:/g/personal/anigupta_moravia_com/ETq9D_2FRG9At5IHN1JY9FwBCK3YKC5vry8hhhKEVtJAjA?e=iYk53U"

    # This represents the number of contestants you want to add in your team.
    # Make sure to enter the number under league limits.

    # Mandatory Objects
    leagueurl = "https://fantasyapp.voot.com/sanity-check-show/7/form-check-league/14"
    token = "?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiJDWldRVGs1dnFXWjZsY092ekh5S0hrZ2ZHYnkwIiwidXNlck5hbWUiOiJBdXRvbWF0YSBUZW4iLCJsb2dpblByb3ZpZGVyIjoiVHJhZGl0aW9uYWwiLCJnZW5kZXIiOiJNIiwiYWdlIjoiMzEtMDMtMTk5NSIsIm5hbWUiOiJBdXRvbWF0YSBUZW4iLCJlbWFpbCI6ImF1dG9tYXRhMDEwQHZvb3QuY29tIiwiVURJRCI6IkNaV1FUazV2cVdaNmxjT3Z6SHlLSGtnZkdieTAiLCJzZXgiOiJNIiwiZXh0cmFEYXRhIjoidm9vdCIsImlhdCI6MTY3MjIyNTQ5NywiZXhwIjoxNzAzNzgzMDk3fQ.IngeENWaj_Fp4VqloclgB7dPzDbDeqEfUmG7AcDb2aw"
    credit_score = "1000.00"
    League_Name = "Form Check League"
    create_team_url_parameter = "?league_id=14"
    team_preview_url_parameter = "?showId=7&leagueId=14"
    edit_team_url_parameter = "?isEdit=true&league_id=14"
    user_name = "Automata Ten"
    user_email = "automata010@voot.com"
    user_DOB = "31-03-1995"
    user_number = "1111111111"
    contestant_no = 10


    # Non-Mandatory Objects
    user_rank = ""
    user_score = ""

    # User Entry Objects
    Name = "automata Ten"
    Mobile = "1111111110"
    Email = "automata010updated@voot.com"
    City = "Kolkata"

    path = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
    driver = webdriver.Chrome(service=path)
    driver.get(leagueurl + token)
    driver.maximize_window()
    driver.implicitly_wait(20)
    time.sleep(3)

    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Coach Card Elements Check")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "coach card")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Check for the presence of create team icon element. "
                 "2. Check for the presence of create team section text element. "
                 "3. Check for the presence of create team description text element. "
                 "4. Check for the presence of manage team icon element. "
                 "5. Check for the presence of manage team section text element. "
                 "6. Check for the presence of manage team description text element. "
                 "7. Check for the presence of track performance icon element. "
                 "8. Check for the presence of track performance text element. "
                 "9. Check for the presence of track performance description text element. "
                 "10. Check for the presence of the coach card continue button element. ")
    def test_001(self):
        """To check Whether coach card page elements are present are not."""
        # Land on the coach card page and check whether the coach card section is present or not.
        # Then check the icon, header and description text is displayed or not along with the continue button.

        try:
            self.driver.find_element(By.XPATH, fe_Sections.createteamicon)
            self.driver.find_element(By.XPATH, fe_Sections.createteamheadersx)
            self.driver.find_element(By.XPATH, fe_Sections.createteamparasx)
            self.driver.find_element(By.XPATH, fe_Sections.manageteamicon)
            self.driver.find_element(By.XPATH, fe_Sections.manageteamheadersx)
            self.driver.find_element(By.XPATH, fe_Sections.manageteamparasx)
            self.driver.find_element(By.XPATH, fe_Sections.trackperformanceicon)
            self.driver.find_element(By.XPATH, fe_Sections.trackperformanceheadersx)
            self.driver.find_element(By.XPATH, fe_Sections.trackperformanceparasx)
            self.driver.find_element(By.XPATH, fe_Objects.coachcardcontinue)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_001", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Coach Card Continue Button")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "coach card")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Click on continue button of coach card section. "
                 "2. Verify the landing page url. ")
    def test_002(self):
        """ To check the continue button functionality of coach card. """
        # check after clicking on continue the whether the user land on the create team page,
        # or not by verifying the url.
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.coachcardcontinue).click()
        time.sleep(2)
        if fe_texts.createteam_url == self.driver.current_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_002", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Header Element")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "coach card")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Check the presence of Voot Fantasy Logo element in header. "
                 "2. Check the presence of Create Team option element in header. "
                 "3. Check the presence of My League option element in header. "
                 "4. Check the presence of Leaderboard option element in header. "
                 "5. Check the presence of bonus point option element in header. "
                 "6. Check the presence of profile icon option element in header. "
                 "7. Check the presence of create team section in create team page.")
    def test_003(self):
        """To check whether the logo and header menu is visible or not."""
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
    @allure.title("Footer Element")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "footer")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Check the presence of footer section element. "
                 "2. Check the presence of terms and condition hyperlinked text element. "
                 "3. Check the presence of reserved rights text element. ")
    def test_004(self):
        """To check the footer element."""
        # check the footer element is present or not
        try:
            self.driver.find_element(By.XPATH, fe_Sections.footersx)
            self.driver.find_element(By.XPATH, fe_Objects.terms_and_conditions)
            self.driver.find_element(By.XPATH, fe_Sections.reservedrightssx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_004", attachment_type=AttachmentType.PNG)
        else:
            assert True

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Contestant List")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Check the expected number of contestants trays are present.")
    def test_005(self):
        """To check the presence of all the contestants added in the league in create team page."""
        time.sleep(2)
        # to check whether total no. of added contestants are displayed,
        # or not by validating that number of contestant trays.
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
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray10)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttray11)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_005", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.MINOR)
    @allure.tittle("League Name in Create team")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Get the league name from opened create team page. "
                 "2. Compare it with the given name in the script. ")
    def test_006(self):
        """To verify the league name in the create team section."""
        # to check the league name in create team section

        if self.driver.find_element(By.XPATH, fe_Sections.leaguenamesx2).text == self.League_Name:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_006", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Credit Score")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Get the credit score from opened create team page. "
                 "2. Compare it with the given credit score in the script. ")
    def test_007(self):
        """To validate the credit score given to the users."""
        # to check the credit score given to users
        if self.driver.find_element(By.XPATH, fe_Sections.creditleftsx).text == self.credit_score:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_007", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("League Rule")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Click on the league rule hyperlink. "
                 "2. Check the presence of league rule box. "
                 "3. Click on cross button. ")
    def test_008(self):
        """To check the functionality of league rules section."""
        # to check the league rules hyperlink by click on it and check whether the pop-up appears or not.
        # to check when clicked on the cross icon, the league rule section disappear.
        try:
            self.driver.find_element(By.XPATH, fe_Objects.leaguerulehyperlink).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, fe_Sections.leaguerulessx)
            time.sleep(1)
            self.driver.find_element(By.XPATH, fe_Objects.closeleaguerule).click()
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_008", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Create Team Button")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Click  on the create team button. "
                 "2. Check for an Web Driver Exception error since button is disabled.")
    def test_009(self):
        """To check the functionality of create team button when required number contestants are not added."""
        # to check whether the create team button is disabled or not,
        # as the required number of contestant is not selected.
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, fe_Objects.createteam1).click()
        except WebDriverException:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_009", attachment_type=AttachmentType.PNG)
            assert False


    @allure.title("My League Header Button")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("1. Click on the my league option from header. "
                 "2. Get the current url. "
                 "3. Compare with the saved one in script.")
    def test_010(self):
        """To check the functionality of my league option from the header menu."""
        # to check whether the user lands on my league page when clicked on my league from header options.
        # The check is done by comparing the url.
        self.driver.find_element(By.XPATH, fe_Objects.myleague).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.myleague_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_010", attachment_type=AttachmentType.PNG)
            assert False


    @allure.title("User Detail Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Search for user detail pop up container. ")
    def test_011(self):
        """To validate the presence of user detail pop up in my league page."""
        # To check whether the pop-up is there or not which will be validated,
        # by checking the presence of the pop-up section.
        try:
            self.driver.find_element(By.XPATH, fe_Sections.userdetailpopupsx)
        except WebDriverException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_011", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("User Detail Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on submit without filling any field. "
                 "2. Search for validation message elements of each field. ")
    def test_012(self):
        """To verify whether the validation error message appear or not for every field,
         when tried to submit by keeping all fields blank."""
        # need to check the validation for every field when tried to submit the form.
        # this will be done, by clicking on submit button and then checking the presence,
        # of validation msg section for every field.
        time.sleep(3)
        self.driver.find_element(By.XPATH, fe_Objects.udsubmitbutton).click()
        try:
            self.driver.find_element(By.XPATH, fe_Sections.udnamevalidationsx)
            self.driver.find_element(By.XPATH, fe_Sections.udemailaddressvalidtionsx)
            self.driver.find_element(By.XPATH, fe_Sections.udmobilenumbervalidationsx)
            self.driver.find_element(By.XPATH, fe_Sections.udcityvalidationsx)
        except WebDriverException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_012", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("User Detail Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("1. Fill all the fields in user detail pop up. "
                 "2. Click on Submit. "
                 "3. Search for user detail pop up container."
                 "4. Check for an webdriver exception since the pop up should be closed.")
    def test_013(self):
        """To check whether the user detail pop up gets submitted when all the fields are filled properly."""
        # need to test whether the form can be submitted or not after filling all the details.
        # that can be checked by filling all the fields and then clicking on submit,
        # and then checking if the user detail pop is still there or not.
        self.driver.find_element(By.XPATH, fe_Objects.udnameinput).send_keys(self.Name)
        self.driver.find_element(By.XPATH, fe_Objects.udmobileinout).send_keys(self.Mobile)
        self.driver.find_element(By.XPATH, fe_Objects.udemailaddress).send_keys(self.Email)
        self.driver.find_element(By.XPATH, fe_Objects.udcity).send_keys(self.City)
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.udsubmitbutton).click()

        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH, fe_Sections.userdetailpopupsx)
        except WebDriverException:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_013", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Create Team Button")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("1. Click on the create team button in league tray. "
                 "2. Get the current url. "
                 "3. Compare the current url with the saved create team url in the script. ")
    def test_014(self):
        """To check the create team button functionality from my league section."""
        # To check when clicked on create team from my league page then user lands on create team page or not.
        # this will be verified by comparing URL.
        time.sleep(15)
        self.driver.find_element(By.XPATH, fe_Objects.createteam3).click()
        time.sleep(1)
        if self.driver.current_url == (fe_texts.createteam_url + self.create_team_url_parameter):
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_014", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Leaderboard Button")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "leaderboard")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("1. Click on leaderboard from the header menu. "
                 "2. Get the current url. "
                 "3. Compare the current url with the saved leaderboard url in the script. ")
    def test_015(self):
        """To check the functionality of leaderboard button in header menu."""
        # to check when admin clicks on leaderboard from header then user lands on it.
        # This will be done by comparing urls
        self.driver.find_element(By.XPATH, fe_Objects.leaderboard).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.leaderoard_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_015", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Leaderboard Page Message")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "leaderboard")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Get the text from the page."
                 "2. Compare the current text with the saved default message text of"
                 "leaderboard page in the script. ")
    def test_016(self):
        """To validate the default message displayed in the leaderboard page before creating the team."""
        # to check the default validation message of leaderboard page when team is not created
        if self.driver.find_element(By.XPATH, fe_Sections.leaderboardvalidtxtsx).text == \
                fe_texts.leaderboardvalidationtxt:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_016", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Bonus Point Page")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "bonuspoint")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("1. Click on the bonus point from the header menu. "
                 "2. Get the current url. "
                 "3. Compare the current url with the saved 'bonuspoint' url in the script. ")
    def test_017(self):
        """To check the functionality of the bonus point option of header menu."""
        # to check when admin clicks on bonus point option from header then user lands on it.
        # This will be done by comparing urls
        self.driver.find_element(By.XPATH, fe_Objects.bonuspoint).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.bonuspoints_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_017", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Bonus Point Page Message")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "bonuspoint")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.step("1. Get the text from the page. "
                 "2. Compare the current text from the saved default message of bonuspoint text in the script.")
    @allure.severity(allure.severity_level.MINOR)
    def test_018(self):
        """ To verify the default message of bonus page when there is no active bonus point."""
        # to check the default validation message of Bonus page when team is not created
        if self.driver.find_element(By.XPATH, fe_Sections.bonusvalidtxtsx).text == fe_texts.bonusvalidationtxt:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_018", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("User Profile Icon")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "user profile")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("1. Click on the user profile icon on the header menu. "
                 "2. Get the current url. "
                 "3. Compare the current url with the saved user profile url in the script. ")
    def test_019(self):
        """To check the functionality of user profile icon in header menu."""
        # to check when admin clicks on userprofile from header then user lands on it.
        # this will be checked by comparing url
        self.driver.find_element(By.XPATH, fe_Objects.profileicon).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.userprofile_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_019", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Create Team Button")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("1. Click on the create team on header. "
                 "2. Click on plus icon of 10 each contestant tray. "
                 "3. Click on the create team button present after contestant tray. ")
    def test_020(self):
        """To check whether the create team button in the create team page gets
        enabled or not when minimum required players are added."""
        # To check when required number of contestant is selected then the create team button gets enabled or not.
        self.driver.find_element(By.XPATH, fe_Objects.createteam2).click()
        time.sleep(7)
        fe_actions.choosecontestants(self, self.contestant_no, startrange=2)
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, fe_Objects.createteam1).click()
        except WebDriverException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_020", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("Choose Captain Section")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("1. Check for the contestant tray, there should be ten. ")
    def test_021(self):
        """ To verify whether, all added contestants are visible or not."""
        # to check the selected no. contestants are present for captain selection
        # this check is done by comparing the  total no. of contestant trays present with the total no. added in team
        try:
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap1)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap2)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap3)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap4)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap5)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap6)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap7)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap8)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap9)
            self.driver.find_element(By.XPATH, fe_Sections.contenstanttraycap10)

        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_021", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("Choose Captain Section")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on back button. "
                 "2. Since you will land on contestant selection page, check whether all the previously"
                 "contestant are selected or not.  ")
    def test_022(self):
        """To verify the function of the back button of choose captain section."""
        # to check the back button in choose captain page
        # this will be checked by clicking on back and then verify
        # whether the previous selected contestants are still selected or not.
        self.driver.find_element(By.XPATH, fe_Objects.back3).click()
        time.sleep(1)
        fe_actions.checkforisselected(self, self.contestant_no, start_range=2)
        allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_022", attachment_type=AttachmentType.PNG)

    @allure.title("Choose Captain Validation Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("1. Since currently user is in create team page where the contestants are already selected."
                 "Click on the create team button. "
                 "2. Then without selecting captain click on submit. "
                 "3. Check for captain selection validation pop up container. ")
    def test_023(self):
        """To verify choose captain validation pop up."""
        # to check when submit button is clicked without choosing captain,
        # then validation message pop up appears or not.
        # this is done by checking whether the pop-up section.
        self.driver.find_element(By.XPATH, fe_Objects.createteam1).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.submit1).click()
        try:
            self.driver.find_element(By.XPATH, fe_Sections.choosecapvalidtionsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_023", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("Choose Captain Validation Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on Ok Button. "
                 "2. Check for the captain validation pop up container. ")
    def test_024(self):
        """To verify the functionality of ok button in choose captain validation pop up."""
        # to check when clicked on the ok button of captain validation message pop up, it disappears or not
        # this will be checked in a similar way the test_020, difference will on exception error it will be passed.
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.ok1).click()
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, fe_Sections.choosecapvalidtionsx)
        except NoSuchElementException:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_024", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Choose Captain Section")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("1. Click on 'C' icon. "
                 "2. Then check the same icon is getting selected or not.")
    def test_025(self):
        """ To verify whether the captain is getting selected or not. """
        # to test whether the captain selected or not.
        # this will be checked by selecting the captain and then checking the same is selected or not.
        self.driver.find_element(By.XPATH, "//*[@id='wrapper']/div/app-create-team/"
                                           "section[2]/div/div/div[3]/table/tbody/tr[2]/td[3]/a").click()

        sslcheck = self.driver.find_element(By.CLASS_NAME, 'sel-captain.selected').is_enabled()
        if sslcheck is True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_025", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Choose Captain Submit Button")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("1. Click on the submit button. "
                 "2. Check for Name your team pop up container. ")
    def test_026(self):
        """ To check the submit button functionality. """
        # to test the submit button when captain is selected.
        # will be checked by validating the Name Your Team pop up.
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.submit1).click()
        try:
            self.driver.find_element(By.XPATH, fe_Sections.nameyourteampopupsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_026", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("Enter Team Name Pop up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on start playing. "
                 "2. Check whether validation text is present or not."
                 "3. Get the validation text."
                 "4. Compare the current validation text with the saved one in script. ")
    def test_027(self):
        """To verify the validation pop up for team name."""
        # to check when the user tries click on start playing without putting up the team name.
        # this will be validated by checking the presence of validation message section along
        # with whether the message is correct or not.
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.startplaying).click()
        try:
            tnvstxt = self.driver.find_element(By.XPATH, fe_Sections.teamnamevalidationsx).text
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_027NoSchElement",
                          attachment_type=AttachmentType.PNG)
            assert False
        else:
            if tnvstxt == fe_texts.teamnamerequiredtxt:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_027Others",
                              attachment_type=AttachmentType.PNG)
                assert False


    @allure.title("Enter Team Name Pop up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("1. Enter the team name. "
                 "2. Click on start playing. "
                 "3. Check for save team pop up container. ")
    def test_028(self):
        """To verify the submit button functionality of name your team pop up."""
        # to check when team name entered and clicked on submit, it opens save team pop up
        # this will be done by checking the availability of Save Team Pop up
        time.sleep(2)
        fe_actions.enterteamname(self, "automated team 01")
        self.driver.find_element(By.XPATH, fe_Objects.startplaying).click()
        try:
            self.driver.find_element(By.XPATH, fe_Sections.saveteampopupsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_028", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("Save Team Pop up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on back button. "
                 "2. Since you landed on the create team section where contestants are selected."
                 " Check for contestants container. ")
    def test_029(self):
        """To verify the functionality of the back button in save team pop up."""
        # to test when clicked on edit of  user lands on the create team section.
        # this will be done by comparing the presence of create team section.
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.back4).click()
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, fe_Sections.createteamsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_029", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("Save Team Pop up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Since you are at the create team section. "
                 "2. Click on the create team button. "
                 "3. Click on the submit button. "
                 "4. Click on start playing button. "
                 "5. Click on save team button. "
                 "6. Check for congratulation pop up. ")
    def test_030(self):
        """To validate functionality of submit button of save team pop up."""
        # to test when clicked on submit at save team the congratulations pop up comes or not.
        # this will be done by checking the congratulation pop up section presence.
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.createteam1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.submit1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.startplaying).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.submit2).click()
        try:
            self.driver.find_element(By.XPATH, fe_Sections.congratsteamcreated)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_030", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("Save Team Pop up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on the ok button. "
                 "2. Get the current url. "
                 "3. Compare the current url with the saved url in the script.")
    def test_031(self):
        """To check the functionality of ok button in congratulation pop up."""
        # to check when clicked on ok of congratulation pop up then user land on team preview page
        # will be checked by comparing the url
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.ok1).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.teampreview_url + self.team_preview_url_parameter:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_031", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Team Preview Page")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "team preview")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on the edit button. "
                 "2. Get the current URL. "
                 "3. Compare the cuurent URL with the saved one in script. ")
    def test_032(self):
        """To check the functionality of edit button in team preview page."""
        # to check for edit button in team preview page
        # this will be checked by comparing the url
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.edit1).click()
        if self.driver.current_url == fe_texts.createteam_url + self.edit_team_url_parameter:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_032", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Team Preview Page")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "team preview")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Since the user is back to the create team section, user will click on create team button. "
                 "2. Click on Submit button. "
                 "3. Click on Start Playing button. "
                 "4. Click on Submit button. "
                 "5. Click on Ok button. "
                 "6. Click on 'Continue to my league' button. "
                 "7. Get the current url. "
                 "8. Compare the current url with the saved one in the script. ")
    def test_033(self):
        """To check the 'continue to my league' button functionality in team preview page."""
        # to check continue to my league button
        # this will be done by comparing the url
        # in this user is clicking from team edit page till team preview page
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.createteam1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.submit1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.startplaying).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.submit2).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.ok1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.continuetomyleague).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.myleague_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_033", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Check For User Detail Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "user detail")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("1. Check for the presence of User Detail Pop Up Container. "
                 "2. In Case yes, enter all the required data and click on continue. ")
    def test_052(self):
        """To check for users who have already filled the user detail pop up, whether coming back to
        my league page shows the user detail pop up or not. """
        # this will be checked by checking the presence of the user detail pop up container element.
        #
        try:
            self.driver.find_element(By.XPATH,fe_Sections.userdetailpopupsx)
        except WebDriverException:
            assert True
        else:
            fe_actions.enteruserdetail(self,self.Name,self.Email,self.Mobile,self.City)
            assert False


    @allure.title("League Tray")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("1. Check for the league tray element. ")
    def test_034(self):
        """To verify the presence of league tray in my league page."""
        # to check whether the league tray is present or not
        # this will be by checking the availability of the league tray section
        time.sleep(6)
        try:
            self.driver.find_element(By.XPATH, fe_Sections.leaguetraysx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_034", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("League Name")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Get the current league name. "
                 "2. Compare the current league name with the saved one in the script.")
    def test_035(self):
        """To verify the league name in my league page."""
        # to check the league name
        if self.driver.find_element(By.XPATH, fe_Sections.leaguenamesx3).text == self.League_Name:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_035", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Total Score")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("1. Click on the leagues point hyperlink. "
                 "2. Check for the total score info container section. ")
    def test_036(self):
        """To check the functionality of total score hyperlink."""
        # to check the total score info pop up
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.leaguepointsview).click()
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, fe_Sections.totalscoreinfosx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_036", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("League Tray Contestants")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("1. Since from the last step, the score info container is opened, click on OK to close it. "
                 "2. Click on the arrow icon. "
                 "3. Check whether the expected number if contestant containers are there or not. ")
    def test_037(self):
        """ To verify the no. of contestant present is as per the added one or not. """
        # click on ok first to close the score info pop up.
        # click on the arrow button.
        # check for the contestant containers.
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Objects.ok3).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, fe_Sections.teamdetailsx).click()
        time.sleep(1)
        # to check whether the number of added contestants are there or not in the league
        fe_actions.checkforaddedcontenstant(self, self.contestant_no, 1)
        allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_037", attachment_type=AttachmentType.PNG)

    @allure.title("League Tray Captain")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "my league")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Check presence of captain icon in the first contestant container. ")
    def test_038(self):
        """To verify the presence of captain tag in the first contestant tray in my league page."""
        # to check the presence of captain tag in the first contestant
        # this will be done by checking the presence of captain tag section
        try:
            self.driver.find_element(By.XPATH, fe_Sections.captaintagsx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_038", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("User Name")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "user profile")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on user profile icon. "
                 "2. Get the current user name. "
                 "3. Compare the current user name with the saved one in the script. ")
    def test_039(self):
        time.sleep(1)
        """ To verify the username, in user profile page."""
        self.driver.find_element(By.XPATH,fe_Objects.profileicon).click()
        # to verify the username
        if self.driver.find_element(By.XPATH, fe_Sections.username2sx).text == self.user_name:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_039", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("User Email")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "user profile")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Get the current user email address. "
                 "2. Compare the current user name with the one entered in user detail pop up. ")
    def test_040(self):
        """ To verify the email, in user profile page. """
        # to verify the user email address
        # now since this was written before, the new mandatory user detail pop up implementation,
        # the test cases is written in a way that it will give true only when the updated email address
        # is there and if the old one or any other is there it will give false.
        # In future there will be case added wherein the user profile will be checked twice,
        # once before user filling the user detail pop up and one after.
        if self.driver.find_element(By.XPATH, fe_Sections.useremailsx).text == self.Email:
            assert True
        elif self.driver.find_element(By.XPATH, fe_Sections.useremailsx).text == self.user_email:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_040UserEmail",
                          attachment_type=AttachmentType.PNG)
            assert False
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_040Email", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("User DOB")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "user profile")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Get the current user DOB. "
                 "2. Compare the current user DOB with the saved one in the script. ")
    def test_041(self):
        """To verify the DOB, in user profile page."""
        # to verify the user DOB
        if self.driver.find_element(By.XPATH, fe_Sections.DOBsx).text == self.user_DOB:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_041", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("User League Joined Status")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "user profile")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Get the current user league joined status. "
                 "2. Compare the current user league joined status with the saved one in the script. ")
    def test_042(self):
        """ To verify the user joined league status, in user profile page. """
        # tp verify the user joined league status
        try:
            joined_league = self.driver.find_element(By.XPATH, fe_Sections.no_of_joined_league).text
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_042NoSchElement",
                          attachment_type=AttachmentType.PNG)
            assert False
        else:
            if joined_league == "1":
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_042not1status",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("User Data In Leaderboard")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "leaderboard")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("1. Click on the my league from the header menu. "
                 "2. Get the current user rank. "
                 "3. Get the current user league point. "
                 "4. Get the current user name. "
                 "5. Compare above three with the saved one in script. ")
    def test_043(self):
        """ To verify the loggedIn user's name, rank and score in leader board."""

        # to verify the loggedIn user's name, rank and score in leader board in comparison
        # to the data given in my league page.
        self.driver.find_element(By.XPATH, fe_Objects.myleague).click()
        try:
            self.driver.find_element(By.XPATH,fe_Sections.userdetailpopupsx)
        except WebDriverException:
            pass
        else:
            fe_actions.enteruserdetail(self,self.Name,self.Email,self.Mobile,self.City)
        time.sleep(2)
        self.user_rank = self.driver.find_element(By.XPATH, fe_Sections.rank1sx).text
        self.user_score = self.driver.find_element(By.XPATH, fe_Objects.leaguepointsview).text
        # to verify the username
        self.driver.find_element(By.XPATH, fe_Objects.leaderboard).click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH, fe_Sections.username1sx).text == self.user_name:
            un = 1
        else:
            un = 0

        # to verify the user rank
        if self.driver.find_element(By.XPATH, fe_Sections.rank2sx).text == self.user_rank:
            ur = 1
        else:
            ur = 0

        # to verify the user score
        if self.driver.find_element(By.XPATH, fe_Sections.pointssx).text == self.user_score:
            us = 1
        else:
            us = 0

        if un and us and ur == 1:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_043", attachment_type=AttachmentType.PNG)
            assert False, f"Value of un:,{un}" \
                          f"Value of us:, {us}" \
                          f"Value of ur:, {ur}"

    @allure.title("TnC Hyperlink")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "terms and conditions")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on the terms and conditions hyperlinked text. "
                 "2. Get the current url. "
                 "3. Compare the current url with the save one in the script. ")
    def test_044(self):
        """ To check the functionality of terms and conditions hyperlink text."""
        # to check the terms and conditions hyperlink text
        # will be checked by comparing urls
        self.driver.find_element(By.XPATH, fe_Objects.terms_and_conditions).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.termsandcondtions_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_044", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("TnC Container")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "terms and conditions")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Check for the terms and conditions continer element. ")
    def test_045(self):
        """ To verify the terms and condition container element in TnC page. """
        # to check the presence of TnC section in TnC Page
        try:
            self.driver.find_element(By.XPATH, fe_Sections.tnc_sx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_045", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("TnC Back Button")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "terms and conditions")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on the back button. "
                 "2. Get the current url. "
                 "3. Compare the current url with the saved one in the script. ")
    def test_046(self):
        """ To check the functionality of the back button of TnC page."""
        # to check the back button functionality of the TnC Page
        # will be checked by comparing the url of the previous visited page i.e. leaderboard page
        self.driver.find_element(By.XPATH, fe_Objects.back1).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.leaderoard_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_046", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Team Already Created Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("1. Click on the create team from the header menu. "
                 "2. check for already created team pop up element. ")
    def test_047(self):
        """ To verify the presence of already created team pop up in create team page. """
        # tp check when user after creating team lands again on the create team page,
        # the already created pop-up appears or not this will be checked by validating the
        # presence of the pop-up section.
        self.driver.find_element(By.XPATH, fe_Objects.createteam2).click()
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, fe_Sections.alreadycreateamteam_sx)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_047", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    @allure.title("Team Already Created Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Get the current text from already created team pop up. "
                 "2. Compare the current text with the saved one. ")
    def test_048(self):
        """ To verify the text message in already created team pop up. """
        # to check when the already created team validation message
        if self.driver.find_element(By.XPATH,
                                    fe_Sections.alreadycreatedteamtxt_sx).text == fe_texts.alreadycreateteam_txt:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_048", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Team Already Created Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on the back button of already created team pop up. "
                 "2. Get the current url. "
                 "3. Compare the current url with the saved leaderboard url since previous page was"
                 "leaderboard page. ")
    def test_049(self):
        """ To check the functionality of back button in the already created team pop up. """
        # to check the functionality of back button in already created team pop up
        self.driver.find_element(By.XPATH, fe_Objects.back2).click()
        time.sleep(2)
        if self.driver.current_url == fe_texts.leaderoard_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_049", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("Team Already Created Pop Up")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "create team")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Click on create team from header menu. "
                 "2. Click on the go to my league button in already created team pop up. "
                 "3. Get the current url. "
                 "4. Compare the current url with the saved my league url in the script. ")
    def test_050(self):
        """ To verify continue to my league button functionality in the already created team pop up. """
        # to check the go to my league button functionality of the already created team pop up
        # this will be checked when the user will land again on the create team page
        # by clicking on create team in header and then go to my league button will be clicked
        # and url will be compared.
        self.driver.find_element(By.XPATH, fe_Objects.createteam2).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, fe_Objects.gotomyleague).click()
        time.sleep(1)
        if self.driver.current_url == fe_texts.myleague_url:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_050", attachment_type=AttachmentType.PNG)
            assert False

    @allure.title("League Logo")
    @allure.testcase(testcasedocument, "Test Case Document")
    @allure.tag("sanity", "user detail popup", "web", "league logo")
    @allure.link(testcasereport,
                 link_type="hyperlink", name="Test Case Report")
    @allure.severity(allure.severity_level.MINOR)
    @allure.step("1. Since user is already on my league page, click on user profile icon. "
                 "2. Click on the league logo from the header. "
                 "3. Get the current url. "
                 "4. Compare the current url with the saved my league url in the script. ")
    def test_051(self):
        """ To check when clicked on league logo user should land on the 'my league' page."""
        # since till above step user is already in my league page, first we will make
        # the user land on different page and from there will be clicking on the
        # league icon and then result will be saved by comparing url

        self.driver.find_element(By.XPATH,fe_Objects.profileicon).click()
        if self.driver.current_url == fe_texts.userprofile_url:
            self.driver.find_element(By.XPATH,fe_Objects.vflicon).click()
            if self.driver.current_url == fe_texts.myleague_url:
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_051",attachment_type=AttachmentType.PNG)
                assert False
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="SSTC_051userprofileiconerror",
                          attachment_type=AttachmentType.PNG)
            assert False