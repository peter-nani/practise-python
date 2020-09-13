#RUN THE PROGRAM DIRECTLY ON GOOGLE COLAB OR YOU CAN COMMENT OUT FIRST 5 LINES OF CODE
# AND RUN IN YOUR IDE BY PIP INSTALLING THE LIBRARIES
!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import sys
import random
import time
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.support.ui import Select
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',options = chrome_options)
#open website
wd.get("http://csa.teamchurchs.com/csa/ssologin.aspx")
#enter username
search_un = wd.find_element_by_id("UserName")
search_un.send_keys("USERNAME")#ENTER YOUR USERNAME
#Enter Password
search_pas = wd.find_element_by_id("password")
search_pas.send_keys("PASSWORD")#ENTER YOUR PASSWORD
#Click Login
search_log = wd.find_element_by_id("login")
search_log.click()
#Find ctl00_ContentPlaceHolder1_btnContinue element and clcik to continue to home page
search_cnt = wd.find_element_by_id("ctl00_ContentPlaceHolder1_btnContinue")
search_cnt.click()
#declare the page you are in is a home page
main_page = wd.current_window_handle
time.sleep(2)
#clcik on button to go to ctl00_tdActivityTrack activity tracker sheet
search_cnt = wd.find_element_by_id("ctl00_tdActivityTrack")
search_cnt.click()
time.sleep(2)
#Selecting popup activity tracking page
#conside the login_page as a activty page
for handle in wd.window_handles:
    if handle != main_page:
        login_page = handle
#switching to activty tracker page
wd.switch_to.window(login_page)
print(wd.current_url)
x = 0
while x<=20:
  #Sending random data to acitivity form. call type
  ddata1 = ['follow ups','assigned followups','checked with assigned tickets','TKT updates','Sending Emails to stores which had not answered the call','checked with my Emails','checked with alerts',
            'RPOS done','shortcollection escalated','checked with GTT about GTT tickets','safe ticket followups','EOD Follow ups','site status follow up','updated sheets','Break',]
  #Sending random data to acitivity form. Remarks
  ddata2 = ['Followed up with the daily followups',
            'Followed up with assigned followups',
            'followed up with assigned tickets',
            'updated all the tickets for the day',
            'Sent Emails to EOD incomplete stores and not responded stores',
            'Checked with all the Emails in my mailbox',
            'Checked with all the Alerts and TKT',
            'Checked with RPOS failures and completed RPOS',
            'Checked with assigned short collection and escalated to NCR',
            'Checked with GTT Tickets and got updates from GTT and updated the Tickets',
            'Checked with Brinks Tickets and got updates from brinks and updated the Tickets',
            'Called EOD failure stores and created Tickets',
            'Followed up with assigned site status and closed the Tickets',
            'Updated all the polling sheets',
            'Break Time']
  r = []
  for i in range(0,14):
    r.append(i)

  z = random.choice(r)
  k = (ddata1[z])
  v = (ddata2[z])

  #select the store number text box - id: txtStoreUserID
  stor = wd.find_element_by_id("txtStoreUserID")
  #put some data inside the text box
  stor.send_keys(k)
  #select the drop down list id: ddlCallType
  ddelemt=Select(wd.find_element_by_id('ddlCallType'))
  ddelemt.select_by_value('Report & Analysis')
  #Enter the remarks or comments of call id-txtRemarks
  stor = wd.find_element_by_id("txtRemarks")
  stor.send_keys(v)
  #selecting the random time limit for every task.
  sort_data = []
  ddata3 = range(360,1985,61)
  for i in ddata3:
    sort_data.append(i)
  random_data = random.choice(sort_data)
  print(random_data)
  time.sleep(random_data)
  #press pause button btnPause
  pause = wd.find_element_by_id("btnPause")
  pause.click()
  #press submit button id - btnAdd
  submit_data = wd.find_element_by_id("btnAdd")
  submit_data.click()
  x=x+1
  print(x)
wd.quit()