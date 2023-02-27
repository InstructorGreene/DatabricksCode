# Databricks notebook source
import pandas as pd


# COMMAND ----------

df = pd.DataFrame({
    'a' : [1,2,3],
    'b' : [4,5,6],
    'c' : [7,8,9],
}, index = [1,2,3])


df2 = pd.DataFrame(
    [[1,2,3],[4,5,6],[7,8,9]],
    index=[1,2,3],
    columns = ['a', 'b', 'c'])

print(df)
print("break") 
print(df2)

# COMMAND ----------

print(df)

print('break')
print(df.T)

# COMMAND ----------

tipsData = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

print(tipsData.describe())

print(tipsData.isnull().sum())




# COMMAND ----------

tipsData.groupby(['day']).count()

# COMMAND ----------

tipsData.groupby(['day']).sum()

# COMMAND ----------

totalTips = tipsData.groupby(['day']).sum()['tip']
totalBill = tipsData.groupby(['day']).sum()['total_bill']

tipDayPercentage = (100 * totalTips / totalBill)

tipDayPercentage = tipDayPercentage.to_frame('tip(%)').reset_index()

print(tipDayPercentage)


# COMMAND ----------


