#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
dataset = pd.read_csv("/home/kavya/internship/sales_dataset.csv")


# In[25]:


dataset.shape


# In[26]:


dataset.head()


# In[15]:


import pymysql

user = 'root'
passw = 'password'
host =  'localhost'
port = 3306
database = 'sales'

connection = pymysql.connect(host=host,port=port,user=user,passwd=passw,db=database,charset='utf8')
cursor = connection.cursor()


# In[42]:


import csv
with open('/home/kavya/internship/sales_dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        cursor.execute('INSERT INTO retail_sales(retailer_country,order_method_type,retailer_type,product_line,product_type,product,year,quarter,revenue,quantity,gross_margin)' 'VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s)',row)


# In[46]:


connection.commit()
cursor.close()
print('Imported!')


# In[ ]:




