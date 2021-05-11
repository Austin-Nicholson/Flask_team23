

import csv
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

import pmdarima as pm
from pmdarima.model_selection import train_test_split
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima.arima import auto_arima
from pmdarima.pipeline import Pipeline
from pmdarima.preprocessing import BoxCoxEndogTransformer

#Read the csv file into the python dataframe###################################################################3
data = pd.read_csv("very_smol.csv", encoding= 'unicode_escape')
#df = pd.DataFrame(my_dict)
df = pd.DataFrame(data, columns=["SKU", "Quantity", "InvoiceDate", "UnitPrice"])

del df['SKU']
del df['UnitPrice']

df['Quantity'].replace('', np.nan, inplace=True)
df.dropna(subset=['Quantity'], inplace=True)

#df[df < 0] = 0
# Get names of indexes for which column Age has value 30
indexNames = df[ df['Quantity'] <= 0 ].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)


#df.sort_index(inplace= True)
df.sort_values(['InvoiceDate', 'Quantity'], ascending=[True, True], inplace=True)


#get into tdi format###########################################################################################
tdi = pd.DatetimeIndex(df.InvoiceDate)
df.set_index(tdi, inplace=True)
df.drop(columns='InvoiceDate', inplace=True)
df.index.name = 'datetimeindex'

df.sort_index(inplace=True)


#train with csv data############################################################################################

train, test = df[:36], df[36:]

test2 = df

pipeline = Pipeline([
    ("fourier", ppc.FourierFeaturizer(m=12, k=4)),
    ("model", arima.AutoARIMA(stepwise=True, trace=1, error_action="ignore",
                              seasonal=False,  # because we use Fourier
                              suppress_warnings=True))
])


#pipeline = Pipeline([
#    ("boxcox", BoxCoxEndogTransformer()),
#    ("model", pm.AutoARIMA(seasonal=False, suppress_warnings=True))
#])

pipeline.fit(test2)
stuff = pipeline.predict(5)
print(stuff)
plt.plot(test2,label="Training")

preds, conf_int = pipe.predict(n_periods=test.shape[0], return_conf_int=True)
print(preds)





