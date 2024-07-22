from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ui
import time

class Payment:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def choosePaymentMethod(self, paymentMethod = ''): #default Saldo Tokopedia
        self.wait.until(Ui.presence_of_element_located((By.XPATH, '//iframe[@id="scrooge-iframe"]')))
        iFramePayment = self.browser.find_element(By.XPATH, '//iframe[@id="scrooge-iframe"]')
        self.browser.switch_to.frame(iFramePayment)
        self.wait.until(Ui.presence_of_element_located((By.XPATH, '//span[@class="css-fh74mg"]')))
        self.browser.find_element(By.XPATH, '//span[@class="css-fh74mg"]').click()
        time.sleep(1)
        self.wait.until(Ui.presence_of_element_located((By.XPATH, '//div[@id="payment-method-list-bottomsheet"]')))
        time.sleep(1)
        xPathPaymentMethod = ''
        match (paymentMethod):
            case 'Saldo Tokopedia':
                xPathPaymentMethod = '//div[@id="tokopediawallet"]'
            case 'GoPay':
                xPathPaymentMethod = '//div[@id="pemuda"]'
            case 'Ovo':
                xPathPaymentMethod = '//div[@id="ovocash"]'
            case 'Credit Card':
                xPathPaymentMethod = '//div[@id="creditcard"]'
            case 'BRI Ceria':
                xPathPaymentMethod = '//div[@id="briceria"]'
            case 'Cod':
                xPathPaymentMethod = '//div[@id="cod"]'
            case 'BCA VA':
                xPathPaymentMethod = '//div[@id="bcava"]'
            case 'Mandiri VA':
                xPathPaymentMethod = '//div[@id="mandiriva"]'
            case 'BRI VA':
                xPathPaymentMethod = '//div[@id="briva"]'
            case 'BNI VA':
                xPathPaymentMethod = '//div[@id="bniva"]'
            case 'BSI VA':
                xPathPaymentMethod = '//div[@id="mandirisyariahva"]'
            case 'CIMB VA':
                xPathPaymentMethod = '//div[@id="cimbva"]'
            case 'Permata VA':
                xPathPaymentMethod = '//div[@id="permatava"]'
            case 'BTN VA':
                xPathPaymentMethod = '//div[@id="permatava"]'
            case 'Danamon VA':
                xPathPaymentMethod = '//div[@id="permatava"]'
            case 'Muamalat VA':
                xPathPaymentMethod = '//div[@id="permatava"]'
            case 'Other VA':
                xPathPaymentMethod = '//div[@id="permatava"]'
            case 'Transfer BCA':
                xPathPaymentMethod = '//div[@id="manualtransfer-1"]'
            case 'Transfer Mandiri':
                xPathPaymentMethod = '//div[@id="manualtransfer-2"]'
            case 'Transfer BNI':
                xPathPaymentMethod = '//div[@id="manualtransfer-3"]'
            case 'Transfer BRI':
                xPathPaymentMethod = '//div[@id="manualtransfer-4"]'
            case 'Transfer CIMB':
                xPathPaymentMethod = '//div[@id="manualtransfer-5"]'
            case 'Debit BRI':
                xPathPaymentMethod = '//div[@id="debitbri"]'
            case 'Debit Mandiri':
                xPathPaymentMethod = '//div[@id="debitmandiri"]'
            case 'Octo Cash':
                xPathPaymentMethod = '//div[@id="prismalink-5"]'
            case 'BCA Klik':
                xPathPaymentMethod = '//div[@id="bcaklikbca"]'
            case 'BRIMO':
                xPathPaymentMethod = '//div[@id="briepay"]'
            case 'Jenius Pay':
                xPathPaymentMethod = '//div[@id="jeniuspay"]'
            case 'Jakone Pay':
                xPathPaymentMethod = '//div[@id="jakonemobile"]'
            case 'Octo Click':
                xPathPaymentMethod = '//div[@id="cimbclicks"]'
            case 'LinkAja Syariah':
                xPathPaymentMethod = '//div[@id="linkajasyariah"]'
            case 'LinkAja':
                xPathPaymentMethod = '//div[@id="mandiriecash"]'
            case 'Qris':
                xPathPaymentMethod = '//div[@id="qris"]'
            case _:
                xPathPaymentMethod = '//div[@id="tokopediawallet"]'

        self.browser.find_element(By.XPATH, xPathPaymentMethod).click()
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//button[@id="btn-pay-confirm"]').click()
        time.sleep(5)