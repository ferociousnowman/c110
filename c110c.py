import plotly.figure_factory as ff 
import statistics 
import random
import pandas as pd 
import csv

df=pd.read_csv("newdata.csv")
data=df["average"].tolist()

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    smean=statistics.mean(dataset)
    sdev=statistics.stdev(dataset)
    print(smean)
    print(sdev)
    return smean

def showfig(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)

setup()



#tempmean=statistics.mean(data)
#tempstd=statistics.stdev(data)
#print(tempmean)
#print(tempstd)

