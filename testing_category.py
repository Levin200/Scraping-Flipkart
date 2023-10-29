import logging
from bs4 import BeautifulSoup
import product
import requests
import time
import sql_functions

def test_category(new_category):
    category = sql_functions.read_category()

    all_categories = []
    for i in range(len(category)):
            print(category[i][0],  category[i][1])
            all_categories.append(category[i][1].upper())

    if new_category.upper() in all_categories:
        return False
#--------------------------------------------------------------------------------------------------------------------------------------------
# Checking the category page
#--------------------------------------------------------------------------------------------------------------------------------------------
    else:
        print("checking the page")
        headers = {'Origin': 'http://flipkart.com','Referer': 'http://flipkart.com/','User-Agent': 'Chrome/54.0.2840.90'}
        base_url = "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=popularity&page={}"

# making request to the page
        for i in range(4):
            response = requests.get(url= base_url.format(new_category, 1), headers= headers)
            #print(response, response.status_code)
            if response.status_code == 200:
                break
            logging.warning(response)
            time.sleep(i*2)
        else:
            logging.debug("error in page")
            return False
            
            

        #logging.info("Response status code: {}".format(response.status_code))

        html_content = response.content

        products = BeautifulSoup(html_content, 'html.parser')

        a_s1Q9rs_all_values = products.find_all('a', class_ = 's1Q9rs')

        if a_s1Q9rs_all_values:
            #print(a_s1Q9rs_all_values)
            link = a_s1Q9rs_all_values[0].get('href')
            l = link.split('?pid=',1)
            pid = l[1][:16]
            logging.debug(link, pid)

            #a_s1Q9rs_all_values = product.find_all('a', class_ = 's1Q9rs')

            product_names = a_s1Q9rs_all_values[0]
            print(product_names.text)
            product_name = product_names.text.replace(','," ")
            

            div__3Djpdu_all_values = products.find_all('div',class_ = '_3Djpdu')
            feature = div__3Djpdu_all_values[2]
            #print(feature.text)
            feature_text = feature.text.replace(',','&')
            #print(feature_text)
            

            product_links = product_names.get('href')
            product_base_url = "https://www.flipkart.com"+ product_links
            URL = product_base_url
           
            if product_name and URL and feature_text:
                logging.debug("All values are proper")
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Checking the product_page
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                for i in range(4):
                    response = requests.get(url= URL, headers= headers)
                    #print(response, response.status_code)
                    if response.status_code == 200:
                        break
                    logging.warning(response)
                    time.sleep(i*2)
                else:
                    print("error in page")
                    logging.error("Response status code: {}".format(response.status_code))
                    return False

                logging.info("Response status code {}".format(response.status_code))
                html_content = response.content

                product_page = BeautifulSoup(html_content, 'html.parser')
                try: 
                    price = product_page.find('div', '_30jeq3 _16Jk6d') # get the tag <div class='_30jeq3 _16Jk6d'>₹22</div>
                    price = price.text.strip("₹") # gets the price and removes '₹'
                    price = int(price.replace(",","")) # replaces ',' with no spaces
                
                
                    try:
                        actual_price = product_page.find('div', '_3I9_wc') #  get the tag <div class='_3I9_wc'>₹44</div>
                        actual_price = actual_price.text.strip("₹") # gets the actual value and removes '₹'
                        actual_price = int(actual_price.replace(",","")) # replaces ',' with no spaces
                        logging.info("price: {}, actual_price {}".format( str(price), str(actual_price)))

                    except:
                        #logging.warning("{} has no actual price".format(pid)) # if no actual price is found
                        actual_price = price 


                    reviews = product_page.find_all('p', class_ = '_2-N8zT') #  get the tag <p class='_2-N8zT'>reviews...</p>
                    pd_reviews = [] # empty list to add all the reviews
                    for i in range(len(reviews)):
                        pd_reviews.append(reviews[i].text)
                    #logging.info("{}".format(pd_reviews))

                    try:
                        ratings = product_page.find('div', class_ = '_2d4LTz')  #  get the tag <div class='_2d4LTz'>4.4</div>
                        ratings = ratings.text
                    
                        review_count = product_page.find_all('div', class_ = 'row _2afbiS')
                        ratings_count = int(review_count[0].text.strip('Ratings & ').replace(',',''))
                        reviews_count = int(review_count[1].text.strip('Reviews').replace(',',''))
                        logging.info("ratings: {}, reviews_count: {}".format(ratings, reviews_count))

                        sub_ratings_count = product_page.find_all('div', class_ = '_1uJVNT')
                        _5_star = sub_ratings_count[0].text.replace(',','')
                        _4_star = sub_ratings_count[1].text.replace(',','')
                        _3_star = sub_ratings_count[2].text.replace(',','')
                        _2_star = sub_ratings_count[3].text.replace(',','')
                        _1_star = sub_ratings_count[4].text.replace(',','')
                        logging.info("_5_star: {}, _4_star: {}, _3_star: {}, _2_star: {}, _1_star: {}".format(_5_star, _4_star, _3_star, _2_star, _1_star))

                    
                    except:
                        logging.debug(" no rating for: {}".format(URL)) # if tag is not being able to be read
                        

                except:

                    logging.debug("{}".format(URL))

                finally:
                    if price and actual_price and ratings:
                        logging.debug("Possible")
                        return [True, "DONT" ]
                    
                    else:
                        logging.debug("Not possible")
                        return False

            else:
                logging.debug("Not Possible")
                return False

        else:
            logging.debug("Not Possible")
            return False


#test_results = test_category("mouse")

"""if test_results:
    print("insertion")

else:
    print("No insertion")"""