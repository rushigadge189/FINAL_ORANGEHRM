from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrangeHRM_login():
    text_username=(By.XPATH, '//input[@name="username"]') ;
    text_password=(By.XPATH, '//input[@name="password"]') ;
    click_login=(By.XPATH, '//button[@type="submit"]') ;
    click_menu=(By.XPATH, "//span[@class='oxd-userdropdown-tab']") ;
    click_logout=(By.XPATH, '//a[text()="Logout"]') ;

    def __init__(self,driver):
        self.driver=driver;
        self.wait=WebDriverWait(self.driver, 10, poll_frequency=0.5) ;

    def enter_username(self,username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.text_username)) ;
        self.driver.find_element(*OrangeHRM_login.text_username).send_keys(username);

    def enter_password(self,password):
        self.driver.find_element(*OrangeHRM_login.text_password).send_keys(password) ;

    def click_login_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.click_login)) ;
        self.driver.find_element(*OrangeHRM_login.click_login).click();

    def click_menu_button(self):
        self.driver.find_element(*OrangeHRM_login.click_menu).click() ;

    def click_logout_button(self):
        self.driver.find_element(*OrangeHRM_login.click_logout).click() ;

    def login_status(self):
        try :
            self.wait.until(expected_conditions.visibility_of_element_located(self.click_menu)) ;
            self.driver.find_element(*OrangeHRM_login.click_menu) ;
            return  True ;
        except :
            return False ;