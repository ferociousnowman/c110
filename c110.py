import plotly.figure_factory as ff 
import statistics 
import random
import pandas as pd 
import csv

df=pd.read_csv("newdata.csv")
data=df["average"].tolist()
averagemean=statistics.mean(data)
fig=ff.create_distplot([data],["average"],show_hist=False)
fig.show()