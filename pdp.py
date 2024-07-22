from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ui
import time

class Pdp:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait
        self.xPathCartButton = '//div[@data-testid="iconHeaderCart"]'
        self.xPathModalCloseButton = '//button[@aria-label="Tutup tampilan modal"]'
        self.xPathAddToCart = '//button[@data-testid="pdpBtnNormalPrimary"]'
        self.productID = ''

    def goToPdp(self, uri):
        self.browser.get(uri)
        self.wait.until(Ui.presence_of_element_located((By.XPATH, self.xPathCartButton)))
        self.wait.until(Ui.presence_of_element_located((By.XPATH, '//meta[@name="branch:deeplink:$ios_deeplink_path"]')))
        content = self.browser.find_element(By.XPATH, '//meta[@name="branch:deeplink:$ios_deeplink_path"]').get_attribute('content')
        self.productID = content.split('/')[1]

    def getProductID(self):
        return self.productID
    
    def atcProduct(self):
        time.sleep(1)
        self.wait.until(Ui.presence_of_element_located((By.XPATH, self.xPathAddToCart)))
        self.browser.find_element(By.XPATH, self.xPathAddToCart).click()
        self.wait.until(Ui.presence_of_element_located((By.XPATH, self.xPathModalCloseButton)))
        self.browser.find_element(By.XPATH, self.xPathModalCloseButton).click()
        time.sleep(1)