import csv 
import sql_functions
import logging

logging.basicConfig(level=logging.DEBUG,filename='logs\product.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def insertion_Price_table():
    val = []
    #open the csv file 
    with open(r'C:\Users\Levin Dsouza\Desktop\webscraping\Flipkart\products\product_details\Price.csv', mode='r') as csv_file: 
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
        with open(r'C:\Users\Levin Dsouza\Desktop\webscraping\Flipkart\products\product_details\Price.csv', mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["product_id","price","actual_price","created_at"])

def insertion_Ratings_table():
    val = []
    #open the csv file 
    #file = 'test.csv'
    file = r'C:\Users\Levin Dsouza\Desktop\webscraping\Flipkart\products\product_details\Ratings.csv'
    with open(file, mode='r') as csv_file: 
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
        with open(file, mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["rating_id","product_id","ratings","rating_count"])

def insertion_Stars_table():
    val = []
    #open the csv file 
    #file = 'test.csv'
    file = r'C:\Users\Levin Dsouza\Desktop\webscraping\Flipkart\products\product_details\Stars.csv'
    with open(file, mode='r') as csv_file: 
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
        with open(file, mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["rating_id","star_id","star_5" ,"star_4" ,"star_3" ,"star_2" ,"star_1"])

def insertion_Reviews_table():
    val = []
    #open the csv file 
    #file = 'test.csv'
    file = r'C:\Users\Levin Dsouza\Desktop\webscraping\Flipkart\products\product_details\Reviews.csv'
    with open(file, mode='r') as csv_file: 
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
        with open(file, mode='w') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["product_id","reviews","created_at"])

