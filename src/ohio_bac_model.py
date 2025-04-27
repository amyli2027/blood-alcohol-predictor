import pandas as pd
ohio_bac_dataset = pd.read_csv('data/processed/ohio_bac_dataset_processed.csv')

from sklearn.linear_model import LinearRegression
X = ohio_bac_dataset[['Beers', 'Weight']]
Y = ohio_bac_dataset['BAC']
model = LinearRegression()
model.fit(X, Y)

import joblib
joblib.dump(model, 'ohio_bac_model.pkl')
