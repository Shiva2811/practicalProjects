#Setp 1 : Importing essential libraries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#================================================================================================================

#Step 2 : Load the dataset

df = pd.read_csv('Projects/Project 1: Global Superstore Dataset/Global_Superstore.csv')
# print(df.head())

#================================================================================================================

#Step 3: Data cleaning and preprocessing 
#Checking Missing values in dataset
print(df.isnull().sum())

#Ensuring that columns like order date and ship date are in datetime format
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Ship Date']=pd.to_datetime(df['Ship Date'])

#Remove duplicate (if any)
df.drop_duplicates(inplace=True)
#================================================================================================================

#Step 4: Descriptive Analysis
#Basic statistics for numerical column
df.describe()

#Check unique values of catagorical columns like Region, Category, Sub-Category, Segment, etc
df[['Region', 'Category', 'Sub-Category']].value_counts()

#================================================================================================================

#Step 5: Visulize overall sales and Profit Trends
#Monthly and Yearly sales trends
df['Order Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Order Month')['Sales'].sum()
monthly_sales.plot(title='Monthly Sales Trend')
plt.show()

#Sales and Profit per year
df['Order Year'] = df['Order Date'].dt.year
annual_sales = df.groupby('Order Year')[['Sales', 'Profit']].sum()
annual_sales.plot(kind='bar', title='Yearly Sales and Profit')
plt.show()

#================================================================================================================
#Analysis by category and sub-category
#Top product category
category_sales = df.groupby('Category')['Sales'].sum()
category_sales.plot(kind='pie',autopct='%1.1f%%',title='Sales By Category')
plt.show()
#Sub-category performance
sub_category_sales = df.groupby('Sub-Category')[['Sales','Profit']].sum()
sub_category_sales.plot(kind='bar', title='Sales by Sub-Category')
plt.show()

#================================================================================================================
#Geographic Analysis
#Sales by region : Identify which regions have highest sales
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='bar', title='Sales By Region')
plt.show()
#Sales by state
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
state_sales.plot(kind='bar', title='Sales by State')
plt.show()
#Sales by country 
country_sales = df.groupby('Country')['Sales'].sum().sort_values(ascending=False).head(10)
country_sales.plot(kind='bar', title='Sales by Country')
plt.show()

#================================================================================================================
#Step 8: Analyze sales and profit by Customer Segment
segment_sales = df.groupby('Segment')[['Sales','Profit']].sum()
segment_sales.plot(kind='bar', title='sales and profit by Customer Segment')
plt.show()

#================================================================================================================
#Step 9: Discount and Profit Analysis
#Check if higher discounts correlate with lower profit margins
sns.scatterplot(x='Discount', y='Profit', data=df)
plt.title('Discount vs Profit')
plt.show()

#================================================================================================================
#Plot the discount distribution to see common discounting practices
df['Discount'].plot(kind='hist', title='Discount Distribution')
plt.show()

#================================================================================================================
#Step 10: Shipping Mode and Priority Analysis
#Determine which shipping modes are most popular and their associated costs
shipping_costs = df.groupby('Ship Mode')['Shipping Cost'].mean()
shipping_costs.plot(kind='bar', title='Average Shipping Cost by Ship Mode')
plt.show()

#Look into the distribution of order priorities
order_priority_counts = df['Order Priority'].value_counts()
order_priority_counts.plot(kind='bar', title='Order Priority Distribution')
plt.show()