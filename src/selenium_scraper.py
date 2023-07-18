# Credit goes to this article explaining on how to make 
# Selenium and Webdrivers work on WSL2.
# https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2

# Credit also goes to the Selenium API docs, especially the Waits section:
# https://www.selenium.dev/documentation/webdriver/waits/

import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

page_num = 1
url = f"https://www.weddingwire.com/shared/search?group_id=2&region_id=10069&sector_id=8&state_id=443&page={page_num}"
url2 = "https://www.weddingwire.com/"

# Adding optinos to prevent a Google Chrome window from popping up
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

chromedir      = f"{os.path.curdir}/chromedriver/stable/chromedriver"
driver_service = Service(chromedir)
driver         = webdriver.Chrome(service=driver_service, options=chrome_options)

# The By.CLASS_NAME uses By.CSS_SELECTOR internally and therefore needs to have "." 
# where there are spaces (" ") - which we see when we "Inspect" elements in Chrome.
# Need valid CSS selector for an element that includes all those classes (i.e.
# separated by spaces).  Must "concatenate" them with "."
# To fix: Simply replace the spaces between the classes with "."
vendor_class             = "vendorTile__content.vendorTileQuickResponse__content"
vendor_name_class        = "vendorTile__title.app-vendor-tile-link"
vendor_price_class       = "vendorTileFooter__info"
vendor_subtitle_class    = "vendorTile__subtitle.link-marker"
vendor_num_reviews_class = "vendorTile__contentRating"
vendor_rating_class      = "vendorTile__rating"

#driver.get(url) # Interacting with the website
driver.get(url2) # Interacting with the website
vendor_elements = driver.find_elements(By.CLASS_NAME, vendor_class)

vendors = []
# TODO: Iterate through ALL the page numbers - make this dynamic since using
#       Selenium
for i, vendor in enumerate(vendor_elements):
    try:
        vendor_name_element = vendor_elements[i].find_element(By.CLASS_NAME,
                                                              vendor_name_class)
        vendor_name = vendor_name_element.text
    except:
        vendor_name = "Null"

    try:
        vendor_price_element = vendor_elements[i].find_element(By.CLASS_NAME,
                                                               vendor_price_class)
        vendor_price = vendor_price_element.text
    except:
        vendor_price = "Null"

    try:
        vendor_subtitle_element = vendor_elements[i].find_element(By.CLASS_NAME,
                                                                  vendor_subtitle_class)

        try:
            vendor_rating_element = vendor_elements[i].find_element(By.CLASS_NAME,
                                                                    vendor_rating_class)
            vendor_rating = vendor_rating_element.text
        except:
            vendor_rating = "Null"

        try:
            vendor_num_reviews_element = vendor_elements[i].find_element(By.CLASS_NAME,
                                                                         vendor_num_reviews_class)
            vendor_num_reviews = vendor_num_reviews_element.text.split("(")[-1].split(")")[0]
        except:
            vendor_num_reviews = "Null"

    except:
        vendor_rating = "Null"
        vendor_num_reviews = "Null"

    vendors.append({"vendor_name":vendor_name,
                    "price":vendor_price,
                    "rating":vendor_rating,
                    "num of reviews": vendor_num_reviews})

# The actual "SEARCH" button
search_button_class = "searcher__submit.app-searcher-submit-tracking"
search_button = driver.find_element(By.CLASS_NAME, search_button_class)
#print(location_search_bar.get_attribute("data-last-value"))

# Figuring out how to get each vendor and search their results
vendor_search_bar_class       = "searcher__category.app-filter-searcher-field.show-searcher-reset"
vendor_search_bar_focus_class = "searcher__category.app-filter-searcher-field.show-searcher-reset.focus"
vendor_input_search_class     = "searcher__input.app-filter-searcher-input.app-searcher-category-input-tracking"
vendor_popup_menu_class       = "searcher__placeholder.app-filter-searcher-list"
vendor_popup_menu_open_class  = "searcher__placeholder.app-filter-searcher-list.open"
vendor_dropdown_list_class    = "searcherCategoriesDropdownList"
vendor_category_class         = "searcherCategoriesDropdownList__item"

vendor_search_bar = driver.find_element(By.CLASS_NAME,
                                        vendor_search_bar_class)
vendor_search_bar.click()

vendor_search_bar_focus = driver.find_element(By.CLASS_NAME,
                                              vendor_search_bar_focus_class)
vendor_popup_menu = vendor_search_bar.find_element(By.CLASS_NAME,
                                                   vendor_popup_menu_class)
