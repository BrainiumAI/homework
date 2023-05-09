import pytest
from selenium import webdriver

def test_url_navigation():
    driver = webdriver.Chrome()

    url = "https://www.cannabisbusinesstimes.com/news/5-tips-to-maintain-a-healthy-organic-living-soil-for-your-indoor-cannabis-facility"
    driver.get(url)
    
    assert driver.current_url == url
    driver.quit()

def test_page_title():
    driver = webdriver.Chrome()

    url = "https://www.cannabisbusinesstimes.com/news/5-tips-to-maintain-a-healthy-organic-living-soil-for-your-indoor-cannabis-facility"
    driver.get(url)

    expected_title = "5 Tips to Maintain a Healthy, Organic Living Soil for Your Indoor Cannabis Facility"
    assert driver.title == expected_title
    driver.quit()
