#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:49:39 2024

@author: hlajoane_the_geologist
"""
import pandas as pd
file = pd.read_csv("data_02/iris.csv")
#absolute path: gives you the full location of the file in the folder

#Relative path:Based on the location you are working on
#e.g data_02/iris.csv

#gettting data online for a specific URL
# df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# url = "http://raw.githubusercontent.com/kode2go/nitecs/main/lecture_01/iris.csv"
# file = pd.read_csv(url)

# colum_names= ['sepal_length', 'sepal_width', 'petal_length', 'petal_witdth', 'class']
    
# file=pd.read_csv("data_02/Geospatial Data.txt", sep=";")

# file=pd.read_csv("data_02/residentdoctors.xlsx")

# df = pd.read_csv("data_02/country_data_index.csv")

# df = pd.read_csv("chat_files/Accelerometer_data.csv",names = ["date_time", "x", "y", "Z"])

#Transforms

# df=pd.read.csv("data_02/country_data_index.csv", index_col=0)

df = pd.read_excel("data_02/residentdoctors.xlsx")
print(df.info())

df["LOWER_AGE"]= df["AGEDIST"].str.extract('(\d+)-')
df["UPPER_AGE"]= df["AGEDIST"].str.extract('-(\d+)')
df["LOWER_AGE"]= df["LOWER_AGE"].astype(int)
print(df.info())

#Regular expressions are important in working with string related data that has to be converted to interger
#Now we working dates
df = pd.read_csv("data_02/time_series_data.csv",index_col=0)

print(df.info())#here we check if date is an object or an integer
df['Date'] = pd.to_datetime(df['Date'])
# df['Date'] = pd.to_datetime(df['Date'], format-"%d-%m-%Y")
print(df.info())

#creating a new coloumn
df['Year'] = df['Date'].dt.year

#Nam

df = pd.read_csv("data_02/patient_data_dates.csv")

df = pd.read_csv("data_02/patient_data_dates.csv", index_col=0)

df ['Date'] = pd.to_datetime(df['Date'])

df.drop(index=26, inplace=True)

print(df.info())

#what to do with empty values (Nan)
avg_cal = df["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace =True)#This code replaces the nan with a value

#Best Coding Practices when cleaning and processing data

df.dropna(inplace = True)# all the data (row 22) was removed (we have to fix the index cells)
df =df.reset_index(drop = True)

#Fixing biased data or typo e.g row 7 column 1

df.loc[7, 'Duration'] = 45 #we are assigning the value 45 instead of 450 as the ) might be a typo

#How can you use your data for your project??

#Applying data Tranformations (Append and Merge related files)

############IRIS DATA


df = pd.read_csv("data_02/iris.csv")
col_names = df.columns.tolist()
df["sepal_length_sq"] = df["sepal_length"]**2
# df["sepal_length_sq"] = df["sepal_lenght"].apply(lambda x: x**2)
print(df.columns)


grouped = df.groupby("class")
mean_square_values = grouped ['sepal_length_sq'].mean()
print(mean_square_values)

#remove iris from class column
df["class"]= df["class"].str.replace("Iris -", "")
print(df)

df = df[df['sepal_length'] > 5]

df = df[df["class"] == "virginica"]

df.to_csv("output/pulsar.csv")

#combine

# df1 = pd.read_csv("data_02/person_split1.csv")
# df2 = pd.read_csv("data_02/person_split2.csv")

# df = pd.concat([df1,df2])
# df  = pd.concat([df1,df2], ignore_index = True)

#########Inner join

# df1 = pd.read_csv("data_02/person_education.csv")
# df2 = pd.read_csv("data_02/person_work.csv")

# df_merger_inner = pd.merge(df1,df2,on = "id")

###loading data or saving it into a csv file
# df.to_csv("pulsar.csv")





















