'''
Alerts : Alerts are not inspectable. We use Javascript to deal with alerts.
To handle the alerts we will switch the driver control from web app to the alert
SYNTAX : alert_obj = driver.switch_to.alert

In selenium, there are 3 types of alerts
    * simple alert : If the alert is having only one option, then it is simple alert
        To handle the simple alert--> alert_obj.accept() or alert_obj.dismiss()
        Both accept and dismiss will work for simple alert

    * confirmation alert : If we are having two options. One positive option and another negative option.
        alert_obj.accept() --> will click on positive option
        alert_obj.dismiss() --> will click on negative option

    * Authentication pop up : Here we will give the username and pwd while launching the web application
        SYNTAX : https://username:password@url

'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

#--------------------------------------------------------------------
## simple alert:

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@value="Search"]').click()
time.sleep(2)

alert_obj = driver.switch_to.alert
alert_obj.accept()
time.sleep(3)

driver.find_element('xpath', '//input[@value="Search"]').click()
time.sleep(2)
alert_obj.dismiss()

#------------------------------------------------------------------------
## Confirmation

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element('xpath', '//button[text()="Confirm Box"]').click()
time.sleep(2)

alert_obj = driver.switch_to.alert
time.sleep(2)
alert_obj.accept()

driver.find_element('xpath', '//button[text()="Confirm Box"]').click()
time.sleep(2)
alert_obj.dismiss()

#-------------------------------------------------------------------------

## authentication pop up:

driver.get('https://the-internet.herokuapp.com/basic_auth')

## We cannot enter the appplication because to enter the application, we have to give username and pwd
## But they are not inspectable,
## In such scenarios we will give the username and pwd while launching the application itself

## SYNTAX : https://username:pwd@url

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

#----------------------------------------------------------------------------------------
## push notifications

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/")
time.sleep(4)

driver.find_element('class name', 'desktop-searchBar').send_keys('Adidas')
time.sleep(3)

driver.find_element('xpath', '//li[text()="Adidas Shoes"]').click()
time.sleep(5)

shoes_name = driver.find_elements('xpath', '//h4[@class="product-product"]')
shoe_names_list = []
for shoes in shoes_name[::2]:
    shoe_names_list.append(shoes.text)

shoe_prices_list = []
shoes_price = driver.find_elements('xpath', '//div[@class="product-price"]')
for price in shoes_price:
    shoe_prices_list.append(price.text)


for shoe, price in zip(shoe_names_list, shoe_prices_list):
    print(shoe, '-', price)


























