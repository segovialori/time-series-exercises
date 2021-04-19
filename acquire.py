import requests
import pandas as pd
import os
from io import StringIO
#######ACQUIRE#############


def get_items(cached=False):
    if cached == False:
        items_list = []
        url = "https://python.zach.lol/api/v1/items"
        response = requests.get(url)
        data = response.json()
        n = data['payload']['max_page']
        
        for i in range(1, n+1):
            new_url = url + '?page=' + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_items = data['payload']['items']
            items_list += page_items
            
        items = pd.DataFrame(items_list)
        items.to_csv('items.csv')
            
    else:
        items = pd.read_csv('items.csv', index_col=0)
    
    return items


def get_sales(cached=False):
    if cached == False:
        sales_list = []
        url = "https://python.zach.lol/api/v1/sales"
        response = requests.get(url)
        data = response.json()
        n = data['payload']['max_page']
        
        for i in range(1, n+1):
            new_url = url + '?page=' + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_sales = data['payload']['sales']
            sales_list += page_sales
            
        sales = pd.DataFrame(sales_list)
        sales.to_csv('sales.csv')
            
    else:
        sales = pd.read_csv('sales.csv', index_col=0)
    
    return sales


def get_stores(cached=False):
    if cached == False:
        stores_list = []
        url = "https://python.zach.lol/api/v1/stores"
        response = requests.get(url)
        data = response.json()
        n = data['payload']['max_page']
        
        for i in range(1, n+1):
            new_url = url + '?page=' + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_stores = data['payload']['stores']
            stores_list += page_stores
            
        stores = pd.DataFrame(stores_list)
        stores.to_csv('stores.csv')
            
    else:
        stores = pd.read_csv('stores.csv', index_col=0)
    
    return stores

def get_store_data(cached=False):
    '''
    This function will take in the dataframes created in get_sales, get_items, and get_stores
    and combine them into one mega dataframe.
    '''
    if cached == False:
        items = get_items(cached=False)
        stores = get_stores(cached=False)
        sales = get_sales(cached=False)

        df = pd.merge(sales, stores, left_on='store', right_on='store_id').drop(columns={'store'})
        df = pd.merge(df, items, left_on='item', right_on='item_id').drop(columns={'item'})
        df.to_csv('store_data.csv')
        df = pd.read_csv('store_data.csv')
    else:
        df = pd.read_csv('store_data.csv', index_col=0)
    return df



#Germany data
def get_germany():
    """
    Returns a dataframe containing Open Power Systems data for Germany.
    """
    response = requests.get("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")
    csv = StringIO(response.text)
    
    return pd.read_csv(csv)