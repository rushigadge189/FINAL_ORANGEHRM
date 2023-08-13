import logging
import time

import allure
from allure_commons.types import AttachmentType
from pageobjects.Add_Emp_Page import Add_Emp
from pageobjects.loginpage import OrangeHRM_login
from utilities.logger import LogGenerator
from utilities.Readconfig import Readconfig

class Test_Add_Emp():
    username=Readconfig.GetUserName() ;
    password=Readconfig.GetPassword() ;

    log=LogGenerator.loggen();

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("Page Title Is Test Case")
    @allure.issue("ABC123")
    @allure.story("This Is Story #1 ")

    def test_add_emp_003(self,setup):

        self.log.info(" Testcase test_add_emp_003 Is Started ") ;

        self.log.info(" Opening The Browser ") ;

        self.driver=setup ;

        self.lp=OrangeHRM_login(self.driver) ;

        self.log.info(" Entering Username "+self.username) ;
        self.lp.enter_username(self.username) ;

        self.log.info(" Entering Password "+self.password) ;
        self.lp.enter_password(self.password) ;

        self.log.info(" Clicking On Login Button ") ;
        self.lp.click_login_button();

        self.ae=Add_Emp(self.driver) ;

        self.log.info("Click Pim")
        self.ae.click_pim_tab();

        self.log.info("Click Add Emp Button") ;
        self.ae.click_add_emp_button();

        self.log.info("Enter First Name");
        self.ae.enter_first_name("Rahul") ;

        self.log.info("Enter Middle Name")
        self.ae.enter_middle_name("K") ;

        self.log.info("Enter Last Name");
        self.ae.enter_last_name("Pune") ;

        self.log.info("Get Employee Value");
        self.ae.get_id_value() ;

        self.log.info("Uploading Image");
        self.ae.upload_img() ;
        time.sleep(2);

        self.log.info("Click Save Button");
        self.ae.click_save_button() ;

        self.log.info("Cheking Success Message")
        if (self.ae.success_messge() == True) :
            self.log.info("Taking Screenshots") ;
            allure.attach(self.driver.get_screenshot_as_png(), name="add_emp_003_pass.png", attachment_type=AttachmentType.PNG) ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\OrangeHRM\\screenshots\\add_emp_003_pass.png");
            self.log.info("Testcase test_add_emp_003 Passed")
            assert True ;

        else :
            allure.attach(self.driver.get_screenshot_as_png(),name="add_emp_003_fail.png", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\PYTHON CT15\\OrangeHRM\\screenshots\\add_emp_003_fail.png") ;
            self.log.info("Testcase test_add_emp_003 Failed") ;
            assert  False;

        self.log.info( "Testcase test_add_emp_003 Is Completed" ) ;
