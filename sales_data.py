import pandas as pd
import numpy as np

#reading single file of all data
sales_data = pd.read_csv("E:\deepak singh\All_months_data.csv",parse_dates=["Order Date"])

#droping na values
sales_data.dropna(how='all',inplace=True)

#cleaning the data

#finding na value
new_df = sales_data[sales_data.isna().any(axis=1)]


#find Or and delete it
temp_df = sales_data[sales_data["Order Date"].str[0:2] == 'Or']#finding rows which cause or error
sales_data = sales_data[sales_data["Order Date"].str[0:2] != 'Or']

#adding additional columns for helping with data analysis and changing its type to int
sales_data["Months"] = sales_data["Order Date"].str[0:2]
sales_data["Months"] = sales_data["Months"].astype('int')
print(sales_data.head())

#best month for sale and how much was earned in that month
