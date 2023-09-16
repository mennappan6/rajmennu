from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Testguvi():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        self.driver.close()

    #Test Case user lohin
    def testlogin_01(self, setup):
        self.driver.get("https://www.demoblaze.com/")

    #Test Case sign up
    def testlogin_02(self, setup):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.find_element(By.ID, "signin2").click()
        self.driver.find_element(By.ID, "sign-username").send_keys("mennappan")
        self.driver.find_element(By.ID, "sign-password").send_keys("mennappan123")
        self.driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()

    #Test case login
    def testlogin_03(self, setup):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.find_element(By.ID, "login2").click()
        self.driver.find_element(By.ID, "loginusername").send_keys("mennappan")
        self.driver.find_element(By.ID, "loginpassword").send_keys("mennappan123")
        self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

    #Test Case ADD to Card
    def testlogin_04(self, setup):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.find_element(By.XPATH, '//*[@id="itemc"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/div/h4/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a').click()

    #Test Case place order
    def testlogin_05(self, setup):
        self.driver.get("https://www.demoblaze.com/")
        self.driver.find_element(By.XPATH, '//*[@id="cartur"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button').click()
        self.driver.find_element(By.ID, "name").send_keys("mennappan m")
        self.driver.find_element(By.ID, "country").send_keys("India")
        self.driver.find_element(By.ID, "city").send_keys("Tamilnadu")
        self.driver.find_element(By.ID, "card").send_keys("4564 2345 5643 6754")
        self.driver.find_element(By.ID, "month").send_keys("april")
        self.driver.find_element(By.ID, "year").send_keys("2024")
        self.driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()

