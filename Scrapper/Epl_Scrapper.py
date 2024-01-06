from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


url='https://www.adamchoi.co.uk/teamgoals/detailed'
options=webdriver.ChromeOptions()
driver = webdriver.Chrome(options)
driver.get(url)
all_matches=driver.find_element(By.XPATH,"(//label[@analytics-event='All matches'])")
all_matches.click()


date=[]
home_team=[]
score=[]
away_team=[]

matches=driver.find_elements(By.TAG_NAME,'tr')
for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home=match.find_element(By.XPATH,'./td[2]').text
    home_team.append(home)
    print(home) 
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)

time.sleep(5)
df=pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('epl_match_data.csv',index=False)

