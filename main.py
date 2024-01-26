from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

Options = Options()
Options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options)

driver.get("https://www.neuralnine.com/")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break
    
    

book_links = driver.find_elements("xpath","//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 in 1')]]]")