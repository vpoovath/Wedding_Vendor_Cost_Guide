#  THIS IS FOR REFERENCE ONLY - NOT ACTUAL PRODUCTION CODE

# Credit goes to this article explaining on how to make 
# Selenium and Webdrivers work on WSL2.
# https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2

# Credit also goes to the Selenium API docs, especially the Waits section:
# https://www.selenium.dev/documentation/webdriver/waits/

import os
import time
import csv
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url2 = "https://www.weddingwire.com/"

# NOTE:
# The By.CLASS_NAME uses By.CSS_SELECTOR internally and therefore needs to have "." 
# where there are spaces (" ") - which we see when we "Inspect" elements in Chrome.
# Need valid CSS selector for an element that includes all those classes (i.e.
# separated by spaces).  Must "concatenate" them with "."
# To fix: Simply replace the spaces between the classes with "."


#vendors = []
# TODO: Iterate through ALL the page numbers - make this dynamic since using
#       Selenium
#for i, vendor in enumerate(vendor_elements):
#    try:
#        vendor_name_element = vendor_elements[i].find_element(By.CLASS_NAME,
#                                                              vendor_name_class)
#        vendor_name = vendor_name_element.text
#    except:
#        vendor_name = "Null"
#
#    try:
#        vendor_price_element = vendor_elements[i].find_element(By.CLASS_NAME,
#                                                               vendor_price_class)
#        vendor_price = vendor_price_element.text
#    except:
#        vendor_price = "Null"
#
#    try:
#        vendor_subtitle_element = vendor_elements[i].find_element(By.CLASS_NAME,
#                                                                  vendor_subtitle_class)
#
#        try:
#            vendor_rating_element = vendor_elements[i].find_element(By.CLASS_NAME,
#                                                                    vendor_rating_class)
#            vendor_rating = vendor_rating_element.text
#        except:
#            vendor_rating = "Null"
#
#        try:
#            vendor_num_reviews_element = vendor_elements[i].find_element(By.CLASS_NAME,
#                                                                         vendor_num_reviews_class)
#            vendor_num_reviews = vendor_num_reviews_element.text.split("(")[-1].split(")")[0]
#        except:
#            vendor_num_reviews = "Null"
#
#    except:
#        vendor_rating = "Null"
#        vendor_num_reviews = "Null"
#
#    vendors.append({"vendor_name":vendor_name,
#                    "price":vendor_price,
#                    "rating":vendor_rating,
#                    "num of reviews": vendor_num_reviews})

## Find each vendor category and search their results
#vendor_search_bar_class       = "searcher__category.app-filter-searcher-field.show-searcher-reset"
#vendor_search_bar_focus_class = "searcher__category.app-filter-searcher-field.show-searcher-reset.focus"
#vendor_input_search_class     = "searcher__input.app-filter-searcher-input.app-searcher-category-input-tracking"
#vendor_popup_menu_class       = "searcher__placeholder.app-filter-searcher-list"
#vendor_popup_menu_open_class  = "searcher__placeholder.app-filter-searcher-list.open"
#vendor_dropdown_list_class    = "searcherCategoriesDropdownList"
#vendor_category_class         = "searcherCategoriesDropdownList__item"
#
#vendor_search_bar = driver.find_element(By.CLASS_NAME,
#                                        vendor_search_bar_class)
#vendor_search_bar.click()
#
#vendor_search_bar_focus = driver.find_element(By.CLASS_NAME,
#                                              vendor_search_bar_focus_class)
#
#vendor_popup_menu = vendor_search_bar.find_element(By.CLASS_NAME,
#                                                   vendor_popup_menu_class)
#vendor_search_bar_focus.click()
#
#vendor_popup_menu_open = WebDriverWait(vendor_search_bar_focus,
#                                       timeout=2).until(lambda d:d.find_element(By.CLASS_NAME,
#                                                                                vendor_popup_menu_open_class))
#vendor_dropdown_list = vendor_popup_menu_open.find_element(By.CLASS_NAME,
#                                                           vendor_dropdown_list_class)
#
#for vend_cat in vendor_dropdown_list.find_elements(By.CLASS_NAME, vendor_category_class):
#    vendor_category = vend_cat.find_element(By.TAG_NAME, "a")
#    vendor_type = vendor_category.get_attribute("data-placeholder-name")
#    vendor_link = vendor_category.get_attribute("href")
#    print(vendor_type)
#    print(vendor_link)

