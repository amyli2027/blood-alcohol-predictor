from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import joblib

def test_regression_model(dataset, features, target_column_name):
  X = dataset[features]
  Y = dataset[target_column_name]
  X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
  model = LinearRegression()
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  mse = mean_squared_error(y_test, y_pred)
  r2 = r2_score(y_test, y_pred)
  return mse, r2, model.coef_, model.intercept_

def results(dataset, features, target_column_name):
  mse, r2, coefficients, intercept = test_regression_model(dataset, features, target_column_name)
  print(f"Features: {features}")
  print(f"Target: {target_column_name}")
  print(f"Mean Squared Error: {mse}")
  print(f"R2 score: {r2}")

def build_model(dataset, features, target):
  X = dataset[features]
  Y = dataset[target]
  model = LinearRegression()
  model.fit(X, Y)
  return model

def save_model(model, path):
  joblib.dump(model, path)