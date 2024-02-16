import csv 
import sql_functions
import logging
import os 

logging.basicConfig(level=logging.DEBUG,filename='logs\product.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def insertion_Price_table():
    val = []
    #open the csv file 
    price_path = os.path.join(os.getcwd(),'products\product_details\Price.csv')
    with open(price_path, mode='r') as csv_file: 
        #read csv using reader class 
        csv_reader = csv.reader(csv_file) 

        #skip header 
        header = next(csv_reader) 
        header = next(csv_reader)

        #Read csv row wise 
        for row in csv_reader: 
            val.append(tuple(row))

    successful = sql_functions.insert_Price(val)

    if successful:
        with open(price_path, mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["product_id","price","actual_price","created_at"])

def insertion_Ratings_table():
    val = []
    #open the csv file 
    ratings_path = os.path.join(os.getcwd(),'products\product_details\Ratings.csv')
    with open(ratings_path, mode='r') as csv_file: 
        #read csv using reader class 
        csv_reader = csv.reader(csv_file) 

        #skip header 
        header = next(csv_reader) 
        header = next(csv_reader)

        #Read csv row wise 
        for row in csv_reader: 
            val.append(tuple(row))

    #print(val)
    successful = sql_functions.insert_Ratings(val)

    if successful:
        with open(ratings_path, mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["rating_id","product_id","ratings","rating_count"])

def insertion_Stars_table():
    val = []
    #open the csv file 
    #file = 'test.csv'
    stars_path = os.path.join(os.getcwd(),'products\product_details\Stars.csv')
    with open(stars_path, mode='r') as csv_file: 
        #read csv using reader class 
        csv_reader = csv.reader(csv_file) 

        #skip header 
        header = next(csv_reader) 
        header = next(csv_reader)

        #Read csv row wise 
        for row in csv_reader: 
            val.append(tuple(row))

    #print(val)
    successful = sql_functions.insert_Stars(val)

    if successful:
        with open(stars_path, mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["rating_id","star_id","star_5" ,"star_4" ,"star_3" ,"star_2" ,"star_1"])

def insertion_Reviews_table():
    val = []
    #open the csv file 
    #file = 'test.csv'
    review_path = os.path.join(os.getcwd(),'products\product_details\Reviews.csv')
    with open(review_path, mode='r',encoding='utf-8') as csv_file: 
        #read csv using reader class 
        csv_reader = csv.reader(csv_file) 

        #skip header 
        header = next(csv_reader) 
        header = next(csv_reader)

        #Read csv row wise 
        for row in csv_reader: 
            val.append(tuple(row))

    #print(val)
    successful = sql_functions.insert_Review(val)

    if successful:
        with open(review_path, mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["product_id","reviews","created_at"])

def insertion_Ranking_table():
    val = []
    #open the csv file 
    #file = 'test.csv'
    ranking_path = os.path.join(os.getcwd(),'products\Rankings.csv')
    with open(ranking_path, mode='r') as csv_file: 
        #read csv using reader class 
        csv_reader = csv.reader(csv_file) 

        #skip header 
        header = next(csv_reader) 
        header = next(csv_reader)

        #Read csv row wise 
        for row in csv_reader: 
            val.append(tuple(row))

    #print(val)
    successful = sql_functions.insert_Ranking(val)

    if successful:
        with open(ranking_path, mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["product_id","rank","date"])



#insertion_Ranking_table()
#insertion_Stars_table()
#insertion_Reviews_table()