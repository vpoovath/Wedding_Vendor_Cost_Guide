import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class VendorCategory:
    def __init__(self):
        self._url                             = ""
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


v = VendorCategory()
print(v)
