import logging
import sql_functions
import search
import product_page
import time 
import insertion

def scrape_flipkart():

    print("Starting.....")

    logging.basicConfig(level=logging.DEBUG,filename='logs\product.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

    category = sql_functions.read_category()

    logging.info(category[0][1])

    for i in range(len(category)):
        logging.info("category id: {}".format(category[i]))
        #print(category[i][0],  category[i][1])
        
        search.check_category_page(category[i][0], category_name= category[i][1])
        logging.info("Completed search for category {}".format(category[i][1]))

        logging.info("Read all product id's for category {}....".format(category[i][1]))
        all_product_ids = sql_functions.read_product_id(category[i][0])
        logging.info('Completed....')
        
        logging.info('Starting Product Details...')
        for j in range(len(all_product_ids)):
            url = sql_functions.read_product_url(product_id= all_product_ids[j], category_id= category[i][0])
            
            product_page.product_details_insert(product_id= all_product_ids[j], url= url[0])

            logging.info('Sleep 1 sec')
            time.sleep(1)

    logging.info('Process Completed')
    print("Stoping....")

    logging.info("Starting Insertion....")

    insertion.insertion_Price_table()
    insertion.insertion_Ratings_table()
    insertion.insertion_Stars_table()
    insertion.insertion_Reviews_table()

    logging.info("Completed")

#scrape_flipkart()