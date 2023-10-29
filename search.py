"""
check_category_page checks if the product ID is already exsisting in the Products Table in MySQL
If it does not exsists then the insertion operation takes place
"""

import logging
from bs4 import BeautifulSoup
import product
import requests
import time
import sql_functions

# checks if the product ID is already exsisting or not
# 
def check_category_page(category_id, category_name):
    # Uses SQL Query to Retrieve all the products in that category
    all_product_ids = sql_functions.read_product_id(category_id= category_id)

    # goes through multiple pages for a particular category
    for page in range(1):
        headers = {'Origin': 'http://flipkart.com','Referer': 'http://flipkart.com/','User-Agent': 'Chrome/54.0.2840.90'}
        base_url = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity&page={}"

        # Checking for Response 200
        for i in range(4):
            response = requests.get(url= base_url.format(category_name, page), headers= headers)
            #print(response, response.status_code)
            if response.status_code == 200:
                break
            logging.warning(response)
            time.sleep(i*2)
        else:
            # if even after 4 trys there is no response return error in page
            #print("error in page")
            logging.error("Response status code: {}".format(response.status_code))
            continue

        logging.info("Response status code: {}".format(response.status_code))

        html_content = response.content

        # Parse the Page
        products = BeautifulSoup(html_content, 'html.parser')

        # Each class_ -> a_s1Q9rshas information about each product
        # Retriving all values about each product in search page
        a_s1Q9rs_all_values = products.find_all('a', class_ = 's1Q9rs')
        for i in range(len(a_s1Q9rs_all_values)):
            link = a_s1Q9rs_all_values[i].get('href')
            l = link.split('?pid=',1)
            pid = l[1][:16] # Gets the product ID 
            #print(pid)
            if pid not in all_product_ids: # If the product is not in the Products table
                product.insert(products,pid,i,category_id)

#check_category_page(category_id= 1)