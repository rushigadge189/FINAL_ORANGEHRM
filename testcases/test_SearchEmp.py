import logging
import time

import allure
from allure_commons.types import AttachmentType
from pageobjects.Add_Emp_Page import Add_Emp
from pageobjects.loginpage import OrangeHRM_login
from pageobjects.Search_EmpPage import Search_Emp
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

    def test_Search_Emp_004(self,setup):

        self.log.info(" Testcase test_Search_Emp_004 Is Started ") ;

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

        self.se=Search_Emp(self.driver);

        self.log.info("Enter Emp ID") ;
        self.se.enter_empid("0268");

        self.log.info("Click On Search Button") ;
        self.se.click_search_button();

        time.sleep(3) ;
        self.log.info("Checking On search Results") ;
        if (self.se.search_results() == True ) :
            self.log.info("Printed Firstname And Middle Name")
            self.log.info("Testcase test_Search_Emp_004 Is Passed")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_Search_Emp_004_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\PYTHON CT15\\OrangeHRM\\screenshots\\test_Search_Emp_004_pass.png") ;
            assert True ;

        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test_Search_Emp_004_pass.png",attachment_type=AttachmentType.PNG) ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\OrangeHRM\\screenshots\\test_Search_Emp_004_fail.png") ;
            self.log.info("Testcase test_Search_Emp_004 Is Failde")
            assert False ;

        self.log.info( "Testcase test_Search_Emp_004 Is Completed" ) ;
