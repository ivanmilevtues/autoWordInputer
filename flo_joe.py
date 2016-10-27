# TODO: Check check_answer()! method
# check what the webs is doing when you click the mark and continue buttons!
# DONE
# 1. Browser Opening
# 2. WebSite locating
# 3. Opening file with english word
# 4. Sending the words to the input boxes of the web site
# This script will make do all kind of open close UOE exersizes

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def load_words():
    word_buffer = ''
    with open("20k.txt", "r") as f:
        word_buffer = f.read()
    return word_buffer.split('\n')


def browser_initializer():
    driver = webdriver.Chrome()
    if driver:
        return driver
    else:
        return False


def check_answer(driver, cur_id):
    mark = driver.find_element_by_id("checkAnswers")
    mark.click()
    result_id = "result" + cur_id[1]
    if driver.find_element_by_id(result_id):
        if driver.find_element_by_xpath("//span[@alt, 'Incorrect!']"):
            return False
        elif driver.find_element_by_xpath("//span[@alt, 'Correct!']"):
            return True
        else:
            pritn("WHAT")
            return True


def load_page(driver):
    url = input("Enter the url of the website you want to go to: ")
    driver.get(url)


def write_to_input(driver, id_list):
    words = load_words()
    for cur_id in id_list:
        if driver.find_element_by_id(cur_id):
            for word in words:
                input_box = driver.find_element_by_id(cur_id)
                input_box.clear()
                input_box.send_keys(word)
                if check_answer(driver, cur_id):
                    break
        else:
            print("There wasn't found any input box")


def main():
    id_list = ["q" + str(i) for i in range(15)]
    driver = browser_initializer()
    if not driver:
        return -1
    load_page(driver)
    write_to_input(driver, id_list)
    input("Press any key to kill the process: ")
    driver.quit()

if __name__ == '__main__':
    main()
