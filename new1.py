from sele
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Raja:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver_firefox = webdriver.Firefox()
    driver_firefox.get(url)
    time.sleep(2)
    driver_firefox.find_element(By.NAME, "username").send_keys("Admin")
    driver_firefox.find_element(By.NAME, "password").send_keys("admin123")
    driver_firefox.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(5)
    driver_firefox.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
    time.sleep(7)
    driver_firefox.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()

    time.sleep(9)
    driver_firefox.find_element(By.NAME, "firstName").send_keys("raj")
    driver_firefox.find_element(By.NAME, "lastName").send_keys("menna")
    driver_firefox.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys("0261")
    driver_firefox.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()

    time.sleep(11)
    driver_firefox.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()

    time.sleep(13)
    driver_firefox.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()

    time.sleep(15)
    driver_firefox.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div").click()
    Element = driver_firefox.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]")
    print(len(Element))
    for opt in Element:
        if opt.text == "Admin":
            opt.click()
            break
#empoyee name
    act = ActionChains(webdriver)
    driver_firefox.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("raj menna")
    act.move_to_element(driver_firefox.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role='listbox']"))
    time.sleep(3)
    Search_Ele = driver_firefox.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role='listbox']/div")
    for tye in Search_Ele:
        if tye.text == "raj menna":
            tye.click()
            break

    #driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").click()
    #status Enabled
    driver_firefox.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div").click()
    Status_Ele = driver_firefox.find_elements(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]")
    print(len(Status_Ele))
    for sta in Status_Ele:
        if sta.text == "Enabled":
            sta.click()
            break

    driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("rajamsd")
    driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Mennaraja$11")
    driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Mennaraja$11")
    time.sleep(2)
    driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()
    time.sleep(3)
    driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
    time.sleep(2)
    driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("rajamsd")
    #search
    driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()

    #logout
    time.sleep(2)
    driver_firefox.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
    driver_firefox.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()

    #login
    time.sleep(3)
    driver_firefox.find_element(By.NAME, "username").send_keys("rajamsd")
    driver_firefox.find_element(By.NAME, "password").send_keys("Mennaraja$11")
    driver_firefox.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()


