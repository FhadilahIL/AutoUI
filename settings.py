from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ui
import time

class Settings:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def accountSettings(self):
        xPathAccountSettings = '(//a[@class="css-ifllvv"])[9]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathAccountSettings)))
        self.browser.find_element(By.XPATH, xPathAccountSettings).click()
        time.sleep(1)

    def checkPhoneNumber(self, email):
        xPathPhoneNumberGroup = '(//div[@class="css-oh71wi"])[5]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathPhoneNumberGroup)))
        try:
            if bool(self.browser.find_element(By.XPATH, '//a[@data-testid="add-phone-link"]')) == True:
                print(email + ' : Nomor Tidak Ada')
        except:
            xPathPhoneNumber = '(//div[@class="css-oh71wi"])[5]/span[2]'
            print(email +' : '+ self.browser.find_element(By.XPATH, xPathPhoneNumber).text)
        time.sleep(1)