import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_setUp():
    global driver
    driver = webdriver.Chrome('C:/Users/Hares/Desktop/Prestashop/Drivers/chromedriver')

def test_verify_Menu():
    driver.get("http://demo.prestashop.com/#/en/front")
    try:
        cloths = driver.find_element_by_id("category-3").is_displayed()
        if clothes ==True:
            assert True
            
    except Exception as e:
        print("there was an exception %s", str(e))
        assert False

    try:
        accessories = driver.find_element_by_id("category-6").is_displayed()
        if accessories ==True:
            assert True
            
    except Exception as e:
        print("there was an exception %s", str(e))
        assert False

    try:
        art = driver.find_element_by_id("category-9").is_displayed()
        if art ==True:
            assert True
            
    except Exception as e:
        print("there was an exception %s", str(e))
        assert False
        #Testing

def test_tearDown():
    driver.close()
