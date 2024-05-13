#Pandas series sorting on index and seperately
import pandas as pd

myVar = pd.Series([10,20,34,12,2], index=[5,4,3,2,1])

myVar2 = myVar.sort_index()
myVar3 = myVar.sort_values()
print(myVar)
print(myVar2)
print(myVar3)

# Ques 2 b

myVar = pd.Series([1,2,2,3,4,4,4], index=['a','b','c','d','e','f','g'])
print(myVar)

min_rank = myVar.rank(method='first')
print(min_rank)

max_rank = myVar.rank(method='max')
print(max_rank)

# Ques 2. c
myVar = pd.Series([11,23,21,10,87,9,355,76,44,21,20])
print(myVar)

max_idx =  myVar.idxmax()
min_idx = myVar.idxmin()
print("Max value is at : "+ str(max_idx))
print("Min value is at : "+ str(min_idx))
