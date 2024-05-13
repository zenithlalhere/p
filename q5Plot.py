# Plotting scatter w regression, density distribution, pairplot, heatmap, mean mode, correlation coeff
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sn

df = pd.read_csv('/iris.csv')
print(df)
#a

df.plot.bar()
plt.show()

#b
df.plot.scatter(x='petal.width',y='sepal.width' )
plt.show()

#c
df2 = sn.load_dataset('iris')
sn.distplot(a=df2.petal_length, color='green',
             hist_kws={"edgecolor": 'black'})
plt.title('Density plot ')
plt.show()



#(d)
df4 = sn.load_dataset('iris')
sn.pairplot(df4, hue ='petal_length')
plt.show()


#(f)
print(df.describe())
print(df[df.columns[1:-2]].mode(axis =1))


#e

sn.heatmap(data = df[df.columns[1:4]])
plt.show()
#g

print(df[df.columns[1:4]].corr())
