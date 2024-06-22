from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_elements.elements_mapper import LoginPage as login







class LoginPageObject:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

    def launch_page(self):
        self.driver.get(login.url)
        self.driver.maximize_window()

    def valid_credentials(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,login.username)))
        self.driver.find_element(By.CSS_SELECTOR,login.username).send_keys('valid')
        self.driver.find_element(By.CSS_SELECTOR,login.password).send_keys('password')

    def invalid_credentials(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,login.username)))
        self.driver.find_element(By.CSS_SELECTOR,login.username).send_keys('invalidcred')
        self.driver.find_element(By.CSS_SELECTOR,login.password).send_keys('password')

    def login_button(self):
        self.driver.find_element(By.CSS_SELECTOR,login.login_button).click()

    def error_display(self,):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, login.error_message)))
        error_message = self.driver.find_element(By.CSS_SELECTOR, login.error_message)
        assert error_message.is_displayed()
    def error_message(self, expected_text):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, login.error_message), expected_text))
        error_message = self.driver.find_element(By.CSS_SELECTOR, login.error_message).text
        assert error_message == expected_text
