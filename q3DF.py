#dataframe using random
import pandas as pd
import numpy as np
import random

df = pd.DataFrame(np.random.randn(50,3), columns=['One','Two','Three'])
# Index to be replaced

idxRep = random.sample(range(0,50),15)

for i in range(0,15):
  col = random.sample(range(0,3),1)
  df.iloc[idxRep[i],col[0]]=np.nan

print(df)

# Verifying null values

nullDataFrame = df.isnull()

print(nullDataFrame)

print("Counting Null values")

count = 0
for i in range(0,50):
  for j in range(0,3):
    if nullDataFrame.iloc[i,j]==True:
      count+=1

print(count)

# Dropping cols with null>5

colsToBeDropped =[]
for i in range(0,3):
  nullCount = 0
  for j in range(0,50):
    if nullDataFrame.iloc[j,i]==True:
      nullCount+=1
  if nullCount>5:
    colsToBeDropped.append(df.columns[i])

df2 = df.drop(colsToBeDropped, axis=1)
print(colsToBeDropped)
print(df2)

# Row with maximum sum

sumSeries = df.sum(axis = 1)
print("Row wise Sum")
print(sumSeries)

print("Row index with max sum is: ",sumSeries.idxmax())

# Sortin dataframe on the basis of first column
df3 = df.sort_values('One')
print("Sorting according to column one")
print(df3)

# Deleting all duplicates from first column
df4 = df.drop_duplicates(subset="One", keep=False)
print("Original DF")
print(df)
print("new Df")
print(df4)

# Find Correlarion between first and second column
print("Correlation")
print(df.iloc[:,0:2].corr())

# Discretize the second column and create 5 bins.
print(pd.cut(df['Two'], bins=5))
