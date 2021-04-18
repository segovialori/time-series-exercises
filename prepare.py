import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import acquire

############## zach store prepare ################
def prep_sales_data():
    '''
    This function will use the store_data dataframe from the acquire.py module function
    "get_store_data" and prepare it to be explored.  This function will:
    - grab get_store_data df from acquire
    - drop columns we wont be using
    - change sale_date to date/time format
    - create month and day of the week columns
    - set time/date as index
    - create a sale_total column
    '''
    df = acquire.get_store_data(cached=True)
    #drop the other upc columns we wont be using
    df.drop(columns= ['item_upc12', 'item_upc14'], inplace=True)
    #converts sale_date from object to date/time format
    df.sale_date = pd.to_datetime(df.sale_date)
    #set the date to the index
    df = df.set_index('sale_date').sort_index()
    #remove time signature
    df.index = df.index.tz_localize(None)
    #add new features
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

# function to plot the histograms for store data.

def store_histplots(df):
    sale_amount=df['sale_amount'].dropna()
    sns.distplot(sale_amount, color = 'green')         
    plt.show()
    
    item_price=df['item_price'].dropna()
    sns.distplot(item_price, color = 'blue')         
    plt.show()   




######## Germany Prepare ##############

