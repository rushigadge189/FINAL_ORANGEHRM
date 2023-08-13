import logging

import allure
from allure_commons.types import AttachmentType

from pageobjects.loginpage import OrangeHRM_login
from utilities.logger import LogGenerator
from utilities.Readconfig import Readconfig

class Test_Login():
    username=Readconfig.GetUserName() ;
    password=Readconfig.GetPassword() ;

    log=LogGenerator.loggen();

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("Page Title Is Test Case")
    @allure.issue("ABC123")
    @allure.story("This Is Story #1 ")

    def test_page_title_001(self,setup):
        self.log.info(" Testcase test_page_title_001 Is started ")
        self.log.info(" Opening The Browser ") ;

        self.driver=setup ;

        self.log.info(" Page Title Is = "+self.driver.title) ;

        if (self.driver.title=='OrangeHRM') :
            allure.attach(self.driver.get_screenshot_as_png(), name="test_page_title_001_pass", attachment_type=AttachmentType.PNG) ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\OrangeHRM\\screenshots\\test_page_title_001_pass.png") ;
            self.log.info(" Testcase test_page_title_001 Is Passed ") ;
            assert True ;
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_page_title_001_fail", attachment_type=AttachmentType.PNG) ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\OrangeHRM\\screenshots\\test_page_title_001_fail.png") ;
            self.log.info(" Testcase test_page_title_001 Is Failed ") ;
            assert False ;
        self.log.info( "Testcase test_login_002 Is Completed" ) ;

    def test_login_002(self,setup):
        self.log.info(" Testcase test_login_002 Is Started ") ;

        self.log.info(" TestCase test_login_002 iS Started ") ;
        self.log.info(" Opening The Browser ") ;

        self.driver=setup ;

        self.lp=OrangeHRM_login(self.driver) ;

        self.log.info(" Entering Username "+self.username) ;
        self.lp.enter_username(self.username) ;

        self.log.info(" Entering Password "+self.password) ;
        self.lp.enter_password(self.password) ;

        self.log.info(" Clicking On Login Button ") ;
        self.lp.click_login_button();

        self.log.info(" Checking for Login Status ") ;
        if ( self.lp.login_status() == True ) :
            self.log.info(" Taking Screenshot ") ;
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_002_pass", attachment_type=AttachmentType.PNG) ;
            self.driver.save_screenshot('D:\\PYTHON CT15\\OrangeHRM\\screenshots\\test_login_002_pass.png');

            self.log.info(" Clicking On Menu Button ") ;
            self.lp.click_menu_button();

            self.log.info(" Clicking On Logout Button ")
            self.lp.click_logout_button();

            self.log.info(" Testcase test_login_002 Is Passed ") ;
            assert True ;

        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test_login_002_fail",attachment_type=AttachmentType.PNG) ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\OrangeHRM\\screenshots\\test_login_002_fail.png") ;

            self.log.info( "Testcase test_login_002 Is Failed" ) ;
            assert False ;
        self.log.info( "Testcase test_login_002 Is Completed" ) ;
