import time

import pytest
from selenium import webdriver


def pytest_addoption(parser) :
    parser.addoption("--browser") ;

@pytest.fixture()
def browser(request) :
    return request.config.getoption("--browser") ;

@pytest.fixture
def setup(browser):
    if ( browser == "chrome" ):
        driver=webdriver.Chrome() ;
    elif ( browser == "edge" ):
        driver=webdriver.Edge() ;
    else:
        chrome_options=webdriver.ChromeOptions();
        chrome_options.add_argument("headless");
        driver=webdriver.Chrome(options=chrome_options);

    driver.implicitly_wait(5) ;

    driver.maximize_window();

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2) ;

    yield driver ;

    driver.quit() ;