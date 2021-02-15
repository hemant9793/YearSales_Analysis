import pandas as pd
import os

#reading all files from directory
files = [file for file in os.listdir("E:\deepak singh\pandas projects\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data")]

all_months_data = pd.DataFrame()

for file in files:
    df= pd.read_csv("E:\deepak singh\pandas projects\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\\"+file)

    all_months_data =  pd.concat([all_months_data,df])

#creating a single file of all data merged
all_months_data.to_csv("E:\deepak singh\pandas projects\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\All_months_data.csv",index=False,)

