import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def browser_initializer(url):
        driver = webdriver.Chrome()
        if driver:
            print("Browser successfuly opened.")
        else:
            print("Driver couldn't open")
        driver.get(url)
        return driver


def write_to_input(input_text, cur_id):
    current_input = driver.find_element_by_id(cur_id)
    current_input.clear()
    current_input.send_keys(input_text)


def website_login():
    print("Logging in...\n")
    login_btn_id = "Langbutton2"
    username_id = "txtUserName"
    password_id = "txtPassword"
    organisation_id = "txtOrgID"
    print("Entering Login information..\n")
    write_to_input("ivan.i.milev@gmail.com", username_id)
    write_to_input("uZknfuB1", password_id)
    write_to_input("900237", organisation_id)
    driver.find_element_by_id(login_btn_id).click()


driver = browser_initializer("http://www.oxfordenglishtesting.com/user_login.aspx")
website_login()

input("Press enter to coninue")
driver.quit()
print("Driver stopped successfuly!")
