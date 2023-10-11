import os
from dataclasses import dataclass, field
from typing import List, Any
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url                             = "https://www.weddingwire.com/"
type                            = ""
city                            = ""
vendor_class                    = "vendorTile__content vendorTileQuickResponse__content"
vendor_name_class               = "vendorTile__title app-vendor-tile-link"
vendor_price_class              = "vendorTileFooter__info"
vendor_num_reviews_class        = "vendorTile__contentRating"
vendor_rating_class             = "vendorTile__rating"
vendor_subtitle_class           = "vendorTile__subtitle link-marker"
search_button_class             = "searcher__submit.app-searcher-submit-tracking"
vendor_search_bar_class         = "searcher__category.app-filter-searcher-field.show-searcher-reset"
vendor_search_bar_focus_class   = "searcher__category.app-filter-searcher-field.show-searcher-reset.focus"
vendor_input_search_class       = "searcher__input.app-filter-searcher-input.app-searcher-category-input-tracking"
vendor_popup_menu_class         = "searcher__placeholder.app-filter-searcher-list"
vendor_popup_menu_open_class    = "searcher__placeholder.app-filter-searcher-list.open"
vendor_dropdown_list_class      = "searcherCategoriesDropdownList"
vendor_category_class           = "searcherCategoriesDropdownList__item"
location_search_bar_class       = "searcher__location"
location_search_bar_focus_class = "searcher__location.focus"
location_search_bar_input_class = "searcher__input.app-searcher-location-input.app-searcher-location-input-tracking"
location_popup_menu_class       = "searcher__placeholder.app-searcher-location-placeholder.open"
location_dropdown_list_class    = "searcherLocationsDropdownList.active.app-searcher-location-tab-modal-content"


def setup_webdriver(url="https://www.weddingwire.com/"):
    """
    """
    # Adding optinos to prevent a Google Chrome window from popping up
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    chromedir      = f"{os.path.curdir}/chromedriver/stable/chromedriver"
    driver_service = Service(chromedir)
    driver         = webdriver.Chrome(service=driver_service,
                                      options=chrome_options)
    driver.get(url)

    return driver

def teardown_webdriver(driver):
    """
    """
    driver.quit()

@dataclass
class Vendor:
    web_driver: webdriver.Chrome = field(default_factory=setup_webdriver)
    vendor_categories: List[str] = field(default_factory=None)
    name: str = field(default_factory="")
    type: str = field(default_factory="")
    city: str = field(default_factory="")
    state: str = field(default_factory="")
    price: str = field(default_factory=0)
    num_reviews: str = field(default_factory=0)
    rating: str = field(default_factory=0)
    link: str = field(default_factory="")

    def get_vendor_categories(self):
        """
        """
        return

    def find_vendor_elements(self):
        """
        """
        return

    def assign_name(self):
        """
        @param:
        @return:
        """
        vendor_name_class = "vendorTile__title.app-vendor-tile-link"
        try:
            self.name = self.webdriver.find_element(By.CLASS_NAME,
                                                    vendor_name_class).text.strip()
        except Exception as e:
            self.name = None
            print(e)

    def assign_city(self):
        """
        """
        return

    def assign_state(self):
        """
        """
        return
    
    def assign_price(self):
        """
        """
        return
    
    def assign_num_reviews(self):
        """
        """
        return

    def assign_rating(self):
        """
        """
        return
    
    def assign_link(self):
        """
        """
        return

    def assign_data(self):
        """
        """
        return


@dataclass
class AllVendors:
    vendors: List[Vendor]


def set_vendor_defaults():
    driver = setup_webdriver()
    return Vendor(driver, 'None', 'None','None','None','None','None','None','None','None')

# How do I simplify the Vendor init process...with defaults...?
test_vendor = set_vendor_defaults()

# Initialize Chrome Driver