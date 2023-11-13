from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from trio import serve_listeners

# Keep the browser ope after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()

wiki = driver.find_element(By.LINK_TEXT, value="Wikipedia")
# wiki.click()

search = driver.find_element(By.NAME, value='search')
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()