def setup_webdriver(url="https://www.weddingwire.com/"):
    """
    """
    # Adding optinos to prevent a Google Chrome window from popping up
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    chromedir      = f"{os.path.curdir}/chromedriver/stable/chromedriver"
    driver_service = Service(chromedir)
    driver         = webdriver.Chrome(service=driver_service, options=chrome_options)

    driver.get(url)

    return driver

def teardown_webdriver(driver):
    """
    """
    driver.quit()

# TODO: Split up and rename the function. The following things are done here:
# 1. The vendor category popup menu is opened and returned to allow the next
#    function to find search results in a given city
# 2. The list of all vendor categories is created
def get_vendor_categories(driver):
    """
    """
    vendor_categories = []

    # Find each vendor category and search their results
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
                                           timeout=2).until(lambda d:d.find_element(By.CLASS_NAME,
                                                                                    vendor_popup_menu_open_class))
    vendor_dropdown_list = vendor_popup_menu_open.find_element(By.CLASS_NAME,
                                                               vendor_dropdown_list_class)

    # Put this into a separate function/object class and use these categories and hrefs
    # to search and build the dataset
    for vend_cat in vendor_dropdown_list.find_elements(By.CLASS_NAME, vendor_category_class):
        vendor_category = vend_cat.find_element(By.TAG_NAME, "a")
        vendor_type = vendor_category.get_attribute("data-placeholder-name")
        vendor_link = vendor_category.get_attribute("href")
        vendor_categories.append((vendor_type, vendor_link))

    return vendor_categories

def get_location_dropdown_list(driver):
    """
    """
    # The actual "SEARCH" button
    #search_button_class = "searcher__submit.app-searcher-submit-tracking"
    #search_button = driver.find_element(By.CLASS_NAME, search_button_class)

    # Search bar for the city
    location_search_bar_class       = "searcher__location"
    location_search_bar_focus_class = "searcher__location.focus"
    location_search_bar_input_class = "searcher__input.app-searcher-location-input.app-searcher-location-input-tracking"
    location_popup_menu_class       = "searcher__placeholder.app-searcher-location-placeholder.open"
    location_dropdown_list_class    = "searcherLocationsDropdownList.active.app-searcher-location-tab-modal-content"

    location_search_bar_input = driver.find_element(By.CLASS_NAME, location_search_bar_class)
    location_search_bar       = driver.find_element(By.CLASS_NAME, location_search_bar_class)
    location_search_bar.click()
    location_search_bar_focus = driver.find_element(By.CLASS_NAME, location_search_bar_focus_class)
    location_search_bar_focus.click()
    location_popup_menu = WebDriverWait(location_search_bar_focus,
                                        timeout=2).until(lambda d:d.find_element(By.CLASS_NAME,
                                                                                 location_popup_menu_class))
    location_dropdown_list = location_popup_menu.find_element(By.CLASS_NAME,
                                                              location_dropdown_list_class)
    return location_dropdown_list

def get_city_href(location_dropdown_list, city_name):
    """
    """
    city = location_dropdown_list.find_element(By.XPATH, 
                                               "//ul/li[a/@data-placeholder-name='{city}']".format(city=city_name))
    city_href = city.find_element(By.TAG_NAME, "a").get_attribute("href")
    return city_href

def get_next_page(driver):
    """
    @param: driver - Selenium WebDriver element.

    @return: <str> - A string that contents the URL/HREF to the next page.

    """
    # Class for the "Next" and "Previous" buttons on the bottom of the search results
    button_container_class = "listingContent__pagination.app-pagination-container"
    next_button_span_class = "pagination__next" 
    next_button_class      = "button.button--block.button--tertiary.app-pagination-link"
    try:
        button_container = driver.find_element(By.CLASS_NAME, button_container_class)
        next_button_span = button_container.find_element(By.CLASS_NAME, next_button_span_class)
        next_button = next_button_span.find_element(By.CLASS_NAME, next_button_class)
        return next_button.get_attribute("data-href")
    except Exception as e:
        return None

