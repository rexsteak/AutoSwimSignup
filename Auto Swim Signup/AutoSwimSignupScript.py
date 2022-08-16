from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta

username = 'username'
password = 'password'
scheduleDay = datetime.today() + timedelta(days=7)
scheduleDayString = scheduleDay.strftime('%#m/%#d/%Y')
eventTitle = None
fullHour = False

def Register():
    browser.find_element_by_xpath("//img[@title='Register Now']").click()
    browser.switch_to.frame("editRegiframe")
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "masterPageUC_MasterPage999999_lbSaveReg"))).click()
    WebDriverWait(browser, 10).until(EC.alert_is_present(),"Thank you for registering!" ).accept()

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(('https://www.marqueeclubgroup.com/default.aspx?p=dynamicmodule&pageid=407676&ssid=334883&vnf=1'))
browser.maximize_window()

usernameInput = browser.find_element_by_id('masterPageUC_ctl01_ctl00_txtUsername')
usernameInput.send_keys(username)
passwordInput = browser.find_element_by_id('masterPageUC_ctl01_ctl00_txtPassword')
passwordInput.send_keys(password)
signinButton = browser.find_element_by_id('btnSecureLogin')
signinButton.click()

linkHover = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "ulMenuItem_335146")))
ActionChains(browser).move_to_element(linkHover).perform()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='https://www.marqueeclubgroup.com/Default.aspx?p=v35Calendar&title=Indoor Pool Schedule&view=l3&ssid=335239&vnf=1']"))).click()

alert = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'eapp-popup-control-close-component')))
alert.click()

day = browser.find_element_by_xpath("//td[contains(@ondblclick, '" + scheduleDayString + "')]")

if scheduleDay.weekday() == 1: #Tuesday
    eventTitle = 'Lap Swim 6-6:30pm'
elif scheduleDay.weekday() == 3: #Thursday
    eventTitle = 'Lap Swim 6-6:30pm'
elif scheduleDay.weekday() == 5: #Saturday
    eventTitle = 'Lap Swim 12-12:30pm'
    fullHour = True
elif scheduleDay.weekday() == 6: #Sunday
    eventTitle = 'Lap Swim 12-12:30pm'
    fullHour = True
else: #None of the above days so error
    sys.exit("Not vaild day of week" + scheduleDay.weekday())    

event = day.find_element_by_xpath(".//*[contains(text(), '" + eventTitle + "')]")
event.find_element_by_xpath('..').find_element_by_xpath('..').click()

Register()

if fullHour:
    browser.find_element_by_class_name('nextNextEventLink').click()
    #browser.find_element_by_id('masterPageUC_MPCA407693_lbNextEvent').click()
    Register()

# print(scheduleDayString)

# browser.get(('https://www.premieratsawmill.com/'))

# browser.find_element_by_class_name('eapp-popup-control-close-component').click()
# linkHover = browser.find_element_by_id('ulMenuItem_335109')
# ActionChains(browser).move_to_element(linkHover).perform()
# WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='https://www.premieratsawmill.com/Default.aspx?p=v35Calendar&title=Water Fitness Schedule&view=l3&ssid=335128&vnf=1']"))).click()

# day = browser.find_element_by_xpath("//td[@class='tnavTabON currentDay']")
# event = day.find_element_by_xpath(".//*[contains(text(), '11-11:45am Hydrorider w/Kathy')]")
# event.find_element_by_xpath('..').find_element_by_xpath('..').click()

# alert = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'eapp-popup-control-close-component')))

# alert.click()

# day = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//td[@class='tnavTabON currentDay']")))

# browser.find_element_by_xpath("//a[@href='https://www.marqueeclubgroup.com/Default.aspx?p=dynamicmodule&pageid=408009&ssid=335249&vnf=1']").click()

# browser.find_element_by_xpath("//a[@href='https://www.premieratsawmill.com/Default.aspx?p=v35Calendar&amp;title=Indoor Pool Schedule&amp;view=l3&amp;ssid=335237&amp;vnf=1']")
# browser.find_element_by_xpath("//li[@id='ulMenuItem_335109']")
# link = browser.find_element_by_xpath("//li[@id='ulMenuItem_335237']")
# link.find_element_by_tag_name('a').click()

# memberButton = browser.find_element_by_id('ulMenuItem_335249')

# memberButton = test.find_element_by_id('ulMenuItem_335249')"https://www.premieratsawmill.com/Default.aspx?p=v35Calendar&amp;title=Indoor Pool Schedule&amp;view=l3&amp;ssid=335237&amp;vnf=1"
# memberButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'ulMenuItem_335249')))
# browser.implicitly_wait(20)
# memberButton.find_element_by_tag_name('a')
# memberButton.click()

# test1 = test.find_element_by_tag_name('a')
# test1.click()



# memberButton = browser.find_element_by_link_text('Member Login')
# memberButton.click()

# usernameInput = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'masterPageUC_ctl01_ctl00_txtUsername')))

