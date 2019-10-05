from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint

class CompanySearch(object):
    def __init__(self, website: str):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(website)

    def company_search(self, company_name: str) -> None:
        elem = self.driver.find_element_by_xpath("//input[@type='search']")
        elem.clear()
        elem.send_keys(company_name)
        elem.send_keys(Keys.RETURN)

    def obtain_results(self):
        company_links = dict()
        resultSet = self.driver.find_element_by_xpath("//ul[@class='results-list']").find_elements_by_tag_name("li")
        for result in resultSet:
            anchor_element = result.find_element_by_tag_name("a")
            company_name = anchor_element.text
            link = anchor_element.get_attribute("href")
            company_links[company_name] = link
        return company_links

    def end_session(self):
        self.driver.close()

if __name__ == "__main__":
    uk = CompanySearch("https://beta.companieshouse.gov.uk/")
    uk.company_search("Shell")
    company_links = uk.obtain_results()
    uk.end_session()

    pprint.pprint(company_links)