def get_prev_page(curr_page):
    """
    """
    # Class for the "Next" and "Previous" buttons on the bottom of the search results
    button_container_class = "listingContent__pagination.app-pagination-container"
    prev_button_span_class = "pagination__prev"
    prev_button_class      = "button.button--block.button--tertiary.app-pagination-link"
    try:
        button_container = driver.find_element(By.CLASS_NAME, button_container_class)
        prev_button_span = button_container.find_element(By.CLASS_NAME, prev_button_span_class)
        prev_button = prev_button_span.find_element(By.CLASS_NAME, prev_button_class)
        return prev_button.get_attribute("data-href")
    except Exception as e:
        return None

def go_to_page_num(page_num):
    """
    @param: curr_page -  an integer representing the desired page number the
                         user wants the WebDriver to go to.
    @return: page_num_str - a string of the format '&page_num=N' where N is a
                            valid page number. This string is used to update
                            the URL to move to the desired page.
    """
    page_num_str = "&page_num={p}".format(p=page_num)
    return page_num_str

def get_num_search_results(driver):
    """
    """
    # Class for Number of Search Results
    num_results_class = "filterButtonBar__results.app-number-of-results"
    num_results = int(driver.find_element(By.CLASS_NAME, num_results_class).get_attribute("data-num-results"))
    return num_results

def get_vendors(drivers, webpage, vendor_type=None):
    """
    """
    # TODO: Create this into a class/subclass
    vendors = []
    vendor_class = "vendorTile__content.vendorTileQuickResponse__content"
    # Load the first page of search results and grab the total number of results
    driver.get(webpage)
    num_results = get_num_search_results(driver)

    #while (len(vendors) < num_results):
    while(webpage):
        driver.get(webpage)
        try: 
            temp_vendors = [get_vendor_data(v, vendor_type) for v in driver.find_elements(By.CLASS_NAME, vendor_class)]
            vendors.extend(temp_vendors)
            webpage = get_next_page(driver) # If there is a 'Next' page, then grab it
        except Exception as e:
            # TODO: Figure out how to do something useful here for debugging...
            vendors.extend([])
            break
    return vendors

def get_vendor_name(vendor):
    """
    @param:
    @return:
    """
    vendor_name_class = "vendorTile__title.app-vendor-tile-link"
    try:
        name = vendor.find_element(By.CLASS_NAME, vendor_name_class).text.strip()
    except Exception as e:
        name = None
        print(e)
    return name

def get_vendor_city(vendor):
    """
    @param:

    @return:
    """
    vendor_name_class = "vendorTile__location"
    city = vendor.find_element(By.CLASS_NAME, vendor_name_class).text.strip().split(",")[0]
    city = city.replace("·", "").strip()
    return city

def get_vendor_state(vendor):
    """
    @param:

    @return:
    """
    vendor_name_class = "vendorTile__location"
    state = vendor.find_element(By.CLASS_NAME, vendor_name_class).text.strip().split(",")[1]
    state = state.strip()
    return state

# TODO: Implement some cleaning on the price field either in separate function 
#       OR separate preprocessing script
def get_vendor_price(vendor):
    """
    @param:

    @return:
    """
    vendor_price_class = "vendorTileFooter__info"
    try:
        vendor_price = vendor.find_element(By.CLASS_NAME, vendor_price_class).text.strip()
    except Exception as e:
        vendor_price = "Null"
    return vendor_price

def get_vendor_rating(vendor):
    """
    @param:

    @return:
    """
    vendor_subtitle_class = "vendorTile__subtitle.link-marker"
    vendor_rating_class   = "vendorTile__rating"
    try:
        subtitle = vendor.find_element(By.CLASS_NAME, vendor_subtitle_class)
        rating   = subtitle.find_element(By.CLASS_NAME, vendor_rating_class).text.strip()
    except Exception as e:
        rating = None
    return rating