vendor_search_bar_focus.click()
vendor_popup_menu_open = WebDriverWait(vendor_search_bar_focus,
                                       timeout=1).until(lambda d:d.find_element(By.CLASS_NAME,
                                                                                vendor_popup_menu_open_class))
vendor_dropdown_list = vendor_popup_menu_open.find_element(By.CLASS_NAME,
                                                           vendor_dropdown_list_class)

for vend_cat in vendor_dropdown_list.find_elements(By.CLASS_NAME, vendor_category_class):
    vendor_category = vend_cat.find_element(By.TAG_NAME, "a")
    vendor_type = vendor_category.get_attribute("data-placeholder-name")
    vendor_link = vendor_category.get_attribute("href")

# Search bar for the city
location_search_bar_class       = "searcher__location"
location_search_bar_focus_class = "searcher__location.focus"
location_search_bar_input_class = "searcher__input.app-searcher-location-input.app-searcher-location-input-tracking"
location_popup_menu_class       = "searcher__placeholder.app-searcher-location-placeholder.open"
location_dropdown_list_class    = "searcherLocationsDropdownList.active.app-searcher-location-tab-modal-content"

location_search_bar_input = driver.find_element(By.CLASS_NAME, location_search_bar_class)
location_search_bar = driver.find_element(By.CLASS_NAME, location_search_bar_class)
location_search_bar.click()
location_search_bar_focus = driver.find_element(By.CLASS_NAME, location_search_bar_focus_class)
location_search_bar_focus.click()
location_popup_menu = WebDriverWait(location_search_bar_focus,
                                    timeout=1).until(lambda d:d.find_element(By.CLASS_NAME, location_popup_menu_class))

# We want to use these four cities to practice making a small dataset
# Then once we feel confident that for each vendor we are able to scrape
# all the data from San Antonio, Austin, Dallas, and Houston, then we can
# look to scrape the data from all the cities listed in the The Wedding Wire
# NOTE: That we are using the cities' search results. For some reason, the 
# search results that appear at the state level do not add up to the sum of the 
# search results that appear at the city level.
location_dropdown_list = location_popup_menu.find_element(By.CLASS_NAME,
                                                          location_dropdown_list_class)
satx = location_dropdown_list.find_element(By.XPATH,
                                           "//ul/li[a/@data-placeholder-name='San Antonio']")
dtx  = location_dropdown_list.find_element(By.XPATH,
                                           "//ul/li[a/@data-placeholder-name='Dallas']")
htx  = location_dropdown_list.find_element(By.XPATH,
                                           "//ul/li[a/@data-placeholder-name='Houston']")
atx  = location_dropdown_list.find_element(By.XPATH,
                                           "//ul/li[a/@data-placeholder-name='Austin']")
# This is how you want to collect the different vendors for each vendor
# category at each city...
satx_href = satx.find_element(By.TAG_NAME, "a").get_attribute("href")
driver.get(satx_href)
vendor             = driver.find_element(By.CLASS_NAME, vendor_class)
vendor_name        = vendor.find_element(By.CLASS_NAME, vendor_name_class)
vendor_price       = vendor.find_element(By.CLASS_NAME, vendor_price_class)
vendor_subtitle    = vendor.find_element(By.CLASS_NAME, vendor_subtitle_class)
vendor_rating      = vendor_subtitle.find_element(By.CLASS_NAME, vendor_rating_class).text.strip()
vendor_num_reviews = vendor_subtitle.find_element(By.CLASS_NAME, vendor_num_reviews_class).text.replace(" ", "").split("(")[-1].split(")")[0]
print(satx_href)
print(vendor_name.text)
print(vendor_price.text)
print(vendor_rating)
print(vendor_num_reviews)
#satx = location_dropdown_list.find_element(By.XPATH,
#                                           "//ul/li/a")
#dtx  = location_dropdown_list.find_element(By.XPATH,
#                                           "//ul/li/a")
#htx  = location_dropdown_list.find_element(By.XPATH,
#                                           "//ul/li/a")
#atx  = location_dropdown_list.find_element(By.XPATH,
#                                           "//ul/li/a")
#print(satx.get_attribute("data-place-holder-name"))
#print(satx.get_attribute("href"))
#print(dtx.get_attribute("data-place-holder-name"))
#print(dtx.get_attribute("href"))
#print(htx.get_attribute("data-place-holder-name"))
#print(htx.get_attribute("href"))
#print(atx.get_attribute("data-place-holder-name"))
#print(atx.get_attribute("href"))

driver.quit()
