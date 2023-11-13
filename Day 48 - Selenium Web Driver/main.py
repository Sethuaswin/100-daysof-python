from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser ope after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
# driver.get("https://www.amazon.in/Samsung-40-62cm-Dynamic-Graphite-NP960XFG-KC2IN/dp/B0BSH4MRWR/ref=sr_1_16?crid=21KINA3YT0KRP&keywords=m2+macbook+air+15+inch&qid=1699867916&sprefix=m2+macbook+air%2Caps%2C206&sr=8-16")

# price_rupee = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price_rupee.text)

# price_rupee = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')
# print(price_rupee)

# submit = driver.find_element(By.NAME, value="1")
# print(submit.size)

# Fetching the upcoming events dates and event name from python.org
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()