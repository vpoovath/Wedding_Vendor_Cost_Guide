import os
import time
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


VendorTuple = namedtuple("Vendor",
                         ['name',
                         'type',
                         'city',
                         'state',
                         'price',
                         'num_reviews',
                         'rating',
                         'link'])

# TODO: Delete these if you're still using a namedtuple to store vendor data
# Creating these getter functions in case
# want to add more functionality
class Vendor(VendorTuple):
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_price(self):
        return self.price

    def get_num_reviews(self):
        return self.num_reviews
    
    def get_link(self):
        return self.link

class VendorCategory:
    """
    This class is meant to store each individual's vendor info that is 
    scraped from the Wedding Wire.
    """
    def __init__(self, webdriver, url):
        self._url                             = url
        self._type                            = ""
        self._city                            = ""
        self._driver                          = None
        self._vendor_class                    = "vendorTile__content vendorTileQuickResponse__content"
        self._vendor_name_class               = "vendorTile__title app-vendor-tile-link"
        self._vendor_price_class              = "vendorTileFooter__info"
        self._vendor_num_reviews_class        = "vendorTile__contentRating"
        self._vendor_rating_class             = "vendorTile__rating"
        self._vendor_subtitle_class           = "vendorTile__subtitle link-marker"
        self._search_button_class             = "searcher__submit.app-searcher-submit-tracking"
        self._vendor_search_bar_class         = "searcher__category.app-filter-searcher-field.show-searcher-reset"
        self._vendor_search_bar_focus_class   = "searcher__category.app-filter-searcher-field.show-searcher-reset.focus"
        self._vendor_input_search_class       = "searcher__input.app-filter-searcher-input.app-searcher-category-input-tracking"
        self._vendor_popup_menu_class         = "searcher__placeholder.app-filter-searcher-list"
        self._vendor_popup_menu_open_class    = "searcher__placeholder.app-filter-searcher-list.open"
        self._vendor_dropdown_list_class      = "searcherCategoriesDropdownList"
        self._vendor_category_class           = "searcherCategoriesDropdownList__item"
        self._location_search_bar_class       = "searcher__location"
        self._location_search_bar_focus_class = "searcher__location.focus"
        self._location_search_bar_input_class = "searcher__input.app-searcher-location-input.app-searcher-location-input-tracking"
        self._location_popup_menu_class       = "searcher__placeholder.app-searcher-location-placeholder.open"
        self._location_dropdown_list_class    = "searcherLocationsDropdownList.active.app-searcher-location-tab-modal-content"

    def vendor():
        print("")

def init_chromedriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chromedir = f"{os.path.curdir}/chromedriver/stable/chromedriver"
    driver_service = Service(chromedir)
    driver = webdriver.Chrome(service=driver_service,
                              options=chrome_options)
    return driver

webdriver = init_chromedriver()
url = ""
v = VendorCategory(webdriver, url)
print(v)