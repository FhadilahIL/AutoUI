from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ui
import time

class Checkout:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def chooseService(self, service, courier = ''): # If courier isn't fill, will not choosen (default recommended)
        shipmentButtomSheet = '//section[@data-testid="btnShippingDurationDropDownCap"][@data-option-loading="false"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, shipmentButtomSheet)))
        self.browser.find_element(By.XPATH, shipmentButtomSheet).click()
        self.wait.until(Ui.presence_of_element_located((By.XPATH, '//section[@class="css-j59v03"]')))
        arrayServices = self.browser.find_elements(By.XPATH, '//section[@class="css-j59v03"]/div/div/section/h5/b')
        for a in range(len(arrayServices)):
            if service == arrayServices[a].text:
                self.browser.find_element(By.XPATH, '(//section[@class="css-j59v03"]/div/div/section/h5/b)['+ str(a+1) +']').click()
        time.sleep(1)
        try:
            if(service == 'Instant 3 Jam' or service == 'Same Day 8 Jam' or service == 'Kurir Toko' or courier == 'Whitelabel' or courier == ''):
                return False
            self.__chooseCourier(courier)
        except:
            print('Service dan Courier Sudah Terisi')

    def __chooseCourier(self, courier = ''):
        courierButtomSheet = '//section[@data-testid="shippingCourierDropDownCapValue"][@data-option-loading="false"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, courierButtomSheet)))
        self.browser.find_element(By.XPATH, courierButtomSheet).click()
        self.wait.until(Ui.presence_of_element_located((By.XPATH, '//section[@class="css-j59v03"]')))
        arrayCouriers = self.browser.find_elements(By.XPATH, '//section[@class="css-j59v03"]/div/div/section/h5/b')
        for a in range(len(arrayCouriers)):
            if courier == arrayCouriers[a].text:
                self.browser.find_element(By.XPATH, '(//section[@class="css-j59v03"]/div/div/section/h5/b)['+ str(a+1) +']').click()
        time.sleep(1)

    def goToPayment(self):
        pilihPembayaranButton = '//button[@data-testid="btnSafChoosePayment"]'
        self.wait.until(Ui.presence_of_element_located((By.XPATH, pilihPembayaranButton)))
        self.browser.find_element(By.XPATH, pilihPembayaranButton).click()
        time.sleep(1)