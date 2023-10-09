import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
time.sleep(25)
year ="2023"
month ="August"
date= "29"

driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR,"input#datepicker").click()

while True:
    mon=driver.find_element(By.CSS_SELECTOR,"span.ui-datepicker-month").text
    yr=driver.find_element(By.CSS_SELECTOR, "span.ui-datepicker-year").text

    if mon== month and yr == year:
            print("Data matched")
            break
    else:
        driver.find_element(By.XPATH,"(//span[@class='ui-icon ui-icon-circle-triangle-e'])[1]").click()


dates= driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        time.sleep(15)
        break