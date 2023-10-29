import streamlit as st
import sql_functions
import scrape_main
import time
import testing_category
import pandas as pd
import matplotlib.pyplot as plt
import helper


st.set_page_config(layout='wide')

st.title("Flipkart Web Scrapper")

tab1, tab2, tab3 = st.tabs(["Dashboard", "Categories", "Search"])


with tab1:
   st.title("Dashboard")
   pressed = st.button("SCRAPE FLIPKART", type="primary", use_container_width=True)
   if pressed:
    with st.spinner('Wait for it...'):
        scrape_main.scrape_flipkart()
        st.success('Done!')
    

   col1, col2, col3 = st.columns(3)

   with col1:
    st.subheader("Total Products")
    st.title(sql_functions.read_count_products())

    with col2:
        st.subheader("Total Categories")
        st.title(sql_functions.read_count_categories())

    with col3:
        st.subheader("Total Products")
        st.title(sql_functions.read_count_products())


#------------ %%%%CATEGORY%%%% -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

with tab2:
   st.title("Categories")
   st.warning('Updates might take 24 hours to display', icon= "ℹ️")
   

   with st.form('Insertion'):
    new_category = st.text_input('Insert New Category', placeholder="Category Name")
    submit = st.form_submit_button('Insert')

   if submit:
        if new_category:
            with st.spinner('Wait for it...'):
                time.sleep(5)
                test_results = testing_category.test_category(new_category)
                if test_results:
                    st.info("Updating Table")
                    sql_functions.insert_category_table(val= [new_category])
                    st.success("Done")

                else:
                    st.error("Not Possible or the category already exsists")
        
        else:
           st.error("Please enter a Value", icon="⚠️")

   col2_1 , col2_2 = st.columns(2)
   with col2_1: 
    category_df = pd.DataFrame(sql_functions.read_category())
    category_df.columns = ["Category id", "Category name"]
    st.table(category_df) #width=500, height=490

   with col2_2:
    
    results_from_table = sql_functions.read_count_of_products_for_each_category()
    results_in_list = helper.convert_to_list_format(results_from_table)
        
    labels = results_in_list[0]
    counts = results_in_list[1]

    count_of_category1, ax1 = plt.subplots()
    ax1.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    st.pyplot(count_of_category1) 

    category_counts = pd.DataFrame(results_from_table)
    category_counts.columns = ["Category Name", "Count"]
    st.table(category_counts) 



        
with tab3:
   st.title("Search")
   
 