def get_vendor_num_reviews(vendor):
    """
    @param:

    @return:
    """
    vendor_subtitle_class    = "vendorTile__subtitle.link-marker"
    vendor_num_reviews_class = "vendorTile__contentRating"
    try:
        subtitle    = vendor.find_element(By.CLASS_NAME, vendor_subtitle_class)
        num_reviews = subtitle.find_element(By.CLASS_NAME, vendor_num_reviews_class).text.replace(" ", "").split("(")[-1].split(")")[0]
    except Exception as e:
        num_reviews = None
    return num_reviews

def get_vendor_link(vendor):
    """
    @param:

    @return:
    """
    vendor_name_class = "vendorTile__title.app-vendor-tile-link"
    try:
        name = vendor.find_element(By.CLASS_NAME, vendor_name_class)
        link = name.get_attribute("href")
    except Exception as e:
        link = ""
        print(e)
    return link

def get_vendor_data(vendor, vendor_type=None):
    """
    @param: vendor = A Selenium WebElement type in which we can search for specific data and attributes
                     by class, tag type, XPATH, etc.

    @return: A VendorTuple (namedtuple) that contains the vendor's name, type, city, state, price, 
             the no. of reviews, and website link.
    """
    # TODO: Extend this into a class in wedding_vendor.py file
    VendorTuple = namedtuple("Vendor",
                             ['name',
                             'type',
                             'city',
                             'state',
                             'price',
                             'num_reviews',
                             'rating',
                             'link'])
    type = vendor_type
    name = get_vendor_name(vendor)
    city = get_vendor_city(vendor)
    state = get_vendor_state(vendor)
    price = get_vendor_price(vendor)
    num_reviews = get_vendor_num_reviews(vendor)
    rating = get_vendor_rating(vendor)
    link = get_vendor_link(vendor)

    vend_tup=VendorTuple(name,
                         type,
                         city,
                         state,
                         price,
                         num_reviews,
                         rating,
                         link)

    return vend_tup

# We want to use these four cities to practice making a small dataset
# Then once we feel confident that for each vendor we are able to scrape
# all the data from San Antonio, Austin, Dallas, and Houston, then we can
# look to scrape the data from all the cities listed in the The Wedding Wire
# NOTE: That we are using the cities' search results. For some reason, the 
# search results that appear at the state level do not add up to the sum of the 
# search results that appear at the city level.
# This is how you want to collect the different vendors for each vendor
# category at each city...
driver = setup_webdriver()

# Use Wedding Venues as the test category. First we grab the name and href and then go to the
# website for the Wedding Venues search bar.
vendor_categories = get_vendor_categories(driver)

