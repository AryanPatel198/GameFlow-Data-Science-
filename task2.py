# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:52:38 2025

@author: Aaryan
"""
import pandas as pd  # For data manipulation
import numpy as np   # For numerical operations

df = pd.read_csv("vgsales.csv") 

print(df.head())  # Displays the first 5 rows
print(df.info())  # Provides basic information about the dataset
print(df.describe())  # Summary statistics of numerical columns


print("duplicated value:")

print(df.duplicated().sum())  # Count duplicate rows

'''Remove duplicates:'''
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

Check for missing values
print("Missing values before filling:")
print(df.isnull().sum())

Fill missing 'Year' values with the median year
df['Year'].fillna(int(df['Year'].median(), inplace=True))

Fill missing 'Publisher' values with 'Unknown'
df['Publisher'].fillna('Unknown', inplace=True)

Verify if missing values are handled
print("\nMissing values after filling:")
print(df.isnull().sum())

Save the cleaned dataset (optional)
df.to_csv("vgsales_new.csv", index=False)


# Compute central tendency measures: Mean, Median, and Mode

def compute_central_tendency(df):
 central_tendency = {
      'Mean': df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].mean(),  # Compute mean sales
        'Median': df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].median(),  # Compute median sales
       'Mode': df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].mode().iloc[0]  # Compute mode sales
   }
    print("Central Tendency Computed Successfully!\n")  # Print confirmation message
   return central_tendency""


def compute_mean(df):

    mean_values = np.mean('NA_Sales')
    mean_values = np.mean('NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales')  

   print("Mean Sales Values:\n", mean_values, "\n") 
   return mean_values

def compute_median(df):
    median_values = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].median()  # Compute median
    print("Median Computed Successfully!\n")  # Print confirmation message
    return median_values

def compute_mode(df):
    mode_values = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].mode().iloc[0]  # Compute mode
    print("Mode Computed Successfully!\n")  # Print confirmation message
    return mode_values

data_odd = [12, 15, 14, 10, 18]
median_odd = np.median(data_odd)
print(f"Median (Odd Count): {median_odd}")


#mean
df = pd.read_csv("vgsales.csv") 
mean_value = df['NA_Sales'].mean()
print(f"Mean of Na_Sales: {mean_value}")


df = pd.read_csv("vgsales.csv") 
mean_values = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].mean()
print("Mean Sales Values:\n", mean_values, "\n") 

#medain 

median_values = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].median()
print("Median Sales Values:\n", median_values, "\n")

#Mode

mode_values = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].mode()
print("Mode Sales Values:\n", mode_values, "\n")


#RANGE

columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
range_values = df[columns].max() - df[columns].min()

print("Range of Sales:\n", range_values, "\n")

