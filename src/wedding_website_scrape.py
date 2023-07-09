from bs4 import BeautifulSoup
import requests

#url    = "https://www.weddingwire.com/shared/search?id_grupo=&id_sector=8&id_region=&id_provincia=10069&id_poblacion=&id_geozona=&id_empresa=&distance=&lat=&long=&showmode=&NumPage=1&userSearch=1&isSearch=1&isHome=1&popularPriceRange%255B%255D=&txtLocSearch=San%20Antonio%20(City)"
page_num                     = 1
url                          = "https://www.weddingwire.com/shared/search?id_grupo=&id_sector=8&id_region=&\
                                id_provincia=10069&id_poblacion=&id_geozona=&id_empresa=&distance=&lat=&\
                                long=&showmode=&NumPage={page_num}&userSearch=1&isSearch=1&isHome=1&\
                                popularPriceRange%255B%255D=&txtLocSearch=San%20Antonio%20(City)"\
                                .format(page_num = page_num)

source                   = requests.get(url)
soup                     = BeautifulSoup(source.text,'lxml')
vendor_class             = "vendorTile__content vendorTileQuickResponse__content"
vendor_name_class        = "vendorTile__title app-vendor-tile-link"
vendor_price_class       = "vendorTileFooter__info"
vendor_num_reviews_class = "vendorTile__contentRating"
vendor_rating_class      = "vendorTile__rating"
vendor_subtitle_class    = "vendorTile__subtitle link-marker"
vendor                   = soup.find('div', class_=vendor_class)
vendor_name              = soup.find('a', class_=vendor_name_class)
vendor_price             = soup.find('div', class_=vendor_price_class)
vendor_num_reviews       = soup.find('div', class_=vendor_num_reviews_class)
vendor_rating            = soup.find('span', class_=vendor_rating_class)

#print(vendor_num_reviews.prettify())
#print(vendor_num_reviews.text.replace(" ", "").split("(")[-1].split(")")[0])
#print(vendor_rating.prettify())
#print(vendor_rating.text.replace(" ", "").split("(")[-1].split(")")[0])
#print(vendor.prettify())
#print(vendor_price.prettify())
#print(vendor_name.prettify())
#print(vendor_name.text.strip())
#print(vendor_price.text.strip())


# This doesn't quite work because you're just pulling all of the 
# matching classes, w/o regard for which vendor they belong to. 
# Better way would be to iterate through all upper-level vendor 
# divs, and then do a conditional find - if the value is missing 
# then put an "Null".
###############################################################################
#vendor_names = [vendor.text.strip() if vendor else "Null"
#                for vendor in soup.find_all('a', class_=vendor_name_class)]
#vendor_prices = [price.text.strip() if price else "Null"
#                 for price in soup.find_all('div',class_=vendor_price_class)]
#
#for i, price in enumerate(soup.find_all('div', class_=vendor_price_class)):
#    if price:
#        pass
#        #print("{i}:{k}".format(i=i, k=price.text.strip()))
#    else:
#        pass
#        #print("{i}:N/A".format(i=i))
#
#print(len(vendor_names))
#print(len(vendor_prices))
#print(vendor_names[0])
#print(vendor_prices[0])
#print(vendor_names[1])
#print(vendor_prices[1])
###############################################################################


def find_photography_vendors():
    """
    @param: None
    @out:   List of photography vendor names and their prices
    @error: None
    """
    vendor_class             = "vendorTile__content vendorTileQuickResponse__content"
    vendor_name_class        = "vendorTile__title app-vendor-tile-link"
    vendor_price_class       = "vendorTileFooter__info"
    vendor_subtitle_class    = "vendorTile__subtitle link-marker"
    vendor_num_reviews_class = "vendorTile__contentRating"
    vendor_rating_class      = "vendorTile__rating"

    vendors = {}
    for page_num in range(1,10,1):
        url = "https://www.weddingwire.com/shared/search?id_grupo=&id_sector=8&id_region=&\
                id_provincia=10069&id_poblacion=&id_geozona=&id_empresa=&distance=&lat=&\
                long=&showmode=&NumPage={page_num}&userSearch=1&isSearch=1&isHome=1&\
                popularPriceRange%255B%255D=&txtLocSearch=San%20Antonio%20(City)"\
                .format(page_num = page_num)

        source          = requests.get(url)
        soup            = BeautifulSoup(source.text,'lxml')
        vendor          = soup.find('div', class_=vendor_class)
        vendor_subtitle = soup.find('div',class_=vendor_subtitle_class)
        vendor_name     = soup.find('a', class_=vendor_name_class)
        vendor_price    = soup.find('div', class_=vendor_price_class)
        vendor_rating   = soup.find('span', class_=vendor_rating_class)

        for i, vendor in enumerate(soup.find_all('div', class_=vendor_class)):
            try:
                vendor_name = vendor.find('a', class_=vendor_name_class).text.strip()
            except Exception as e:
                vendor_name = "Null"

            try:
                vendor_price = vendor.find('div', class_=vendor_price_class).text.strip()
            except Exception as e:
                vendor_price = "Null"

            # TODO: Fix this, all the fields are returning NULL
            try:
                vendor_subtitle    = vendor.find('div', class_=vendor_subtitle_class)
                vendor_rating      = vendor_subtitle.find('span', class_=vendor_rating_class).text.strip()
                vendor_num_reviews = vendor_subtitle.find('div',
                                        class_=vendor_num_reviews_class).text.replace(" ", "").split("(")[-1].split(")")[0]
            except Exception as e:
                vendor_rating = "Null"
                vendor_num_reviews = "Null"

            vendors[vendor_name] = [vendor_price, vendor_rating, vendor_num_reviews]
    return vendors


photo_vendors = find_photography_vendors()
print(len(photo_vendors))
for key, value in photo_vendors.items():
    print("{name}: {price}, {rating}, {reviews}".format(name=key,
                                                        price=value[0],
                                                        rating=value[1],
                                                        reviews=value[2]))
