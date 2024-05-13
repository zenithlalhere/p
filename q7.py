import pandas as pd

df = pd.read_csv('/titanic.csv')
# print(df.to_string())

# Passengers with age < 30
print("Total passengers with age<30: ",len(df.loc[df['Age']<30]))

# Total fare paid by first class passengers
print('Total fare paid by first class passenger is: ',df.loc[df['Pclass']==1]['Fare'].sum())

# Survivors of each class
print('Passengers Survived:')
print(df.groupby('Pclass')['Survived'].sum())

# Gender wise descriptive statistics
print(df.groupby('Sex').describe().to_string())