for vendor_cat in vendor_categories:
    vendor_cat_name = vendor_cat[0]
    vendor_cat_link = vendor_cat[1]
    driver.get(vendor_cat_link)

    #num_results = get_num_search_results(driver)
    city_name = "San Antonio" # TODO: Make this into a data field called "nearest_metro"

    location_dropdown_list = get_location_dropdown_list(driver)
    satx_href = get_city_href(location_dropdown_list, city_name)
    vendors = get_vendors(driver, satx_href, vendor_cat_name)

    # TODO: Add in a timestamp to the filename for differentiation
    csv_filename = "{}_test.csv".format(vendor_cat_name)

    # TODO: Delete this when in production, keep all files and differentiate them with a timestamp
    if os.path.exists(csv_filename):
        os.remove(csv_filename)

    with open(csv_filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(list(vendors[0]._fields)) # All vendors are namedtuples with same fields

    with open(csv_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        for vendor in vendors:
            csvwriter.writerow([data for data in vendor])
    
    print(vendor_cat_name)

teardown_webdriver(driver)

# TODO: Delete
#######################################################################################################################
# Quick check
#print(vendor_categories)
#print("No. Search Results: {a}".format(a=num_results))
#print("No. Vendors: {a}".format(a=len(vendors)))
#
#temp_vendor = vendors[0]
#print("Vendor Name: {}".format(temp_vendor.name))
#print("Vendor Type: {}".format(temp_vendor.type))
#print("Vendor City: {}".format(temp_vendor.city))
#print("Vendor State: {}".format(temp_vendor.state))
#print("Vendor Price: {}".format(temp_vendor.price))
#print("Vendor Rating: {}".format(temp_vendor.rating))
#print("Vendor No. Reviews: {}".format(temp_vendor.num_reviews))
#print("Vendor Link: {}".format(temp_vendor.link))


## Dallas
#print("\n")
#dtx  = location_dropdown_list.find_element(By.XPATH, "//ul/li[a/@data-placeholder-name='Dallas']")
#dtx_href  = dtx.find_element(By.TAG_NAME, "a").get_attribute("href")
#driver.get(dtx_href)
#
#try:
#    vendor = driver.find_element(By.CLASS_NAME, vendor_class)
#except NoSuchElementException as e:
#    vendor = None
#
#try:
#    vendor_name = vendor.find_element(By.CLASS_NAME, vendor_name_class)
#except NoSuchElementException as e:
#    vendor_name = None
#
#vendor_price = vendor.find_element(By.CLASS_NAME, vendor_price_class)
#
#vendor_subtitle = vendor.find_element(By.CLASS_NAME, vendor_subtitle_class)
#
#vendor_rating = vendor_subtitle.find_element(By.CLASS_NAME, vendor_rating_class).text.strip()
#
#vendor_num_reviews = vendor_subtitle.text.split("\n")[1].replace(")", "").replace("(","")
#
#print(dtx_href)
#print(vendor_name.text)
#print(vendor_price.text.replace("\n", ""))
#print(vendor_rating)
#print(vendor_num_reviews)
#
## Houston
#print("\n")
#htx  = location_dropdown_list.find_element(By.XPATH, "//ul/li[a/@data-placeholder-name='Houston']")
#htx_href  = htx.find_element(By.TAG_NAME, "a").get_attribute("href")
#driver.get(htx_href)
#vendor             = driver.find_element(By.CLASS_NAME, vendor_class)
#vendor_name        = vendor.find_element(By.CLASS_NAME, vendor_name_class)
#vendor_price       = vendor.find_element(By.CLASS_NAME, vendor_price_class)
#vendor_subtitle    = vendor.find_element(By.CLASS_NAME, vendor_subtitle_class)
#vendor_rating      = vendor_subtitle.find_element(By.CLASS_NAME, vendor_rating_class).text.strip()
#vendor_num_reviews = vendor_subtitle.text.split("\n")[1].replace(")", "").replace("(","")
#print(htx_href)
#print(vendor_name.text)
#print(vendor_price.text.replace("\n", ""))
#print(vendor_rating)
#print(vendor_num_reviews)
#
#print("\n")
#atx  = location_dropdown_list.find_element(By.XPATH, "//ul/li[a/@data-placeholder-name='Austin']")
#atx_href = atx.find_element(By.TAG_NAME, "a").get_attribute("href")
#driver.get(atx_href)
#vendor = driver.find_element(By.CLASS_NAME, vendor_class)
#
#print(atx_href)
#try:
#    vendor_name = vendor.find_element(By.CLASS_NAME, vendor_name_class)
#    print(vendor_name.text)
#except Exception as e:
#    vendor_name = None
#
#try:
#    vendor_price = vendor.find_element(By.CLASS_NAME, vendor_price_class)
#    print(vendor_price.text.replace("\n", ""))
#except Exception as e:
#    vendor_price = None
#
#try:
#    vendor_subtitle = vendor.find_element(By.CLASS_NAME, vendor_subtitle_class)
#
#    try:
#        vendor_rating = vendor_subtitle.find_element(By.CLASS_NAME, vendor_rating_class).text.strip()
#        print(vendor_rating)
#    except Exception as e:
#        vendor_Rating = None
#
#    vendor_num_reviews = vendor_subtitle.text.split("\n")[1].replace(")", "").replace("(","")
#    print(vendor_num_reviews)
#
#except Exception as e:
#    vendor_subttile = None
#
#print("End of Selenium Scraper")