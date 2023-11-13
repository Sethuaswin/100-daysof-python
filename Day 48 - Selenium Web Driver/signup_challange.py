from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep the browser ope after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("fisrt_name")

lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("last_name")

email = driver.find_element(By.NAME, value="email")
email.send_keys("some_email@email.com")

button = driver.find_element(By.CSS_SELECTOR, value='form button')
button.click()

# driver.quit()

