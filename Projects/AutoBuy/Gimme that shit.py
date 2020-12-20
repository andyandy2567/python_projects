from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
# import requests
import time
import sys

option = webdriver.ChromeOptions()
option.add_argument("--lang=en")
driver = webdriver.Chrome(chrome_options=option,executable_path='C:/Users/OASIS/Desktop/chromedriver.exe')
login_url = "https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=https%3A%2F%2Fecvip.pchome.com.tw%2Fweb%2Forder%2Fall"
init_url = "https://ecvip.pchome.com.tw/web/order/all"
url = 'https://24h.pchome.com.tw/prod/DRAD1R-A900AYES2?fq=/S/DRADHM'
ACCOUNTS = {'andyandy2567@gmail.com': 'A29332930', 'muse2567@yahoo.com.tw': 'A29332930'}


def login():
    # get to login_url
    driver.get(login_url)
    driver.maximize_window()
    # WebDriverWait(driver,1000).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME,'login-tab-r')))
    # driver.find_element_by_class_name('login-tab-r').click()
    # enter my account id
    driver.find_element_by_id('loginAcc').send_keys('andyandy2567@gmail.com')
    # enter password
    driver.find_element_by_id('loginPwd').send_keys('A29332930')
    # find and click the login button
    driver.find_element_by_id('btnLogin').click()
    # Check if refreshed
    WebDriverWait(driver, 1000).until(EC.url_to_be(init_url))
    # print notice if login was successful
    print('Login Successful')


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


#  use pop-out alert to test if it's out of stock
def check_stock():
    try:
        driver.switch_to.alert.accept()
        print("Accept alert")
    except NoAlertPresentException:
        print("No alert pop out")
        return False
    print("click")
    return True


def buy():
    driver.get(url)
    # find and click the add_to_cart button using xpath
    xpath = '//li[@id="ButtonContainer"]/button'
    not_yet = '//a[contains(text(), "完售，請參考其他商品")]'
    cart_24 = '//a[contains(text(), "加入24h購物車")]'
    cart_not_24 = '//a[contains(text(), "加入購物車")]'
    check = '//a[contains(text(), "點擊後進入結帳清單")]'
    # cart_path = "//*[@id="ServiceContainer"]/cart"
    # keep refreshing if button not found
    # while check_exists_by_xpath(not_yet):
    #     driver.get(url)
    # check if there is any unexpected alert
    while True:
        button_buy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button_buy.click()
        # keep refreshing the page if it's our of stock
        if check_stock():
            # refresh if out of stock
            driver.refresh()
            print("yes")
        else:
            break


def check_out():
    if url == driver.current_url:
        # find and click the check_out button
        button_check = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "check"))
        )
        # to prevent element to be clicked got covered
        driver.execute_script("arguments[0].click();", button_check)
    # payment method: paid in full
    payment_methond = '//a[contains(text(), "一次付清")]'
    # Wait for the button to be clickable
    button_CC = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, payment_methond))
    )
    button_CC.click()
    go = '//a[contains(text(), "繼續")]'
    # Wait for the button to be clickable
    button_go = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, go))
    )
    button_go.click()
    time.sleep(1)
    driver.find_element_by_id('multi_CVV2Num').send_keys('397')
    driver.find_element_by_id('BuyerSSN').send_keys('A127442307')


# option = webdriver.ChromeOptions()
# #option.add_argument('headless')
# option.add_argument("--lang=en")
# driver = webdriver.Chrome(chrome_options=option,executable_path='C:/Users/Oasis/Desktop/chromedriver.exe')
def main():
    login()
    buy()
    check_out()


if __name__ == '__main__':
    main()


