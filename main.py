from homepage import Homepage
from option import Option
from pdp import Pdp
from cart import Cart
from checkout import Checkout
from payment import Payment
import testdata

class Main:
    def __init__(self):
        self.options = Option()
        self.myOption = self.options.myOption()
        self.action = self.options.actionChains()
        self.wait = self.options.webDriverWait()
        self.productID = ''
        self.__insHome = Homepage(self.myOption, self.wait)
        self.__insPdp = Pdp(self.myOption, self.wait)
        self.__insCart = Cart(self.myOption, self.wait, self.action)
        self.__insCheckout = Checkout(self.myOption, self.wait)
        self.__insPayment = Payment(self.myOption, self.wait)

    def __login(self, email, password):
        self.__insHome.loginFunc(email, password)

    def __goToPdp(self, productUri):
        self.__insPdp.goToPdp(productUri)
        self.productID = self.__insPdp.getProductID()


    def __atcProduct(self):
        self.__insPdp.atcProduct()

    def __goToCart(self):
        self.__insCart.goToCart()

    def __checklistProduct(self):
        self.__insCart = Cart(self.myOption, self.wait, self.action, self.productID)
        self.__insCart.checkProduct()

    def __goToCheckout(self):
        self.__insCart.goToCheckout()

    def __goToHomepage(self, baseUri):
        self.__insHome.goToHomePage(baseUri)

    def __openAccountMenu(self, baseUri):
        self.__insHome.accountMenu(self.action, baseUri)

    def __logout(self, baseUri):
        self.__insHome.logoutFunc(baseUri)

    def __chooseShipperService(self, service, courier):
        self.__insCheckout.chooseService(service, courier)

    def __goToPayment(self):
        self.__insCheckout.goToPayment()

    def __choosePaymentMethod(self, paymentMethod):
        self.__insPayment.choosePaymentMethod(paymentMethod)


    def createOrders(self):
        for index in range(len(testdata.allDataTest)):
            baseUri = self.options.environment(testdata.allDataTest.env[index])
            self.__login(testdata.allDataTest.email[index], testdata.allDataTest.password[index])
            self.__goToPdp(baseUri + testdata.allDataTest.product_link[index])
            self.__atcProduct()
            self.__goToCart()
            self.__checklistProduct()
            self.__goToCheckout()
            self.__chooseShipperService(testdata.allDataTest.service[index], testdata.allDataTest.courier[index])
            self.__goToPayment()
            self.__choosePaymentMethod(testdata.allDataTest.payment_method[index])
            self.__goToHomepage(baseUri)
            self.__openAccountMenu(baseUri)
            self.__logout(baseUri)
        self.options.quit()

main = Main()
main.createOrders()