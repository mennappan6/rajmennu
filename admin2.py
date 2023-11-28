from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "http://gcreddy.com/project/"
driver = webdriver.Firefox()

driver.get(url)

#1.verify that elements availability home page
if driver.find_element(By.XPATH, '//*[@id="columnLeft"]/div[1]/div[2]/a[1]').is_displayed():
    print("Displayed")
else:
    print(" Not Displayed")

if driver.find_element(By.ID, "bodyWrapper").is_displayed():
    print("Displayed")
else:
    print("Not Displayed")

#2.verify costemer login
def verify_user_login(email, password):
    driver.get("http://gcreddy.com/project/")
    time.sleep(4)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/a[3]").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div/form/table/tbody/tr[1]/td[2]/input").send_keys("mennappan@123")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div/form/table/tbody/tr[2]/td[2]/input").send_keys("menna678")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div/form/p[2]/span/button/span[2]").click()

try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="columnRight"]/div/div[1]/a')))
    print("Login successful!")
except Exception as e:
    print("Login failed. Exception: {}".format(str(P)))

#3.verify shopping card
def verify_shopping_card():
    driver.get("http://gcreddy.com/project/")
    driver.find_element(By.XPATH, '//*[@id="columnRight"]/div/div[1]/a').click()

    try:
        product_elemnts = driver.find_elements(By.CLASS_NAME, "product-item")
        assert len(product_elemnts) > 0, "Shopping card is empty"
        print("Shopping card contains item:")
        for product_elemnt in product_elemnts:
            product_name = product_elemnt.find_element(By.CLASS_NAME, "product-name").text
            product_price = product_elemnt.find_element(By.CLASS_NAME, "product-price").text
            print(f"- {product_name}, price: {product_price}")

    except Exception as e:
        print(f"Failed to verify shopping card. Exception: {str(e)}")

    driver.quit()

verify_shopping_card()

#4.verify checkout
def verify_checkout():
    driver.get("http://gcreddy.com/project/")
    driver.find_element(By.XPATH, '//*[@id="tdb4"]/span[2]').click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div/form/table/tbody/tr[1]/td[2]/input").send_keys("mennappan@123")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div/form/table/tbody/tr[2]/td[2]/input").send_keys("menna678")
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div/form/p[2]/span/button/span[2]").click()


    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tdb3"]/span[2]')))
        print("checkout successful!")
    except Exception as e:
        print(f"failed to verify checkout. Exception: {str(e)}")

driver.quit()
verify_checkout()







