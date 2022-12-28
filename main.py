from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#open target website with webdriver
website = 'https://www.youtube.com/'
path = '\Python310\Chromedriver'
driver = webdriver.Chrome(executable_path=r'C:\Python310\Chromedriver\chromedriver.exe')
driver.get(website)

# Navigate to the website
driver.get('https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DIAKpwt1ZXZY%2526list%253DPL699Xf-_ilW76WC_FIcE8TqqkzpB9dhy3%2526index%253D2&hl=en&ec=65620&ifkv=AeAAQh5-2O2Fjd2B3zOKY0d-0bXLZpnDW0dph6x0Z4BS2LNz_1yGpuMf0PmntNJPHeVv8PVxvuPOZg&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

#wait before click sign in
time.sleep(1)

#click to log in
#WebElement  = driver.find_element(By.xpath("//div[@id='end']/div[2]/ytd-button-renderer[1]/yt-button-shape[1]/a[1]/yt-touch-feedback-shape[1]/div[1]/div[2]"))

#wait before click sign in
#time.sleep(1)

#click to use another account
#click_submit = driver.findElement(By.xpath("//div[@class='BHzsHc']")).click()

#fill google account email
username = " "
password = " "

#automated fill in email and password
driver.find_element("xpath", "//input[@class='whsOnd zHQkBf']").send_keys(username)

#wait before click next
time.sleep(3)

#click next
driver.find_element("xpath", ("(//button[@data-idom-class='nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']//div)[3]")).click()

#automated fill in password
driver.find_element("xpath", "//input[@type='password']")).send_keys(password)

#click next
driver.findElement(By.xpath("//span[text()='Next']")).click()


# Find the elements that you want to scrape
#elements = driver.find_elements(By.CLASS_NAME, 'article-title')

# Extract the data from the elements
#for element in elements:
    #print(element.text)

# Close the webdriver
#driver.quit()
