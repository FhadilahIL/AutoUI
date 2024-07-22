from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ui
import time

class Homepage:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def goToHomePage(self, baseUri):
        self.browser.get(baseUri)
        time.sleep(1)

    def accountMenu(self, action, baseUri):
        if self.browser.current_url == baseUri + 'cart':
            xPathAccountMenu = '(//div[@class="css-1if1bl1"])[3]'
        else:
            xPathAccountMenu = '//div[@data-testid="btnHeaderMyProfile"]'

        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathAccountMenu)))
        action.move_to_element(self.browser.find_element(By.XPATH, xPathAccountMenu)).perform()
        time.sleep(1)

    def loginFunc(self, email, password):
        # Login Button
        xPathLoginButton = '//button[@data-testid="btnHeaderLogin"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathLoginButton)))
        self.browser.find_element(By.XPATH, xPathLoginButton).click()
        time.sleep(1)

        # Email Text Field
        emailTextField =self.browser.find_element(By.XPATH, '//input[@id="email-phone"]')
        emailTextField.send_keys(email)
        time.sleep(1)
        
        # Selanjutnya Login Button
        self.browser.find_element(By.XPATH, '//button[@data-testid="email-phone-submit"]').click()
        time.sleep(2)
        
        # Password Text Field
        passwordTextField = self.browser.find_element(By.XPATH, '//input[@id="password-input"]')
        passwordTextField.send_keys(password)
        time.sleep(1)

        # Masuk Login Button
        self.browser.find_element(By.XPATH, '//span[@aria-label="login-button"]').click()
        
        self.wait.until(Ui.presence_of_element_located((By.XPATH, '//div[@data-testid="btnHeaderMyProfile"]')))

    def logoutFunc(self, baseUri):
        if self.browser.current_url == baseUri + 'cart':
            xPathLogout = '//div[@class="css-1496vmj"]'
        else:
            xPathLogout = '//div[@class="css-15qug2e"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathLogout)))
        self.browser.find_element(By.XPATH, xPathLogout).click()
        
        try:
            xPathNantiSajaButton = '(//*[@class="css-87gx4"])[1]'
            if bool(self.browser.find_element(By.XPATH, xPathNantiSajaButton)) == True:
                self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathNantiSajaButton)))
                self.browser.find_element(By.XPATH, xPathNantiSajaButton).click()
                self.browser.get(baseUri)
        except:
            print('Popup Tidak Ada')

        time.sleep(1)