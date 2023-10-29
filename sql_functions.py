"""
All functions related to SQL are present in this script.
It starts with connection to the Database.
"""

import logging
import mysql.connector

# To connect with MySQL database
def connect_db():
    logging.info("Connecting To Database")

    mydb = mysql.connector.connect(	
        host = "localhost",
        user = "root",
        password = "pass@1234",
        database = "Flipkart"
    )

    return mydb

# ------------------- %%%% INITAL INSERTION %%%%--------------------------------------------------------------------------------------------------------------------------------------------------------------

# insertion from product.py to MySQL Products table
def insert_product(product_id, product_name, URL, feature_text, category_id):
    try:
        mydb = connect_db()

    # Printing the connection object
        logging.info(mydb)
        logging.info("Connection Successfull")

        products_query= """
        INSERT INTO Products (product_id, product_name, URL, feature, category_id)
        values ('{0}','{1}','{2}','{3}',{4});
        """.format(product_id, product_name, URL, feature_text, category_id)
        
        logging.info("Inserting values into Products Table")
        Products_table =  mydb.cursor()
        Products_table.execute(products_query)
        mydb.commit()

        logging.info("Insertion Successful")
 
    except:
        logging.error("Duplicate entry")

    finally:
        mydb.close()

# insertion from product.py to Image_url table
def insert_image(product_id, img_url):

    try:
        mydb = connect_db()

        logging.info(mydb)
        logging.info("Connection Successfull")

        img_url_query= """
    INSERT INTO Image_url (product_id, img_url)
    values ('{0}','{1}');
    """.format(product_id, img_url)
        
        logging.info("Inserting values into Image_url Table")
        Image_url_table =  mydb.cursor()
        Image_url_table.execute(img_url_query)
        mydb.commit()

        logging.info("Insertion Successful")

    except:
        logging.error("Duplicate entry")

    finally:
        mydb.close()

#-------------- %%%% READ %%%%-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  get all product ids
def read_product_id(category_id):
    try:
        mydb = connect_db()

        logging.info(mydb)
        logging.info("Connection Successfull")

        query = """
SELECT product_id FROM Products
WHERE category_id = {}; 
""".format(category_id)
        mycursor = mydb.cursor()

        mycursor.execute(query)
        myresult = mycursor.fetchall()
        product_id = [''.join(i) for i in myresult]

        return product_id

    except:
        logging.error("Check")
        
    finally:
        mydb.close()

# get all from category table
def read_category():
    try:
        mydb = connect_db()

        logging.info(mydb)
        logging.info("Connection Successfull")
        
        query = """ 
SELECT * FROM Category;
"""
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()

        return myresult

    except:
        logging.error("Check")

    finally:
        mydb.close()

# get the product URL from product table
def read_product_url(product_id, category_id):
    try:
        mydb = connect_db()

        logging.info(mydb)
        logging.info("Connection Successfull")
        
        query = """ 
SELECT URL FROM Products
WHERE product_id = '{}' 
AND
category_id = {};
""".format(product_id, category_id)
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchone()

        return myresult

    except:
        logging.error("Check")

    finally:
        mydb.close()

# get count of all the products available
def read_count_products():

    mydb = connect_db()
    Product_table = mydb.cursor()
    products_query = """select count(*) from Products"""
    Product_table.execute(products_query)
    myresult = Product_table.fetchall()
    
    return myresult[0][0]

# get count of all categories present
def read_count_categories():

    mydb = connect_db()

    Product_table = mydb.cursor()

    products_query = """select count(*) from Category"""

    Product_table.execute(products_query)

    myresult = Product_table.fetchall()
    
    return myresult[0][0]

# get count of products from each category
def read_count_of_products_for_each_category():

    mydb = connect_db()

    myCountTable = mydb.cursor()

    count_query = "SELECT Category.category_name, count(Category.category_id) from Products left join Category on Products.category_id = Category.category_id group by (Category.category_name)"
    myCountTable.execute(count_query)

    myresults = myCountTable.fetchall()

    return myresults
