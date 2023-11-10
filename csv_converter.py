"""
All functions in this are used to insert all data into their respective CSV file
"""

import pandas as pd
import datetime
import logging
import helper
import os 

logging.basicConfig(level=logging.DEBUG,filename='logs\product_page.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

#------------ %%%% Inserting Product price into price.csv %%%%----------------------------------------------------------------------------------------
def Price(product_id, curr_price, actual_price):
    logging.info("Inserting into Price.csv")
    Prices = {"product_id":[product_id], "price":[curr_price], "actual_price":[actual_price], "created_at":[datetime.datetime.now()] }
    price = pd.DataFrame(Prices)

    price_path = os.path.join(os.getcwd(),'products\product_details\Price.csv')
    price.to_csv(price_path,
                  mode='a', index=False, header=False )
    logging.info("Inserted into Price.csv")

# ------------- %%%%Inserting Product reviews into reviews.csv %%%%-----------------------------------------------------------------------------------
def Reviews(product_id,review):
    logging.info("Inserting into Reviews.csv")
    for i in range(len(review)):
        Review = {'product_id':[product_id],'reviews':[review[i]], 'created_at':[datetime.datetime.now()] }
        reviews = pd.DataFrame(Review)

        review_path = os.path.join(os.getcwd(),'products\product_details\Reviews.csv')
        reviews.to_csv(review_path,
                    mode='a',header=False,index=False)
    
    logging.info("Inserted into Reviews.csv")

#----------- %%%% Inserting Product ratings into ratings.csv & Product stars into stars.csv %%%%----------------------------------------------------- 
def Ratings(product_id, rating, rating_counts,_5_star, _4_star, _3_star, _2_star, _1_star):
    try:
        # getting the index value to insert it as rating_id which is also foreign key in Stars Table
        index_value = helper.index_()
        logging.info(index_value)
    except:
        logging.error("None Value Error Handling")
        index_value = 0
    
#------------- %%%% Inserting Product ratings into ratings.csv %%%%--------------------------------------------------------------   
    Rating = {'rating_id':[index_value],'product_id': [product_id], 'ratings':[rating], 'rating_count':[rating_counts]}
    ratings = pd.DataFrame(Rating)
    
    logging.info("Inserting values into Ratings.csv")

    ratings_path = os.path.join(os.getcwd(),'products\product_details\Ratings.csv')
    ratings.to_csv(ratings_path,
                mode='a',index=False, header=False)

    logging.info("Inserted into Ratings.csv")

#---------- %%%% Inserting Product stars into stars.csv %%%%-----------------------------------------------------------------------------------------------------------------------------
    Star = {'rating_id':[index_value], 'star_id':[index_value],
            'star_5':[_5_star],
            'star_4':[_4_star],
            'star_3':[_3_star],
            'star_2':[_2_star],
            'star_1':[_1_star]
            }
    
    logging.info("Inserting values into Stars.csv")
    stars = pd.DataFrame(Star)

    stars_path = os.path.join(os.getcwd(),'products\product_details\Stars.csv')
    stars.to_csv(stars_path,
                 mode='a',index=False,header=False)
    
    logging.info("Inserted into Stars.csv")

#---------------------%%%% Inserting Product Ranking into Rankings.csv %%%%------------------------------------------------------------------------------------------------------------- 
def Rankings(product_id,rank):

    Ranking = {"product_id": [product_id], "rank": [rank], "date":[datetime.datetime.now().strftime("%x")]}

    logging.info("Inserting values into Rankings.csv")
    ranking_path = os.path.join(os.getcwd(),'products\Rankings.csv')

    rankings = pd.DataFrame(Ranking)
    rankings.to_csv(ranking_path, mode='a', index=False, header=False)


Rankings('fsafsa',43049)