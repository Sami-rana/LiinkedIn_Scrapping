import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://www.linkedin.com"

driver.get(url)
element = driver.find_element(By.XPATH, "//html/body/nav/ul/li[4]/a")
element.click()
time.sleep(5)
job_listings_xpath = "//div//main//section//ul[@class='jobs-search__results-list']//li"
job_listings = driver.find_elements(By.XPATH, job_listings_xpath)

with open('linkedin_jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Details', 'Description', 'Job Criteria']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for job in job_listings:
        job.click()

        time.sleep(10)

        title_element = driver.find_element(By.XPATH, "//div//h1[@class='top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title']")
        title = title_element.text
        print(title)
        details_element = driver.find_element(By.XPATH, "//div[@class='topcard__flavor-row']")
        details = details_element.text
        print(details)
        description_elements = driver.find_elements(By.XPATH, '//div//section//div[@class="show-more-less-html__markup relative overflow-hidden"]//p')
        description = ''
        for element in description_elements:
            description += element.text + '\n'

        description = description.strip()
        print(description)
        criteria_elements = driver.find_elements(By.XPATH, "//div[@class='description__job-criteria-list']//li")
        job_criteria = '\n'.join([criteria.text for criteria in criteria_elements])
        writer.writerow({'Title': title, 'Details': details, 'Description': description, 'Job Criteria': job_criteria})
        driver.back()

        # time.sleep(3)
        # job_listings = driver.find_elements(By.XPATH, job_listings_xpath)

driver.quit()











# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# url = "https://www.linkedin.com"
#
# driver.get(url)
# element = driver.find_element(By.XPATH, "//html/body/nav/ul/li[4]/a")
# element.click()
# time.sleep(5)
# job_listings_xpath = "//div//main//section//ul[@class='jobs-search__results-list']//li"
# job_listings = driver.find_elements(By.XPATH, job_listings_xpath)
#
# with open('linkedin_jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Title', 'Details', 'Description', 'Job Criteria']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for job in job_listings:
#         job_listings = job.find_element(By.XPATH, "//div//main//section//ul[@class='jobs-search__results-list']//li") # Extract job title
#         job.click()
#
#         time.sleep(10)
#
#         title_element = driver.find_element(By.XPATH, "//div//h1[@class='top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title']")
#         title = title_element.text
#         print(title)
#         details_element = driver.find_element(By.XPATH, "//div[@class='topcard__flavor-row']")
#         details = details_element.text
#         print(details)
#         description_elements = driver.find_elements(By.XPATH, '//div//section//div[@class="show-more-less-html__markup relative overflow-hidden"]//p')
#         description = ''
#         for element in description_elements:
#             description += element.text + '\n'
#
#         description = description.strip()
#         print(description)
#         criteria_elements = driver.find_elements(By.XPATH, "//div[@class='description__job-criteria-list']//li")
#         job_criteria = '\n'.join([criteria.text for criteria in criteria_elements])
#         writer.writerow({'Title': title, 'Details': details, 'Description': description, 'Job Criteria': job_criteria})
#         driver.back()
#
#         time.sleep(5)  # Add a short pause to allow the page to load and elements to become ready again
#
# driver.quit()


show_description = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section['
                                                 '1]/div/div/section/button[1]')
show_description.click()

description_elements = driver.find_elements(By.XPATH,
                                            '//div[@class="show-more-less-html__markup relative overflow-hidden"]//p')
description = ''
for element in description_elements:
    description += element.text + '\n'

description = description.strip()
print(description)
criteria_elements = driver.find_elements(By.XPATH, '//ul[@class="description__job-criteria-list"]//li')
job_criteria = '\n'.join([criteria.text for criteria in criteria_elements])