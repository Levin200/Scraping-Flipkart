from bs4 import BeautifulSoup
import requests
import logging
import sql_functions
import time 

logging.basicConfig(level=logging.DEBUG,filename='logs\product.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


#------------ %%%% Testing Response %%%%-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def response_page():
    headers = {'Origin': 'http://flipkart.com','Referer': 'http://flipkart.com/','User-Agent': 'Chrome/54.0.2840.90'}
    base_url = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity&page={}"
    logging.critical("Delete")
    for i in range(4):
        response = requests.get(url= base_url.format('headphone', 8), headers= headers)
        #print(response, response.status_code)
        if response.status_code == 200:
            break
        logging.warning(response)
        time.sleep(i*2)
    else:
        print("error in page")
        logging.error("Response status code: {}".format(response.status_code))
        quit()

    logging.info("Response status code: {}".format(response.status_code))

    #html_content = response.content

#------------------------ %%%% INSERTION FROM SEARCH PAGE %%%%------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function to insert the values from Product Category page 
# Retrive product ID, name, URL, features
# product-> parsed page when called from search.py
def insert(product, product_id, index, category=1):

    logging.info("Starting Inserion For {}".format(product_id))

    #product = BeautifulSoup(html_content, 'html.parser')

    a_s1Q9rs_all_values = product.find_all('a', class_ = 's1Q9rs')

    # get Product Name
    product_names = a_s1Q9rs_all_values[index]
    #print(product_names.text)
    product_name = product_names.text.replace(','," ")
    logging.info("product_name: {}".format(product_name))

    # get Product Feature
    div__3Djpdu_all_values = product.find_all('div',class_ = '_3Djpdu')
    feature = div__3Djpdu_all_values[2]
    #print(feature.text)
    feature_text = feature.text.replace(',','&')
    logging.info("features: {}".format(feature_text))

    # get Product URL
    product_links = product_names.get('href')
    product_base_url = "https://www.flipkart.com"+ product_links #adding to base url
    URL = product_base_url
    logging.info("product_base_url: {}".format(URL))

    # Insertion into MySQL Products Table
    sql_functions.insert_product(product_id= product_id,product_name = product_name, URL= URL,
                                feature_text= feature_text, category_id= category)

    # get Image URL
    div_CXW8mj_all_values = product.find_all('div', class_ = 'CXW8mj')
    img_source = div_CXW8mj_all_values[2].find('img', class_ = '_396cs4')
    logging.info("Image SRC: {}".format(img_source['src']))

    # Insertion into MySQL Image_url Table
    sql_functions.insert_image(product_id= product_id, img_url= img_source['src'] )