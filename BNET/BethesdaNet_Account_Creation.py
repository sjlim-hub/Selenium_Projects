#Import webdriver and required libraries
import time
from selenium import webdriver

#We will be using time.sleep(X) to allow different elements to load. Other wait options would be explicit or implicit wait.

#define the webdriver
driver = webdriver.Chrome(executable_path='C:\Webdrivers\chromedriver\chromedriver.exe')

#open the webpage
driver.get("https://bethesda.net/en/dashboard")

time.sleep(6)

#Accept the privacy policy
driver.find_element_by_id("onetrust-accept-btn-handler").click()

#Navigate to the Login/SignUp button and click it
driver.find_element_by_class_name("RiotWrapper-cogs-global-nav-RiotWrapper-cogs-global-nav35").click()

#Click to Sign Up to begin account creation
driver.find_element_by_xpath("//button[@id='createAccountBtn']").click()

#Click 'Create Account'
driver.find_element_by_id("signupBtn").click()

#Enter your e-mail address
driver.find_element_by_css_selector("input[id='bnet-marketing-opt-in-checkbox']").click()
Email = "johndoe202150@protonmail.com"
driver.find_element_by_name("email_address").send_keys(Email)
time.sleep(2)

#Continue to the next step
driver.find_element_by_xpath("//span[contains(text(), 'Continue')]").click()
time.sleep(2)

#Enter new username and password
Username = "MaroonSoldier123456"
Password = "Combination1Password@"
driver.find_element_by_name("username").send_keys(Username)
driver.find_element_by_name("password").send_keys(Password)
driver.find_element_by_xpath("//span[contains(text(), 'Continue')]").click()
time.sleep(2)

#Select the security question dropdown
driver.find_element_by_id("mui-component-select-question").click()
time.sleep(2)
driver.find_element_by_xpath("//ul[@role='listbox']/li[3]").click() #Choose the favorite dessert option
driver.find_element_by_name('answer').send_keys('candy')

#Create the account
driver.find_element_by_xpath("//span[contains(text(), 'Create Account')]").click()

print("Account creation complete!")
print("Username: ", Username)
print("Password: ", Password)
print("Email: ", Email)