import pandas as pd
import matplotlib.pyplot as plt

#reading single file of all data
sales_data = pd.read_csv("E:\deepak singh\All_months_data.csv",parse_dates=["Order Date"])

#droping na values
sales_data.dropna(how='all',inplace=True)
#removing or values from Order Date
sales_data = sales_data[sales_data["Order Date"].str[0:2] != 'Or']


#question 2- what time should we display the ads so that customer is most likely to buy our products
#convert order date into datetime object so that they can be accessed easily using datetime properties
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
sales_data['Hour'] = sales_data["Order Date"].dt.hour
sales_data["Minutes"] = sales_data["Order Date"].dt.minute

hours = [hour for hour,df in sales_data.groupby(by='Hour')]

plt.plot(hours,sales_data.groupby(by='Hour').count())
plt.xticks(hours)
plt.xlabel("Hours")
plt.ylabel("Number of orders")
plt.grid()
plt.show()
#as the line chart shows there are two peaks so we should be show ads at that peak time
