import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

class Add_Emp ():
    click_pim_xpath=(By.XPATH,'//a[@href="/web/index.php/pim/viewPimModule"]') ;
    click_add_emp_xpath=(By.XPATH, '//i[@class="oxd-icon bi-plus oxd-button-icon"]') ;
    text_firstname_xpath=(By.XPATH, '//input[@name="firstName"]') ;
    text_middlename_xpath=(By.XPATH, '//input[@name="middleName"]') ;
    text_lastname_xpath=(By.XPATH, '//input[@name="lastName"]') ;
    upload_img_xpath=(By.XPATH, "//button[@class='oxd-icon-button oxd-icon-button--solid-main employee-image-action']") ;
    click_save_button_xpath=(By.XPATH, '//button[@type="submit"]') ;
    success_message_xpath=(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']") ;
    get_id_xpath=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]") ;

    def __init__(self,driver):
        self.driver=driver ;

    def click_pim_tab(self):
        self.driver.find_element(*Add_Emp.click_pim_xpath).click() ;

    def click_add_emp_button(self):
        self.driver.find_element(*Add_Emp.click_add_emp_xpath).click() ;

    def enter_first_name(self,firstname):
        self.driver.find_element(*Add_Emp.text_firstname_xpath).send_keys(firstname) ;

    def enter_middle_name(self,middlename):
        self.driver.find_element(*Add_Emp.text_middlename_xpath).send_keys(middlename);

    def enter_last_name(self,lastname):
        self.driver.find_element(*Add_Emp.text_lastname_xpath).send_keys(lastname) ;

    def upload_img(self):
        self.driver.find_element(*Add_Emp.upload_img_xpath).click() ;
        time.sleep(2) ;
        keyboard= Controller();
        keyboard.type("D:\\PYTHON CT15\\OrangeHRM\\testdata\\logo.jpg") ;
        time.sleep(2)
        keyboard.press(Key.enter) ;
        keyboard.release(Key.enter) ;
        time.sleep(2) ;

    def click_save_button(self):
        self.driver.find_element(*Add_Emp.click_save_button_xpath).click() ;
        time.sleep(1) ;

    def get_id_value(self):
        id=self.driver.find_element(*Add_Emp.get_id_xpath).get_attribute("value") ;
        print(" Emloyee Id= "+id) ;

    def success_messge(self):
        try :
            success_message=self.driver.find_element(*Add_Emp.success_message_xpath).text ;
            print(success_message) ;
            return True ;

        except NoSuchElementException:
            return False ;