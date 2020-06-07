from selenium import webdriver
from time import sleep

url = 'https://www.instagram.com/'
url1 = 'https://www.instagram.com/ted'

login=input("Your login: ")
password=input("Your password: ")
hashtag = "#" + input("Enter a word for hashtag (without the symbol of hashtag): ")


def login_page():
    login_link = browser.find_element_by_name('username')
    login_link.click()
    login_link.send_keys(login)  # Login

    password_link = browser.find_element_by_name('password')
    password_link.click()
    password_link.send_keys(password)  # Password

    click_button = browser.find_element_by_css_selector("button[type='submit']")
    click_button.click()


def not_now_window():
    sleep(4)

    not_now_button = browser.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    not_now_button.click()


def follow():
    sleep(3)
    folllow_button = browser.find_elements_by_xpath(
        "//button[contains(text(), 'Follow')][not(contains(text(), 'Unfollow'))][not(contains(text(), 'Followers'))]")
    for i in folllow_button:
        sleep(2)
        i.click()

def search_by_hashtag():
    sleep(2)
    search_window = browser.find_element_by_css_selector(".XTCLo")
    search_window.send_keys(hashtag)
    select_result = browser.find_element_by_css_selector("a.yCE8d:nth-child(1)")
    select_result.click()


with webdriver.Firefox() as browser:
    browser.implicitly_wait(5)
    browser.get(url)

    login_page()
    not_now_window()

    browser.get(url1)
    follow()
    search_by_hashtag()

    sleep(100)

