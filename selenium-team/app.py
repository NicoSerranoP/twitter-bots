
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    user = ""
    password = ""

    # This is the path for the Browser driver
    driver_path = "C:/Users/nnico/Documents/University/Hacking/chromedriver.exe"
    # This is the path for the Browser executable
    browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    optionsChrome = webdriver.ChromeOptions()
    # This option prevents the script to open the browser
    #optionsChrome.add_argument('headless')
    optionsChrome.binary_location = browser_path
    driver = webdriver.Chrome(executable_path=driver_path, options = optionsChrome)
    # A timer (is in seconds? or ms?)
    timeout = 10
    url = "https://twitter.com/"
    driver.get(url)

    # Find the login button and click it
    login_button = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]/div'
    button = driver.find_element_by_xpath(login_button)
    button.click()


if __name__ == '__main__':
    main()
