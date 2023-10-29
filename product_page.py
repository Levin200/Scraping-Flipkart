"""
product_details_insert is a function which is use to scrape the information from the product page using the 
product URL and store those information in csv files using csv_convertor
"""
from bs4 import BeautifulSoup
import csv_converter
import requests
import logging
import time


def product_details_insert(product_id, url):

    logging.basicConfig(level=logging.DEBUG,filename='logs\product.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting Product Details Insertion")
    
# ------------------ %%%% GET THE PAGE %%%%--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    headers = {'Origin': 'http://flipkart.com',
        'Referer': 'http://flipkart.com',
        'User-Agent': 'Chrome/54.0.2840.90'}
    #url = "https://www.flipkart.com/realme-buds-2-wired-headset/p/itm393326c26b6ad?pid=ACCFKYE2ARGG67WC&lid=LSTACCFKYE2ARGG67WCEU0OSD&marketplace=FLIPKART&q=headphones&store=0pm%2Ffcn&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=75589135-9b4e-4db9-bf33-60d67cee834e.ACCFKYE2ARGG67WC.SEARCH&ppt=None&ppn=None&ssid=cajrxlfnao0000001695971396877&qH=edd443896ef5dbfc"

    #response = requests.get(url= url, headers= headers)
    #print(response, response.status_code)

    # testing for response from the page
    for i in range(4):
        response = requests.get(url= url, headers= headers)
        #print(response, response.status_code)
        if response.status_code == 200:
            break
        logging.warning(response)
        time.sleep(i*2)
    else:
        print("error in page")
        logging.error("Response status code: {}".format(response.status_code))
        return

    logging.info("Response status code {}".format(response.status_code))
    html_content = response.content

    product_page = BeautifulSoup(html_content, 'html.parser')

# ---------------------- %%%% For Scrape the Product Details %%%%--------------------------------------------------------------------------------------------------------
    try: 
        # Get Product Price
        price = product_page.find('div', '_30jeq3 _16Jk6d') # get the tag <div class='_30jeq3 _16Jk6d'>₹22</div>
        price = price.text.strip("₹") # gets the price and removes '₹'
        price = int(price.replace(",","")) # replaces ',' with no spaces
    
    
        try:
            # Check if actual price exsists or not 
            # If exsists 
            actual_price = product_page.find('div', '_3I9_wc') #  get the tag <div class='_3I9_wc'>₹44</div>
            actual_price = actual_price.text.strip("₹") # gets the actual value and removes '₹'
            actual_price = int(actual_price.replace(",","")) # replaces ',' with no spaces
            logging.info("price: {}, actual_price {}".format( str(price), str(actual_price)))

        except:
            # If not esists then actual price is equal to price
            logging.warning("{} has no actual price".format(product_id)) # if no actual price is found
            actual_price = price 

# ------------- get reviews & ratings from the product page -----------------------------------------------------------------------
        reviews = product_page.find_all('p', class_ = '_2-N8zT') #  get the tag <p class='_2-N8zT'>reviews...</p>
        pd_reviews = [] # empty list to add all the reviews
        for i in range(len(reviews)):
            pd_reviews.append(reviews[i].text)
        logging.info("{}".format(pd_reviews))

        try:
            # get the ratings from the product page
            ratings = product_page.find('div', class_ = '_2d4LTz')  # get the tag <div class='_2d4LTz'>4.4</div>
            ratings = ratings.text

            # get the review counts
            review_count = product_page.find_all('div', class_ = 'row _2afbiS')  # get the tag <div class='row _2afbiS'>...</div>
            ratings_count = int(review_count[0].text.strip('Ratings & ').replace(',',''))
            reviews_count = int(review_count[1].text.strip('Reviews').replace(',',''))
            logging.info("ratings: {}, reviews_count: {}".format(ratings, reviews_count))

            # get the count of stars recived to each product
            sub_ratings_count = product_page.find_all('div', class_ = '_1uJVNT')
            _5_star = sub_ratings_count[0].text.replace(',','')
            _4_star = sub_ratings_count[1].text.replace(',','')
            _3_star = sub_ratings_count[2].text.replace(',','')
            _2_star = sub_ratings_count[3].text.replace(',','')
            _1_star = sub_ratings_count[4].text.replace(',','')
            logging.info("_5_star: {}, _4_star: {}, _3_star: {}, _2_star: {}, _1_star: {}".format(_5_star, _4_star, _3_star, _2_star, _1_star))

#----------------- %%%% INSERT ALL DETAILS SCRAPED TO CSV FILES %%%%---------------------------------------------------------------------------------------------------------------------
            csv_converter.Price(product_id, price, actual_price)
            csv_converter.Reviews(product_id, pd_reviews)
            csv_converter.Ratings(product_id,ratings,ratings_count,_5_star,_4_star,_3_star,_2_star,_1_star)
        
        except:
            # if tag is not being able to be read the ratings or Ratings DO NOT EXSIST
            logging.critical(" no rating for: {}: {}".format(product_id, url)) 
            return

    except Exception as e:
        # if tag is not being able to be read
        logging.critical("{} AT {}: {}".format(e, product_id, url))

#product_details_insert(product_id= 'ACCDQZAUKTMY5VT7', url = 'https://www.flipkart.com/lezzie-m19-tws-bluetooth-5-1-wireless-earbuds-2000-mah-power-bank-gaming-headset/p/itm387b4e25f00ad?pid=ACCGSZGM5BRT5AHR&lid=LSTACCGSZGM5BRT5AHRNY2HJB&marketplace=FLIPKART&q=headphone&store=0pm%2Ffcn&srno=s_8_318&otracker=search&otracker1=search&fm=organic&iid=e735d3b0-1aad-46f6-8f93-0a6695ea0be1.ACCGSZGM5BRT5AHR.SEARCH&ppt=None&ppn=None&ssid=ovmkyr3nv40000001696617840274&qH=b052e360817fdeec' )