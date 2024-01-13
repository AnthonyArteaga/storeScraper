from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.dickblick.com/")

time.sleep(6)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Paint & Mediums")) #will wait 5 seconds to see if element exists before crashing
) 
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Paint & Mediums") #can also use PARTIAL_LINK_TEXT if looking for something not specific
link.click()

#currently at all the paint and mediums category URL on blick

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'departmentLinks__options css-eucynq e2wsta36')]")) 
) 

subCategoriesParent = driver.find_element(By.XPATH, "//ul[contains(@class, 'departmentLinks__options css-eucynq e2wsta36')]") 
subCategories = subCategoriesParent.find_elements(By.XPATH, ".//*")

#print(range(len(subCategories))) 175, i dont know why

paintCategories = []

for x in range(6,175,7):
    paintCategories.append(subCategories[x].text)

#=========================================================================================================================================================================


for elem in paintCategories: #sometimes doesnt go through all 25 paint/medium categories
    WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, elem)) 
    ) 
    link = driver.find_element(By.PARTIAL_LINK_TEXT, elem)
    link.click()


    #=====================================================================================================================================================================
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/main/div[2]/section/div/div/h2')) 
    ) 
    subCatHeaderElem = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/main/div[2]/section/div/div/h2').text

    if subCatHeaderElem=="Frequently Asked Questions": #this means there are no subcategories, should start going through each page
    #for each specific item listing, find a way to save the fullName, price, and any 'Product Details'
        #print("no subCats")

        # xpath for unsorted list of page buttons : //*[@id="productsHolder"]/div[1]/ul ; css-11awlpj ; //ul[contains(@class, 'css-11awlpj')]

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'css-11awlpj')]/li[last()-1]")) 
            ) 

            buttonsParent = driver.find_element(By.XPATH, "//ul[contains(@class, 'css-11awlpj')]")
            buttonNames = buttonsParent.find_elements(By.XPATH, ".//*")
            pageButtons =[]

            index=0
            while buttonNames[index].text != "next":
                pageButtons.append(buttonNames[index].text)
                index+=2
            
            #len(pageButtons) is how many total pages there are
            #need to go thru len-1 pages past page 1
                
            for page in range(len(pageButtons)-1):
                #WebDriverWait(driver, 5).until( #incase theres load time after going to next page
                #    EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'css-11awlpj')]/li[last()-1]")) 
                #) 
                #nxtButton = driver.find_element(By.XPATH, "//ul[contains(@class, 'css-11awlpj')]/li[last()-1]")
                
                #go thru all items
                #WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='productCarousel__products productsView_productList__lB3_8']/li")))
#USE webDriverWait somehow to stop using sleep

                unsorted_list = driver.find_elements(By.XPATH, "//ul[@class='productCarousel__products productsView_productList__lB3_8']/li")

                for i in range(len(unsorted_list)):
                    try:
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"(//ul[@class='productCarousel__products productsView_productList__lB3_8']/li)[{i+1}]")))
                        item = unsorted_list[i]
                        item.click()
                        
                        # Do stuff with the clicked item
                        print(i)

                        

                        time.sleep(1)

                        driver.back()

                        # Wait for the presence of the element before re-locating
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='productCarousel__products productsView_productList__lB3_8']/li")))
                        unsorted_list = driver.find_elements(By.XPATH, "//ul[@class='productCarousel__products productsView_productList__lB3_8']/li")

                    except (StaleElementReferenceException, TimeoutException):
                        # Handle the StaleElementReferenceException or TimeoutException by re-locating the elements
                        unsorted_list = driver.find_elements(By.XPATH, "//ul[@class='productCarousel__products productsView_productList__lB3_8']/li")

                driver.refresh()

                WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'css-11awlpj')]/li[last()-1]")))
                nxtButton = driver.find_element(By.XPATH, "//ul[contains(@class, 'css-11awlpj')]/li[last()-1]")
                nxtButton.click() #want this to happen until above elemnt(aka next button) doesnt exist
                time.sleep(1)

        except TimeoutException:
            #go through all items on the one page

            print("one page")

        
    else: #there exists sub categories and must go thru each then the pages ====================================================================================================



        print("subCats")
    
    

    time.sleep(1)

    driver.get("https://www.dickblick.com/categories/painting/")



time.sleep(10)

driver.quit()