#-------------------- %%%% Insertion %%%%------------------------------------------------------------------------------------------------------------------------------------------------------------------
# insertion from csv to MySQL Price table
def insert_Price(val):
    try:
        mydb = connect_db()  

        # Printing the connection object
        logging.info(mydb)
        logging.info("Connection Successfull")

        cursor = mydb.cursor()
        sql = "INSERT INTO Price (product_id,price,actual_price,created_at) VALUES (%s,%s,%s,%s)" 
        cursor.executemany(sql, val) 
        logging.info(f"Records inserted in Price Table: {cursor.rowcount}") 
        mydb.commit() 

        successful = True

    except Exception as e:
        logging.critical("Reviews table not updated")
        logging.critical(e)
        print(e)
        successful = False

    finally:
        mydb.close()
        return successful

# insertion from csv to MySQL Ratings table
def insert_Ratings(val):
    try:
        mydb = connect_db()  

        # Printing the connection object
        logging.info(mydb)
        logging.info("Connection Successfull")

        cursor = mydb.cursor()
        sql = "INSERT INTO Ratings (rating_id,product_id,rating,count_of_people) VALUES (%s,%s,%s,%s)" 
        cursor.executemany(sql, val) 
        logging.info(f"Records inserted in Ratings Table: {cursor.rowcount}") 
        print(cursor.rowcount)
        mydb.commit() 

        successful = True

    except Exception as e:
        logging.critical("Reviews table not updated")
        logging.critical(e)
        print(e)
        successful = False

    finally:
        mydb.close()
        return successful

# insertion from csv to MySQL Stars table        
def insert_Stars(val):
    try:
        mydb = connect_db()  

        # Printing the connection object
        logging.info(mydb)
        logging.info("Connection Successfull")

        cursor = mydb.cursor()
        sql = "INSERT INTO Stars (rating_id,star_id,star_5 ,star_4 ,star_3 ,star_2 ,star_1) VALUES (%s,%s,%s,%s,%s,%s,%s)" 
        cursor.executemany(sql, val) 
        logging.info(f"Records inserted in Stars Table: {cursor.rowcount}") 
        print(cursor.rowcount)
        mydb.commit() 

        successful = True

    except Exception as e:
        logging.critical("Reviews table not updated")
        logging.critical(e)
        print(e)
        successful = False

    finally:
        mydb.close()
        return successful

# insertion from csv to MySQL Review table 
def insert_Review(val):
    try:
        mydb = connect_db()  

        # Printing the connection object
        logging.info(mydb)
        logging.info("Connection Successfull")

        cursor = mydb.cursor()
        sql = "INSERT INTO Review (product_id,review,created_at) VALUES (%s,%s,%s)" 
        cursor.executemany(sql, val) 
        logging.info(f"Records inserted in Reviews Table: {cursor.rowcount}") 
        print(cursor.rowcount)
        mydb.commit() 

        successful = True

    except Exception as e:
        logging.critical("Reviews table not updated")
        logging.critical(e)
        print(e)
        successful = False

    finally:
        mydb.close()
        return successful

# insertion from app.py to MySQL Category table
def insert_category_table(val):
    try:
        mydb = connect_db()  

        # Printing the connection object
        logging.info(mydb)
        logging.info("Connection Successfull")

        cursor = mydb.cursor()
        sql = "INSERT INTO Category (category_name) VALUES (%s)" 
        cursor.execute(sql, val) 
        logging.info(f"Records inserted in Reviews Table: {cursor.rowcount}") 
        print(cursor.rowcount)
        mydb.commit()

    except Exception as e:
        logging.error(e)

    finally:
        mydb.close()


# ------------------------%%%% TESTING %%%%----------------------------------------------------------------------------------------------------------------------

#all_product_id = read_product_id(1)
##print(all_product_id[0])
#category = read_category()
#print(category)

#url = read_product_url(product_id='ACCGSZGM5BRT5AHR', category_id=1)
#print(url[0])
#print(read_count_categories())
#new_category = "mouse"
#insert_category_table(val = [new_category])
#print(read_count_of_products_for_each_category())

