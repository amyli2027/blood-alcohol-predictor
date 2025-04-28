from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import os

def test_regression_model(dataset, features, target_column_name):
  X = dataset[features]
  Y = dataset[target_column_name]
  X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
  model = LinearRegression()
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  mse = mean_squared_error(y_test, y_pred)
  r2 = r2_score(y_test, y_pred)
  return mse, r2

def results(dataset, features, target_column_name):
  mse, r2= test_regression_model(dataset, features, target_column_name)
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

def cross_validate_model(dataset, features, target, folds, metric):
  X = dataset[features]
  Y = dataset[target]
  model = LinearRegression()
  scores = cross_val_score(model, X, Y, cv=folds, scoring=metric)

  print("Cross-validated R2 scores:", scores)
  print("Average R2:", scores.mean())

def save_model_summary(model, X, y, output_path):
  # Predict
  features = X.columns
  y_pred = model.predict(X)

  # Calculate metrics
  r2 = r2_score(y, y_pred)
  mse = mean_squared_error(y, y_pred)

  # Get coefficients and intercept
  intercept = model.intercept_
  coefficients = model.coef_

  # Build equation string
  equation_parts = [f"({coef:.6f} x {features[i]})" for i, coef in enumerate(coefficients)]
  equation = " + ".join(equation_parts)
  equation = f"Predicted BAC = {intercept:.6f} + {equation}"

  # Make sure output folder exists
  os.makedirs(os.path.dirname(output_path), exist_ok=True)

  # Write to file
  with open(output_path, 'w') as f:
      f.write("Model Equation:\n")
      f.write(equation + "\n\n")
      f.write(f"R2 Score: {r2:.4f}\n")
      f.write(f"MSE: {mse:.4f}\n")

def plot_model_results(model, dataset, features, target_column_name):
  Y = dataset[target_column_name]
  X = dataset[features]
  y_pred = model.predict(X)
  plt.scatter(Y, y_pred)
  plt.xlabel('Actual BAC')
  plt.ylabel('Predicted BAC')
  plt.title('Actual vs Predicted BAC')
  plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'r--')
  plt.savefig('../output/actual_vs_predicted_plot.png', dpi=300)
  plt.close()

