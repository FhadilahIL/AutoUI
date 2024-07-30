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

    def biodataDiriTab(self):
        xPathBiodataDiri = '//button[@data-testid="tab-bio"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathBiodataDiri)))
        self.browser.find_element(By.XPATH, xPathBiodataDiri).click()
    
    def alamatTab(self):
        xPathAlamat = '//button[@data-testid="tab-adress"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathAlamat)))
        self.browser.find_element(By.XPATH, xPathAlamat).click()
    
    def pembayaranTab(self):
        xPathPembayaran = '//button[@data-testid="tab-payment"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathPembayaran)))
        self.browser.find_element(By.XPATH, xPathPembayaran).click()
    
    def bankTab(self):
        xPathBank = '//button[@data-testid="tab-bank"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathBank)))
        self.browser.find_element(By.XPATH, xPathBank).click()
    
    def notifTab(self):
        xPathNotif = '//button[@data-testid="tab-notif"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathNotif)))
        self.browser.find_element(By.XPATH, xPathNotif).click()
    
    def googleAuthenticatorTab(self):
        xPathGoogleAuthenticator = '//button[@data-testid="tab-ga"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathGoogleAuthenticator)))
        self.browser.find_element(By.XPATH, xPathGoogleAuthenticator).click()