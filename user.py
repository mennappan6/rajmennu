from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

#1 launch application

url = "http://gcreddy.com/project/"
driver = webdriver.Firefox()
driver.get(url)

#2 View products
driver.get("http://gcreddy.com/project/")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[1]/div[2]/a[5]').click()
driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[1]/div[2]/a[8]').click()
driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[1]/div[2]/a[9]').click()
driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[1]/div[2]/a[11]').click()
driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[1]/div[2]/a[12]').click()
driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[1]/div[2]/a[15]').click()

#3 Advanced search
driver.get("http://gcreddy.com/project/")
driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[3]/div[2]/form/a/strong').click()
search_criteria = driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div/div[1]/input[1]').send_keys("shoes")
time.sleep(4)
search_button = driver.find_element(By.XPATH, '//*[@id="tdb4"]/span[1]').click()

#4 Customer registration
driver.get("http://gcreddy.com/project/")
driver.find_element(By.XPATH, '//*[@id="tdb3"]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="tdb2"]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[2]/table/tbody/tr[1]/td[2]/input[1]').click()
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').send_keys("mennappan")
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[2]/table/tbody/tr[3]/td[2]/input").send_keys("menna")
driver.find_element(By.ID, "dob").send_keys("11/07/1992")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[2]/table/tbody/tr[5]/td[2]/input').send_keys("rajamenna35@gmail.com")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[3]/table/tbody/tr/td[2]/input').send_keys("aks companyh")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[4]/table/tbody/tr[1]/td[2]/input').send_keys("suriya streat123")
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div/div[4]/table/tbody/tr[2]/td[2]/input").send_keys("raj nagar")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[4]/table/tbody/tr[4]/td[2]/input').send_keys("Chennai")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[4]/table/tbody/tr[3]/td[2]/input').send_keys("622202")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[4]/table/tbody/tr[5]/td[2]/input').send_keys("pudukkottai")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[4]/table/tbody/tr[6]/td[2]/select').send_keys("india")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[5]/table/tbody/tr[1]/td[2]/input').send_keys("+91 7064567865")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[5]/table/tbody/tr[2]/td[2]/input').send_keys("212-678-876")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[5]/table/tbody/tr[3]/td[2]/input').click()
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[6]/table/tbody/tr[1]/td[2]/input').send_keys("raja123456")
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/form/div/div[6]/table/tbody/tr[2]/td[2]/input').send_keys("raja123456")
driver.find_element(By.XPATH, '//*[@id="tdb4"]/span[2]').click()

#5 Customer login
driver.get('http://gcreddy.com/project/')
driver.find_element(By.XPATH, '//*[@id="bodyContent"]/div/div[1]/a[1]/u').click()
driver.find_element(By.XPATH, '//*[@id="loginModules"]/div[1]/div/form/table/tbody/tr[1]/td[2]/input').send_keys("rajamenna35@gmail.com")
driver.find_element(By.XPATH, '//*[@id="loginModules"]/div[1]/div/form/table/tbody/tr[2]/td[2]/input').send_keys("raja123456")
driver.find_element(By.XPATH, '//*[@id="tdb1"]/span[2]').click()










