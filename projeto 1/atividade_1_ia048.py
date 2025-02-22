# -*- coding: utf-8 -*-
"""Atividade_1_IA048.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S1cj5g54UTGC6ht0ICrWEa6hr7XDAlvx
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from itertools import chain
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from scipy.interpolate import interp1d
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

df = pd.read_csv('/opt/air traffic.csv')
df

# @title Default title text
df.info()

df.describe()

duplicated_rows = df[df.duplicated()]

if not duplicated_rows.empty:
    print("There are duplicated rows.")
    print(duplicated_rows)
else:
    print("There are no duplicated rows.")

df['date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY = 1))

#lockdown start date
lockdown_date = pd.Timestamp('2020-01-01')


#plot with matplotlib
plt.figure(figsize =(10,6))
plt.plot(df['date'],df['Dom_LF'], label ='Dometic Flight Number' )
plt.axvline(lockdown_date, color = 'r', label = f'covid-19 lockdown {lockdown_date}')
plt.title('Domestic Flight Number')
plt.xlabel('Date')
plt.ylabel('Domestic Flight')
plt.grid(True)
plt.legend()
plt.show()

df['date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY = 1))

#lockdown start date
jan2003_to_ago2008 = pd.Timestamp('2008-08-30')
sep2008_to_dec2019 = pd.Timestamp('2019-12-30')
jan2020_to_sep2023 = pd.Timestamp('2023-09-30')


#plot with matplotlib
plt.figure(figsize =(10,6))
plt.plot(df['date'],df['LF'], label ='Flight Number' )
plt.axvline(jan2003_to_ago2008, color = 'r', label = f'jan/2003 to ago/2008 {jan2003_to_ago2008}')
plt.axvline(sep2008_to_dec2019, color = 'r', label = f'sep/2008 to dec/2019 {sep2008_to_dec2019}')
plt.axvline(jan2020_to_sep2023, color = 'r', label = f'jan/2020 to sep/2023 {jan2020_to_sep2023}')
plt.title('Flight Number')
plt.xlabel('Date')
plt.ylabel(' Flight')
plt.grid(True)
plt.legend()
plt.show()

df['time'] = (df.index.values + 0.5) / 12

#Train for K values where K = 0,1,2,...,24 for each value
# Type 1 - Data of 2003 to 2019
df_normal_times = df[df['date'] < lockdown_date]
x_normal_times = list(df_normal_times['time'])
y_normal_times = list(df_normal_times['LF'])

matriz_de_erros = []
menor_erro = 10000
k_otimo = 0
coefficients_otimos = []
linear_otimo = 0

aux = 0
aux_otimo = 0


for i in range(0,len(y_normal_times)):
  matriz_de_erros.append(RMSE_linear)
  if i > 24:
    for k in range(1,25):
      # Divide data into traning and test data
      train_size = k
      test_size = len(x_normal_times) - k

      # Data in train
      x_train = x_normal_times[0:train_size]
      y_train = y_normal_times[0:train_size]

      # Data test
      x_test = x_normal_times[train_size:]
      y_test = y_normal_times[train_size:]

      LF_test = df_normal_times.iloc[train_size:].copy()
      LF_train = df_normal_times.iloc[0:train_size].copy()

      # Fit model data with training data
      model_1 = LinearRegression().fit(np.array(x_train).reshape(-1,1), y_train)
      coefficients = [model_1.coef_[0], model_1.intercept_]
      linear = model_1.predict(np.array(x_train).reshape(-1,1))

      # Calculate performance metrics for Linear Model
      linear_test = model_1.predict(np.array(x_test).reshape(-1, 1))
      RMSE_linear = (mean_squared_error(y_test, linear_test ,squared=False))

      if RMSE_linear < menor_erro:
        menor_erro = RMSE_linear
        k_otimo = k
        coefficients_otimos.insert(0, coefficients[0])
        coefficients_otimos.insert(1, coefficients[1])
        linear_otimo = linear
        aux_otimo = i
  else:
    for k in range(1, i):
      # Divide data into traning and test data
      train_size = k
      test_size = len(x_normal_times) - k

      # Data in train
      x_train = x_normal_times[0:train_size]
      y_train = y_normal_times[0:train_size]

      # Data test
      x_test = x_normal_times[train_size:]
      y_test = y_normal_times[train_size:]

      LF_test = df_normal_times.iloc[train_size:].copy()
      LF_train = df_normal_times.iloc[0:train_size].copy()

      # Fit model data with training data
      model_1 = LinearRegression().fit(np.array(x_train).reshape(-1,1), y_train)
      coefficients = [model_1.coef_[0], model_1.intercept_]
      linear = model_1.predict(np.array(x_train).reshape(-1,1))

      # Calculate performance metrics for Linear Model
      linear_test = model_1.predict(np.array(x_test).reshape(-1, 1))
      RMSE_linear = (mean_squared_error(y_test, linear_test ,squared=False))


      if RMSE_linear < menor_erro:
        menor_erro = RMSE_linear
        k_otimo = k
        coefficients_otimos.insert(0, coefficients[0])
        coefficients_otimos.insert(1, coefficients[1])
        linear_otimo = linear
        aux_otimo = i

#Train for K values where K = 0,1,2,...,24 for each value
# Type 1 - Data of 2003 to 2019
df_normal_times = df[df['date'] < lockdown_date]
x_normal_times = list(df_normal_times['time'])
y_normal_times = list(df_normal_times['LF'])

matriz_de_erros = []
menor_erro = 10000
k_otimo = 0
coefficients_otimos = []
linear_otimo = 0

aux = 0
aux_otimo = 0


for i in range(0,len(y_normal_times)):
  matriz_de_erros.append(RMSE_linear)
  if i > 24:
    for k in range(1,25):
      # Divide data into traning and test data
      train_size = k
      test_size = len(x_normal_times) - k

      # Data in train
      x_train = x_normal_times[0:train_size]
      y_train = y_normal_times[0:train_size]

      # Data test
      x_test = x_normal_times[train_size:]
      y_test = y_normal_times[train_size:]

      LF_test = df_normal_times.iloc[train_size:].copy()
      LF_train = df_normal_times.iloc[0:train_size].copy()

      # Fit model data with training data
      model_1 = LinearRegression().fit(np.array(x_train).reshape(-1,1), y_train)
      coefficients = [model_1.coef_[0], model_1.intercept_]
      linear = model_1.predict(np.array(x_train).reshape(-1,1))

      # Calculate performance metrics for Linear Model
      linear_test = model_1.predict(np.array(x_test).reshape(-1, 1))
      RMSE_linear = (mean_squared_error(y_test, linear_test ,squared=False))

      if RMSE_linear < menor_erro:
        menor_erro = RMSE_linear
        k_otimo = k
        coefficients_otimos.insert(0, coefficients[0])
        coefficients_otimos.insert(1, coefficients[1])
        linear_otimo = linear
        aux_otimo = i
  else:
    for k in range(1, i):
      # Divide data into traning and test data
      train_size = k
      test_size = len(x_normal_times) - k

      # Data in train
      x_train = x_normal_times[0:train_size]
      y_train = y_normal_times[0:train_size]

      # Data test
      x_test = x_normal_times[train_size:]
      y_test = y_normal_times[train_size:]

      LF_test = df_normal_times.iloc[train_size:].copy()
      LF_train = df_normal_times.iloc[0:train_size].copy()

      # Fit model data with training data
      model_1 = LinearRegression().fit(np.array(x_train).reshape(-1,1), y_train)
      coefficients = [model_1.coef_[0], model_1.intercept_]
      linear = model_1.predict(np.array(x_train).reshape(-1,1))

      # Calculate performance metrics for Linear Model
      linear_test = model_1.predict(np.array(x_test).reshape(-1, 1))
      RMSE_linear = (mean_squared_error(y_test, linear_test ,squared=False))


      if RMSE_linear < menor_erro:
        menor_erro = RMSE_linear
        k_otimo = k
        coefficients_otimos.insert(0, coefficients[0])
        coefficients_otimos.insert(1, coefficients[1])
        linear_otimo = linear
        aux_otimo = i

print("The linear model is F(t) = {:.3f}*t + {:.3f} ".format(coefficients_otimos[0],coefficients_otimos[1]))
def f(x_normal_times): return np.float64(coefficients_otimos[0])*np.float64(x_normal_times) + np.float64(coefficients_otimos[1])

# plot data with matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(x_normal_times, y_normal_times, s=20, c="blue", alpha=0.5, label="Flight Data")
plt.plot(x_normal_times, f(x_normal_times), color="red", linewidth=2.5, label="Modelo Preditivo")
plt.plot(x_normal_times, matriz_de_erros,color="green", linewidth=2.5, label="Evolução do erro")
plt.xlabel('Time')
plt.ylabel('Flight')
plt.title('Linear Model Fit')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(x_train, y_train, s=20, alpha=0.5, edgecolors="red")
plt.xlabel('Date')
plt.ylabel('Flights')
plt.title('Scatter Plot of Flights 2020-2023')
plt.grid(True)
plt.show()

df_pandemic_times = df[df['date'] > lockdown_date]
x_pandemic_times = list(df_pandemic_times['time'])
y_pandemic_times = list(df_pandemic_times['LF'])

matriz_de_erros = []
menor_erro = 10000
k_otimo = 0
coefficients_otimos = []
linear_otimo = 0

aux = 0
aux_otimo = 0


for i in range(0,len(y_pandemic_times)):
  matriz_de_erros.append(RMSE_linear)
  if i > 24:
    for k in range(1,25):
      # Divide data into traning and test data
      train_size = k
      validate_size = len(x_pandemic_times) - k

      # Data in train
      x_train = x_pandemic_times[0:train_size]
      y_train = y_pandemic_times[0:train_size]

      # Data validate
      x_validate = x_pandemic_times[train_size:]
      y_validate = y_pandemic_times[train_size:]

      LF_validate = df_normal_times.iloc[train_size:].copy()
      LF_train = df_normal_times.iloc[0:train_size].copy()

      # Fit model data with training data
      model_1 = LinearRegression().fit(np.array(x_train).reshape(-1,1), y_train)
      coefficients = [model_1.coef_[0], model_1.intercept_]
      linear = model_1.predict(np.array(x_train).reshape(-1,1))

      # Calculate performance metrics for Linear Model
      linear_test = model_1.predict(np.array(x_validate).reshape(-1, 1))
      RMSE_linear = (mean_squared_error(y_validate, linear_test ,squared=False))

      if RMSE_linear < menor_erro:
        menor_erro = RMSE_linear
        k_otimo = k
        coefficients_otimos.insert(0, coefficients[0])
        coefficients_otimos.insert(1, coefficients[1])
        linear_otimo = linear
        aux_otimo = i
  else:
    for k in range(1, i):
      # Divide data into traning and test data
      train_size = k
      validate_size = len(x_normal_times) - k

      # Data in train
      x_train = x_pandemic_times[0:train_size]
      y_train = y_pandemic_times[0:train_size]

      # Data test
      x_test = x_pandemic_times[train_size:]
      y_test = y_pandemic_times[train_size:]

      LF_test = df_pandemic_times.iloc[train_size:].copy()
      LF_train = df_pandemic_times.iloc[0:train_size].copy()

      # Fit model data with training data
      model_1 = LinearRegression().fit(np.array(x_train).reshape(-1,1), y_train)
      coefficients = [model_1.coef_[0], model_1.intercept_]
      linear = model_1.predict(np.array(x_train).reshape(-1,1))

      # Calculate performance metrics for Linear Model
      linear_test = model_1.predict(np.array(x_test).reshape(-1, 1))
      RMSE_linear = (mean_squared_error(y_test, linear_test ,squared=False))


      if RMSE_linear < menor_erro:
        menor_erro = RMSE_linear
        k_otimo = k
        coefficients_otimos.insert(0, coefficients[0])
        coefficients_otimos.insert(1, coefficients[1])
        linear_otimo = linear
        aux_otimo = i

print("The linear model is F(t) = {:.3f}*t + {:.3f} ".format(coefficients_otimos[0],coefficients_otimos[1]))
def f(x_pandemic_times): return np.float64(coefficients_otimos[0])*np.float64(x_pandemic_times) + np.float64(coefficients_otimos[1])



# plot data with matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(x_pandemic_times, y_pandemic_times, s=20, c="blue", alpha=0.5, label="Flight Data")
plt.plot(x_pandemic_times, f(x_pandemic_times), color="red", linewidth=2.5, label="Modelo Preditivo")
plt.plot(x_pandemic_times, matriz_de_erros,color="green", linewidth=2.5, label="Evolução do erro")
plt.xlabel('Time')
plt.ylabel('Flight')
plt.title('Linear Model Fit')
plt.legend()
plt.grid(True)
plt.show()

print("The linear model is F(t) = {:.3f}*t + {:.3f} ".format(coefficients_otimos[0],coefficients_otimos[1]))
def f(x_test): return np.float64(coefficients_otimos[0])*np.float64(x_test) + np.float64(coefficients_otimos[1])

# Calculate performance metrics for Linear Model
RMSE_linear = (mean_squared_error(y_test, f(x_test) ,squared=False))
MAPE_linear = mean_absolute_percentage_error(y_test, f(x_test))
print("RMSE of linear model:{:.3f}".format(RMSE_linear))
print("MAPE of linear model:{:.3f} %".format(MAPE_linear))

# plot data with matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(x_test, y_test, s=20, c="blue", alpha=0.5, label="Flight Data")
plt.plot(x_test, f(x_test), color="red", linewidth=2.5, label="Modelo Preditivo")
# plt.plot(x_test, matriz_de_erros,color="green", linewidth=2.5, label="Evolução do erro")
plt.xlabel('Time')
plt.ylabel('Flight')
plt.title('Linear Model Fit')
plt.legend()
plt.grid(True)
plt.show()

min_date = pd.Timestamp('2022-01-01')
df_min_date = df[df["date"] >= min_date]
x = list(df_min_date['time'])
y = list(df_min_date['LF'])

print(len(x))
def f(x): return np.float64(coefficients_otimos[0])*np.float64(x) + np.float64(coefficients_otimos[1])

# Calculate performance metrics for Linear Model
RMSE_linear = (mean_squared_error(y, f(x) ,squared=False))
MAPE_linear = mean_absolute_percentage_error(y, f(x))
print("RMSE of linear model:{:.3f}".format(RMSE_linear))
print("MAPE of linear model:{:.3f} %".format(MAPE_linear))

# plot data with matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=20, c="blue", alpha=0.5, label="Flight Data")
plt.plot(x, f(x), color="red", linewidth=2.5, label="Modelo Preditivo")
# plt.plot(x_test, matriz_de_erros,color="green", linewidth=2.5, label="Evolução do erro")
plt.xlabel('Time')
plt.ylabel('Flight')
plt.title('Linear Model Fit')
plt.legend()
plt.grid(True)
plt.show()

"""Letra C)"""

date_of_test_init = pd.Timestamp('2020-01-01')
date_of_test_end = pd.Timestamp('2022-01-01')

# Divide data into traning, validate data and test data
df_train_data = df[df['date'] < date_of_test_init]
x_train_data = list(df_train_data['time'])
y_train_data = list(df_train_data['LF'])
LF_train = df_train_data.iloc[::].copy()

df_validatate_data = df[df['date'].between(date_of_test_init, date_of_test_end)]
x_validatate_data = list(df_validatate_data['time'])
y_validatate_data = list(df_validatate_data['LF'])
LF_validate = df_validatate_data.iloc[::].copy()

df_test_data = df[df['date'] > date_of_test_end]
x_test_data = list(df_test_data['time'])
y_test_data = list(df_test_data['LF'])
LF_test = df_test_data.iloc[::].copy()


model = LinearRegression().fit(np.array(x_train_data).reshape(-1,1), y_train_data)
coefficients = [model.coef_[0], model.intercept_]


#Train for K values where K = 0,1,2,...,24 for each value
matriz_de_erros = []
menor_erro = 10000
k_otimo = 0
coefficients_otimos = []
linear_otimo = 0

aux = 0
aux_otimo = 0


for i in range(0,len(y_train_data)):
  matriz_de_erros.append(RMSE_linear)
  if i > 24:
    for k in range(1,25):
      # Divide data into traning and test data
      train_size = k
      test_size = len(x_train_data) - k

      # Data in train
      x_train = x_train_data[0:train_size]
      y_train = y_train_data[0:train_size]

      # Data test
      x_validate = x_validatate_data[train_size:]
      y_validate = y_validatate_data[train_size:]

      LF_test = df_validatate_data.iloc[train_size:].copy()
      LF_validate = df_validatate_data.iloc[0:train_size].copy()

      # Fit model data with training data
      model = LinearRegression().fit(np.array(x_train).reshape(-1,1), y_train)
      coefficients = [model.coef_[0], model.intercept_]
      linear = model_1.predict(np.array(x_train).reshape(-1,1))

      def f(x_validate): return coefficients[0]*np.float64(x_validate) + coefficients[1]
      # Calculate performance metrics for Linear Model
      RMSE_linear = (mean_squared_error(y_validate, f(x_validate) ,squared=False))

      if RMSE_linear < menor_erro:
        menor_erro = RMSE_linear
        k_otimo = k
        coefficients_otimos.insert(0, coefficients[0])
        coefficients_otimos.insert(1, coefficients[1])
        linear_otimo = linear
        aux_otimo = i
  else:
    for k in range(1, i):
     # Divide data into traning and test data
      train_size = k
      test_size = len(x_train_data) - k

      # Data in train
      x_train = x_train_data[0:train_size]
      y_train = y_train_data[0:train_size]

      # Data test
      x_validate = x_validatate_data[train_size:]
      y_validate = y_validatate_data[train_size:]

      LF_test = df_validatate_data.iloc[train_size:].copy()
      LF_validate = df_validatate_data.iloc[0:train_size].copy()

      # Fit model data with training data
      model = LinearRegression().fit(np.array(x_train).reshape(-1,1), y_train)
      coefficients = [model.coef_[0], model.intercept_]
      linear = model.predict(np.array(x_train).reshape(-1,1))

      # Calculate performance metrics for Linear Model
      def f(x_validate): return coefficients[0]*np.float64(x_validate) + coefficients[1]
      RMSE_linear = (mean_squared_error(y_validate, f(x_validate),squared=False))

      if RMSE_linear < menor_erro:
        menor_erro = RMSE_linear
        k_otimo = k
        coefficients_otimos.insert(0, coefficients[0])
        coefficients_otimos.insert(1, coefficients[1])
        linear_otimo = linear
        aux_otimo = i

print(coefficients_otimos[0], coefficients_otimos[1])

print("The linear model is F(t) = {:.3f}*t + {:.3f} ".format(coefficients_otimos[0],coefficients_otimos[1]))
def f(x_normal_times): return np.float64(coefficients_otimos[0])*np.float64(x_normal_times) + np.float64(coefficients_otimos[1])

# plot data with matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(x_normal_times, y_normal_times, s=20, c="blue", alpha=0.5, label="Flight Data")
plt.plot(x_normal_times, f(x_normal_times), color="red", linewidth=2.5, label="Modelo Preditivo")
plt.plot(x_normal_times, matriz_de_erros,color="green", linewidth=2.5, label="Evolução do erro")
plt.xlabel('Time')
plt.ylabel('Flight')
plt.title('Linear Model Fit')
plt.legend()
plt.grid(True)
plt.show()

def f(x_test_data): return np.float64(coefficients_otimos[0])*np.float64(x_test_data) + np.float64(coefficients_otimos[1])
print("The linear model is F(t) = {:.3f}*t + {:.3f} ".format(coefficients_otimos[0],coefficients_otimos[1]))

# Calculate performance metrics for Linear Model
RMSE_linear = (mean_squared_error(y_test_data, f(x_test_data) ,squared=False))
MAPE_linear = mean_absolute_percentage_error(y_test_data, f(x_test_data))
print("RMSE of linear model:{:.3f}".format(RMSE_linear))
print("MAPE of linear model:{:.3f} %".format(MAPE_linear))

# plot data with matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=20, c="blue", alpha=0.5, label="Flight Data")
plt.plot(x, f(x), color="red", linewidth=2.5, label="Modelo Preditivo")
# plt.plot(x_test, matriz_de_erros,color="green", linewidth=2.5, label="Evolução do erro")
plt.xlabel('Time')
plt.ylabel('Flight')
plt.title('Linear Model Fit')
plt.legend()
plt.grid(True)
plt.show()

min_date = pd.Timestamp('2022-01-01')
df_min_date = df[df["date"] >= min_date]
x = list(df_min_date['time'])
y = list(df_min_date['LF'])

print(len(x))
def f(x): return np.float64(coefficients_otimos[0])*np.float64(x) + np.float64(coefficients_otimos[1])

# Calculate performance metrics for Linear Model
RMSE_linear = (mean_squared_error(y, f(x) ,squared=False))
MAPE_linear = mean_absolute_percentage_error(y, f(x))
print("RMSE of linear model:{:.3f}".format(RMSE_linear))
print("MAPE of linear model:{:.3f} %".format(MAPE_linear))

# plot data with matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=20, c="blue", alpha=0.5, label="Flight Data")
plt.plot(x, f(x), color="red", linewidth=2.5, label="Modelo Preditivo")
# plt.plot(x_test, matriz_de_erros,color="green", linewidth=2.5, label="Evolução do erro")
plt.xlabel('Time')
plt.ylabel('Flight')
plt.title('Linear Model Fit')
plt.legend()
plt.grid(True)
plt.show()