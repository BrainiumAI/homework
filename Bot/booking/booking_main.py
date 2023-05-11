from selenium import webdriver
import booking.constants as const
import os
import time


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r'C:\SeleniumDrivers\')', teardown=False):
        
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path

        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        time.sleep(15)
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        else:
            pass


    def land_first_page(self):
        self.get(const.BASE_URL)

        