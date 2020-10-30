import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_SetUp():
    global driver
    driver = webdriver.Chrome('C:/Users/Hares/Desktop/Prestashop/Drivers/chromedriver')   

@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_verify_logo2():  
    driver.get("http://demo.prestashop.com/#/en/front")
    try:
        elem = driver.find_element_by_id("logfo").is_displayed()
        if elem ==True:
            assert True
            
    except Exception as e:
        print("there was an exception %s", str(e))
        assert False

def f():
    raise SystemExit(1)

@allure.severity(allure.severity_level.NORMAL)
def test_mytest():
    with pytest.raises(SystemExit):
        f()
@allure.severity(allure.severity_level.TRIVIAL)
def test_tearDown():
    assert False
    driver.close()
    
