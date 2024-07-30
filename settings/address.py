from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ui
import time

class Address:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def searchAddress(self, address):
        xPathSearchAddressTextField = '(//input[@class="css-3017qm exxxdg63"])[2]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathSearchAddressTextField)))
        self.browser.find_element(By.XPATH, xPathSearchAddressTextField).send_keys(address)
        time.sleep(1)
    
    def addAddress(self):
        xPathAddAddressButton = '//button[@class="css-1cpgquu-unf-btn eg8apji0"]/span'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathAddAddressButton)))
        self.browser.find_element(By.XPATH, xPathAddAddressButton).click()
        time.sleep(1)

    def allAddressList(self):
        xPathAllAddressListButton = '//button[@class="css-1pt00lg-unf-chip e6yxrl1"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathAllAddressListButton)))
        self.browser.find_element(By.XPATH, xPathAllAddressListButton).click()
        time.sleep(1)
    
    def shareAddressList(self):
        xPathSharedAddressListButton = '//button[@class="css-eylirg-unf-chip e6yxrl1"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathSharedAddressListButton)))
        self.browser.find_element(By.XPATH, xPathSharedAddressListButton).click()
        time.sleep(1)