from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
start_url = "https://npidb.org/doctors/allopathic_osteopathic_physicians/allergy-immunology_207k00000x/"
driver.get(start_url)
time.sleep(45)

doctor_links = driver.find_elements(By.XPATH, "//tbody//h2/a")

for link in doctor_links:
    doctor_url = link.get_attribute("href")
    driver.get(doctor_url)
    time.sleep(10)
    name = driver.find_element(By.XPATH, "//tbody//h2/a").get_attribute("title")
    address = driver.find_element(By.XPATH, "//div/address[@class='lead']//span").text
    phone = driver.find_element(By.XPATH, "//div/span[@itemprop='telephone']").text
    fax = driver.find_element(By.XPATH, "//div/span[@itemprop='faxNumber']").text
    print({
        'Name': name,
        'Specialty': address,
        'Phone Number': phone,
        'Fax': fax
    })

driver.quit()
