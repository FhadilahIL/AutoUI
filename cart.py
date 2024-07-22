from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ui
import time

class Cart:
    def __init__(self, browser, wait, action, productID = ''):
        self.browser = browser
        self.action = action
        self.wait = wait
        self.productID = productID
        self.xPathCartButton = '//div[@data-testid="iconHeaderCart"]'

    def goToCart(self):
        self.browser.find_element(By.XPATH, self.xPathCartButton).click()
        time.sleep(1)

    def checkProduct(self):
        xPathProductChecklistCart = '//div[@data-testid="productInfoAvailable-' + self.productID + '"]/div/span/input[@type="checkbox"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathProductChecklistCart)))
        if self.browser.find_element(By.XPATH, xPathProductChecklistCart).get_attribute('checked') != 'true':
            self.browser.find_element(By.XPATH, xPathProductChecklistCart).click()
        try:
            self.uncheckProduct()
        except:
            print('Product di Cart Sudah ter-Unchecklist')
        time.sleep(1)

    def uncheckProduct(self):
        arrChecklist = self.browser.find_elements(By.XPATH, '//div[@class="css-2c3mjn"]')
        for i in range(len(arrChecklist)):
            checklist = self.browser.find_element(By.XPATH, '(//div[@class="css-2c3mjn"])['+ str(i + 1) +']').get_attribute('data-testid')
            if checklist != None:
                if checklist.split('-')[0] == 'productInfoAvailable':
                    if self.productID != checklist.split('-')[1]:
                        xPathProductChecklistCart = '//div[@data-testid="productInfoAvailable-' + checklist.split('-')[1] + '"]/div/span/input[@type="checkbox"]'
                        if self.browser.find_element(By.XPATH, xPathProductChecklistCart).get_attribute('checked') == 'true':
                            self.action.scroll_to_element(self.browser.find_element(By.XPATH, xPathProductChecklistCart)).perform()
                            time.sleep(1)
                            self.browser.find_element(By.XPATH, xPathProductChecklistCart).click()
                            time.sleep(1)
    def goToCheckout(self):
        beliButton = '//button[@data-testid="cartCheckoutBTN"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, beliButton)))
        self.browser.find_element(By.XPATH, beliButton).click()
        time.sleep(1)