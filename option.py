from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Option:
    def __init__(self):
        options = Options()
        options.add_argument('--start-maximized')

        self.browser = webdriver.Chrome(options)

    def myOption(self):
        return self.browser
    
    def actionChains(self):
        self.action = ActionChains(self.browser)
        return self.action
    
    def webDriverWait(self):
        self.wait = WebDriverWait(self.browser, 30)
        return self.wait
    
    def quit(self):
        return self.browser.quit()
    
    def environment(self, env):
        if (env == 'Staging'):
            self.baseUri = 'https://staging.tokopedia.com/'
        elif (env == 'Production'):
            self.baseUri = 'https://www.tokopedia.com/'
        else:
            print('Environment Tidak Ada')
            False    
        self.browser.get(self.baseUri)
        return self.baseUri
        
    # def baseUri(baseUri):