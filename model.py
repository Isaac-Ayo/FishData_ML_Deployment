import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np

df = pd.read_csv(r"C:\Users\isaac\Desktop\Heroku_app\Fish.csv")

df['Species'] = LabelEncoder().fit_transform(df['Species'])
X = df[['Species', 'Length1', 'Length2', 'Length3', 'Height', 'Width']]
X = X.astype('float32')
y = df['Weight']

regr = linear_model.LinearRegression()
regr.fit(X.values, y.values)

pickle.dump(regr, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[0, 23.2, 25.4, 30.0, 11.5200, 4.0200]]))