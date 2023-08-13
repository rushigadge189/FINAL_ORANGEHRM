import logging
import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageobjects.Add_Emp_Page import Add_Emp
from pageobjects.loginpage import OrangeHRM_login
from utilities.logger import LogGenerator
from utilities.Readconfig import Readconfig
from utilities import XUTilities ;

class Test_Ddt_Add_Emp():
    username=Readconfig.GetUserName() ;
    password=Readconfig.GetPassword() ;

    log=LogGenerator.loggen();

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("Page Title Is Test Case")
    @allure.issue("ABC123")
    @allure.story("This Is Story #1 ")

    def test_ddt_addemp_005(self,setup):

        self.log.info(" Testcase test_ddt_addemp_005 Is Started ") ;

        self.log.info(" Opening The Browser ") ;

        self.driver=setup ;

        self.driver.implicitly_wait(5) ;

        self.lp=OrangeHRM_login(self.driver) ;

        self.log.info(" Entering Username "+self.username) ;
        self.lp.enter_username(self.username) ;

        self.log.info(" Entering Password "+self.password) ;
        self.lp.enter_password(self.password) ;

        self.log.info(" Clicking On Login Button ") ;
        self.lp.click_login_button();

        self.ae=Add_Emp(self.driver) ;

        path = "D:\\PYTHON CT15\\OrangeHRM\\testdata\\ddt.xlsx";
        rows = XUTilities.getRowCount(path, "Sheet1");

        self.log.info("Performing DDT")
        for r in range(2, rows + 1):

            fn=XUTilities.readData(path, "Sheet1", r, 1) ;
            mn=XUTilities.readData(path, "Sheet1", r, 2) ;
            ln=XUTilities.readData(path, "Sheet1", r, 3) ;

            self.log.info("Click Pim")
            self.ae.click_pim_tab();

            self.log.info("Click Add Emp Button") ;
            self.ae.click_add_emp_button();

            self.log.info("Enter First Name");
            self.ae.enter_first_name(fn) ;

            self.log.info("Enter Middle Name")
            self.ae.enter_middle_name(mn) ;

            self.log.info("Enter Last Name");
            self.ae.enter_last_name(ln) ;

            self.log.info("Get Employee Value");
            self.ae.get_id_value();

            self.log.info("Uploading Image");
            self.ae.upload_img();

            self.log.info("Click Save Button");
            self.ae.click_save_button() ;

            self.log.info("Cheking Success Message")
            if (self.ae.success_messge() == True) :
                print("Employee Added Successfully")
                XUTilities.writeData(path, "Sheet1", r, 4, "EMP_ADDED");
                assert True ;

            else:
                print("Invalid Operation") ;
                XUTilities.writeData(path, "Sheet1", r, 4,"ERROR")
                assert  False;

        self.log.info( "Testcase test_ddt_addemp_005 Is Completed" ) ;
