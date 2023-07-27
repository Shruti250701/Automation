from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

timeout = 1

def open_demo_website():
    driver = webdriver.Chrome(
    executable_path="C:\\Users\\ssahu\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("http://localhost:3000/")
    return driver

# Function to log in
def login(driver, username, password):
    username_field = driver.find_element(By.ID, "outlined-basic")
    username_field.send_keys(username)
    time.sleep(timeout)
    password_field = driver.find_element(By.ID, "outlined-basic-password")
    password_field.send_keys(password)
    time.sleep(timeout)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(timeout)

def search(driver, search_name) :
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(search_name)
    time.sleep(timeout)

def search_and_sort(driver,search_name):
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(search_name)
    time.sleep(timeout)
    arr = []
    for _ in range(2):
        list = driver.find_elements(By.XPATH, '//div[@data-field="name" and @role="cell"]/div')
        arr.extend([i.text for i in list])
        end = list[-1]
        driver.execute_script("arguments[0].scrollIntoView(true);", end)
        time.sleep(timeout)
    print(arr)

def sorting_a(driver):
    sort_list = []
    scroll_back(driver)
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in sort_list:
                sort_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            sort_list.append(res.text)
            break
        time.sleep(timeout)
    error_raised = False
    for i in range(len(sort_list)-1):
        if sort_list[i] > sort_list[i+1]:
            error_raised = True
    if not error_raised:
        print("Ascending Sort Validated!")
    else:
        print("Error: Ascending Sort Failed!")
    # print(f"sorted-list = {sort_list}")
    time.sleep(timeout)

def scroll_back(driver):
    action = ActionChains(driver)
    print("Scrolling to top")
    while True:
        for_parent_of_first = driver.find_elements(By.XPATH, "//div[@data-rowindex = '1']")
        res = driver.find_elements(By.XPATH, '//div[@data-field="name"]/div[text()]')
        action.scroll_to_element(res[0]).perform()
        if for_parent_of_first:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "1"]/div[@data-field="name"]/div[text()]')
            break
        time.sleep(timeout)

def sorting_d(driver):
    sort_list = []
    scroll_back(driver)
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    while True:
        for_parent_of_last = driver.find_elements(By.XPATH, "//div[@data-rowindex = '19']")
        res = driver.find_elements(By.XPATH, '//div[@class="MuiDataGrid-row"]/div[@data-field="name"]/div[text()]')
        for i in res:
            if i.text not in sort_list:
                sort_list.append(i.text)
        action.scroll_to_element(res[-1]).perform()
        if for_parent_of_last:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "19"]/div[@data-field="name"]/div[text()]')
            sort_list.append(res.text)
            break
        time.sleep(timeout)
    error_raised = False
    for i in range(len(sort_list)-1):
        if sort_list[i] < sort_list[i+1]:
            error_raised = True
    if not error_raised:
        print("Descending Sort Validated!")
    else:
        print("Error: Descending Sort Failed!")
    # print(f"sorted-list = {sort_list}")
    time.sleep(timeout)

if __name__ == "__main__":
    username = "shruti@data-axle.com"
    password = "this is a secret key"
    search = "ric"
    driver = open_demo_website()
    login(driver, username, password)
    search_and_sort(driver, search)
    sorting_a(driver)
    sorting_d(driver)
    driver.quit()
