# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# url = "https://www.linkedin.com"
#
# driver.get(url)
# element = driver.find_element(By.XPATH, "//nav/ul/li[4]")
# element.click()
# time.sleep(3)
# job_listings_xpath = "//ul[@class='jobs-search__results-list']//li"
# job_listings = driver.find_elements(By.XPATH, job_listings_xpath)
# print("Length :", len(job_listings))
#
#
# with open('linkedin_jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Title', 'Details', 'Description', 'Job Criteria']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for job in job_listings:
#         job.click()
#
#         time.sleep(8)
#
#         title_element = driver.find_element(By.XPATH, "//div//h1[@class='top-card-layout__title font-sans text-lg "
#                                                       "papabear:text-xl font-bold leading-open text-color-text mb-0 "
#                                                       "topcard__title']")
#         title = title_element.text
#         print(title)
#         details_elements = driver.find_elements(By.XPATH, "//div[@class='topcard__flavor-row']//span")
#         details = '\n'.join([detail.text for detail in details_elements])
#         print(details)
#         writer.writerow({'Title': title, 'Details': details})
#         time.sleep(3)
#         driver.back()
#         time.sleep(5)
#
# driver.quit()


import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://www.linkedin.com"

driver.get(url)
element = driver.find_element(By.XPATH, "//nav/ul/li[4]")
element.click()
time.sleep(3)
job_listings_xpath = "//ul[@class='jobs-search__results-list']//li"
job_listings = driver.find_elements(By.XPATH, job_listings_xpath)
print("Length :", len(job_listings))

with open('linkedin_jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Details', 'Description', 'Job Criteria']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for job in job_listings:
        print("JOB :", job)
        job.click()
        time.sleep(8)
        title_element = driver.find_element(By.XPATH, "//div//h1[@class='top-card-layout__title font-sans text-lg "
                                                      "papabear:text-xl font-bold leading-open text-color-text mb-0 "
                                                      "topcard__title']")
        title = title_element.text
        print(title)
        details_elements = driver.find_elements(By.XPATH, "//div[@class='topcard__flavor-row']//span")
        details = '\n'.join([detail.text for detail in details_elements])
        print(details)
        writer.writerow({'Title': title, 'Details': details})
        next_element = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/section[2]/div/a')
        next_element.click()
        time.sleep(5)
        company_size_element = driver.find_element(By.XPATH, "//*[@id='main-content']/section[1]/div/section[1]/div/dl/div[3]/dd")
        company_size = company_size_element.text
        print("Company Size:", company_size)
        driver.back()
        time.sleep(1)
        driver.back()
        time.sleep(5)
        # job_listings = driver.find_elements(By.XPATH, job_listings_xpath)

driver.quit()
