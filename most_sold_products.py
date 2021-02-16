import pandas as pd
import matplotlib.pyplot as plt


#reading single file of all data
sales_data = pd.read_csv("E:\deepak singh\All_months_data.csv",parse_dates=["Order Date"])

#droping na values
sales_data.dropna(how='all',inplace=True)
#removing or values from Order Date
sales_data = sales_data[sales_data["Order Date"].str[0:2] != 'Or']

#which product sold the most
products = sales_data.groupby(by='Product')
quantity_ordered = products.sum()['Quantity Ordered']
product = [product for product,df in products]

plt.bar(product,quantity_ordered)
plt.xticks(product,rotation = 'vertical',size=8)
plt.xlabel("Products")
plt.ylabel("Number of orders")
plt.show()
#as the bar chart shows , aaa batteries were the most sold products
