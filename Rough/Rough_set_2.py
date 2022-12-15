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

service = Service("C:\\Users\\aniket.gupta\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
leagueurl = "https://fantasyapp.voot.com/kkk-12/10/kkk12/12"
token = "?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiJwdDM2S0Y3VlZpbTJzMmNVaUN1eTdVdHJRT3BsIiwidXNlck5hbWUiOiJOZXcgVXNlciB0aHJlZSIsImxvZ2luUHJvdmlkZXIiOiJUcmFkaXRpb25hbCIsImdlbmRlciI6Ik0iLCJhZ2UiOiIzMS0wMy0xOTk1IiwibmFtZSI6Ik5ldyBVc2VyIHRocmVlIiwiZW1haWwiOiJuZXd1c2VyMDAwMDAwMDNAdm9vdC5jb20iLCJVRElEIjoicHQzNktGN1ZWaW0yczJjVWlDdXk3VXRyUU9wbCIsInNleCI6Ik0iLCJleHRyYURhdGEiOiJ2b290IiwiaWF0IjoxNjYzNTk2MDMzLCJleHAiOjE2OTUxNTM2MzN9.C6NGrNruwHABxI-njfgrHjA06Inofy03-dUCKV2he7E"
driver.get(leagueurl + token)
driver.maximize_window()
driver.implicitly_wait(6)
time.sleep(3)
contestant_no = 6
credit_score = "300.00"
League_Name = "KKK12"
create_team_url_parameter = "?league_id=12"
team_preview_url_parameter = "?showId=10&leagueId=12"
edit_team_url_parameter = "?isEdit=true&league_id=12"
user_name = "New Use Three"
user_email = "newuser00000003@voot.com"
user_DOB = "31-03-1995"
user_updated_email = ""
user_number = ""
user_rank= ""
user_score=""



driver.find_element(By.XPATH,fe_Objects.coachcardcontinue).click()
time.sleep(7)
for i in range(2,8):
    driver.find_element(By.XPATH,
                             f"//*[@id='wrapper']/div/app-create-team/section[2]/div"
                             f"/div/div[2]/table/tbody/tr[{i}]/td[3]/div/div/a").click()
time.sleep(1)
driver.find_element(By.XPATH,fe_Objects.createteam1).click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='wrapper']/div/app-create-team/"
                                          f"section[2]/div/div/div[3]/table/tbody/tr[2]/td[3]/a").click()
time.sleep(2)
a1 = driver.find_element(By.CLASS_NAME,'sel-captain.selected').click()
print(a1)