# -*- coding: utf-8 -*-
"""Chess_ apriori.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VKExnslHxeXId61HEHtoPCt88JN-dl_V

# **Chess Apriori-**

Group Members:
1. Mohammd Nurul Abrar (2018-1-60-0139)
2.Md Maruf (2018-1-60-140)
"""

from google.colab import drive
drive.mount("/content/gdrive")

pip install apyori

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori
from apyori import apriori
import time

chessdata= pd.read_csv("/content/gdrive/MyDrive/Colab Notebooks/477project/Chess.csv", header = None) 
chessdata

#manually add the column name which should be convert from category to numeric
Cat = []

for column in Cat:
    col_name = column + '_cat'
    df[col_name] = df[column].astype('category').cat.codes
    df=df.drop([column], axis=1)

chessdata.info()

chessdata.isnull().sum()

rowlength = len(chessdata)
no_features = len(chessdata.values[0])

chessrecords = []
for i in range(0, rowlength):
    chessrecords.append([int(chessdata.values[i,j]) for j in range(0, no_features)if int(chessdata.values[i,j]) != 0])
    #removing 0

cthreshold = 1
chess_time = []
cthreshold_value = []


for i in range(0,3):
  start = time.time()
  rules = apriori(chessrecords,min_support=cthreshold)
  output = list(rules)
  end = time.time()
  chess_time.append(end-start)
  cthreshold_value.append(cthreshold)
  cthreshold = cthreshold - 0.1

from matplotlib import pyplot as plt

plt.plot( cthreshold_value ,chess_time, label='chess dataset')
plt.xlabel("Threshold")
plt.ylabel("Time (s)")
plt.savefig("Chess_apriori.jpg")

"""Chess Dataset Analysis"""

!pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

data=pd.read_csv("/content/gdrive/MyDrive/Colab Notebooks/477project/Chess.csv")

import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])

!pip install pandas-profiling

import numpy as np
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
pro=pandas_profiling.ProfileReport(data)

pro

pro.to_file("chessanalysis.html")