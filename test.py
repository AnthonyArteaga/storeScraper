from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

# Initialize the webdriver (you may need to specify the path to your webdriver executable)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.dickblick.com/products/blickrylic-student-acrylics/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, ' //*[@id="shop-products"]/div/div[2]/div[2]/div[3] ')) #will wait 5 seconds to see if element exists before crashing
) 

# Locate the parent div by its ID (replace 'parent_div_id' with the actual ID)
parent_div = driver.find_element(By.XPATH, ' //*[@id="shop-products"]/div/div[2]/div[2]/div[3] ')

# Get all nested div elements inside the parent div
nested_divs = parent_div.find_elements(By.TAG_NAME, "div")

count=0
# Print the text content of each nested div
for nested_div in nested_divs:
    print(nested_div.text)
    count+=1


print(f"rows counted: {count}")
time.sleep(30)
# Close the webdriver when done
driver.quit()