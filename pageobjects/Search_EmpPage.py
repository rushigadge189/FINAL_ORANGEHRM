from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Search_Emp():
    enter_empid_xpath=(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input');
    click_search_button_xpath=(By.XPATH, '//button[@type="submit"]') ;
    search_result_css=(By.CSS_SELECTOR, "div[class='oxd-table-card'] div:nth-child(3) div:nth-child(1)") ;

    def __init__(self,driver):
        self.driver=driver ;

    def enter_empid(self,empid):
        self.driver.find_element(*Search_Emp.enter_empid_xpath).send_keys(empid) ;

    def click_search_button(self):
        self.driver.find_element(*Search_Emp.click_search_button_xpath).click() ;

    def search_results(self):
        try:
            firstmiddlename=self.driver.find_element(*Search_Emp.search_result_css).text ;
            print(firstmiddlename);
            return  True ;

        except NoSuchElementException :
            return False ;