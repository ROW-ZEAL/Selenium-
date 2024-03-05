import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def verify_title():
    options = webdriver.ChromeOptions()
    # Use the default Chrome location
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    # Automatically download and use the latest ChromeDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    # Navigate to the website
    driver.get("https://tms25.nepsetms.com.np/login")

    # Get the title of the page
    title = driver.title

    # Verify the title
    expected_title = "NEPSE Online Trading system"
    if title == expected_title:
        print(f"Title verification successful! and title is '{title}'")
    else:
        print(f"Title verification failed. Expected '{expected_title}', but got '{title}'.")

    # Find the text field by CSS selector and input the value
    text_field = driver.find_element("css selector", ".form-control")
    text_field.send_keys("2020092711")

    # Find the password field by ID and input the value
    password_field = driver.find_element("id", "password-field")
    password_field.send_keys("Hinduism2024@")

    # Find the captcha field by ID and input the value
    captcha_field = driver.find_element("id", "captchaEnter")
    captcha_field.send_keys("your_captcha_here")


    # Find the login button by class name and click it
    login_button = driver.find_element("class name", "btn-primary")
    login_button.click()

    # Verify if all values have been written correctly
    if (text_field.get_attribute("value") == "2020092711" and
        password_field.get_attribute("value") == "Hinduism2024@" and
        captcha_field.get_attribute("value") == "your_captcha_here" and 
        login_button.is_enabled()):
        print("All values have been written correctly")
        print("Login button is clickable")
    else:
        print("Some values have not been written correctly")
        print("Login button is not clickable")

    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    verify_title()
