import pandas as pd
import matplotlib.pyplot as plt

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


#best month for sale and how much was earned in that month

#adding sales column to ans our question
sales_data['Quantity Ordered'] = pd.to_numeric(sales_data['Quantity Ordered'])
sales_data['Price Each'] = pd.to_numeric(sales_data['Price Each'])
sales_data["Sales"] = sales_data['Quantity Ordered'] * sales_data['Price Each']


#getting the total of each month
monthly_sale = sales_data.groupby(by='Months')

list=[]
month =[]
for key,df in monthly_sale:
    month.append(key)
    list.append(df["Sales"].sum())
a=list.index(max(list))

#plotting bar chart

plt.bar(month,list)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(month)
plt.show()
#as our bar chart shows that best month for sales was December.