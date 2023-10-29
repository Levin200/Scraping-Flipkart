import pandas as pd

def index_():
    index_df = pd.read_csv(r'C:\Users\Levin Dsouza\Desktop\webscraping\Flipkart\index.csv')
    index = index_df.tail()
    #print(index)
    index_value = int(index['index_id'].iloc[-1]) + 1
    Index = {'index_id': [index_value]}
    _index = pd.DataFrame(Index)
    _index.to_csv(r'C:\Users\Levin Dsouza\Desktop\webscraping\Flipkart\index.csv', mode= 'w', index= False)

    return index_value

def convert_to_list_format(table):

    result_lists = []

    for i in range(len(table[0])):
        result_lists.append([])

    for i in range(len(table)):
        for j in range(len(table[i])):
            result_lists[j].append(table[i][j])

    return result_lists

#import sql_functions
#myresult = sql_functions.read_count_of_products_for_each_category()
#print(convert_to_list_format(myresult))
