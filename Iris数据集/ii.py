import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('iris.csv')
le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])
# df.to_excel('iris.xlsx')
a=pd.get_dummies(df['Species'])
temp={True:1,False:0}
print(type(a.astype(int)))

