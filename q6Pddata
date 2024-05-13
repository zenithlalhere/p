import pandas as pd

data = {
    'Name':['Shah','Vats','Vats','Kumar','Vats','Kumar','Shah','Shah','Kumar','Vats'],
    'Gender':['Male','Male','Female','Female','Female','Male','Male','Female','Female','Male'],
    'MonthlyIncome': [114000,65000,43150,69500,155000,103000,55000,112400,81030,71900]
}

df=pd.DataFrame(data)
print(df)

# Family wise income
print('Family wise income')
df2 = df.groupby('Name')['MonthlyIncome'].sum()
print(df2)

# Member with highest salary
print("Member with highest salary")
print(df.loc[df['MonthlyIncome'].idxmax()])
print()
#Members with salary >60000
print('Members with salary >60000')
print(df.loc[df['MonthlyIncome']>60000])
print()
# Average monthly salary of female members
print("Average salary of females ")
avg_salary_female = (df.loc[df['Gender']=='Female']['MonthlyIncome']).mean()
print(avg_salary_female)
