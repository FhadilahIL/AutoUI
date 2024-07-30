from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ui
import time

class OrderList:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def searchTransactiion(self, invoice):
        xPathSearchTransactionTextField = '(//input[@class="css-3017qm exxxdg63"])[2]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, xPathSearchTransactionTextField)))
        self.browser.find_element(By.XPATH, xPathSearchTransactionTextField).send_keys(invoice)
        time.sleep(1)