import plotly.graph_objects as go
import statistics
import plotly.figure_factory as ff
import random
import csv
import pandas as pd

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print("populationMean : ", population_mean)
print("std_dev : ", std_dev)
dataset = []
for i in range(0,100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_dev1 = statistics.stdev(dataset)
print("SampleMean : ", mean)
print("std_dev1 : ", std_dev1)
fig = ff.create_distplot([data],["reading_time"], show_hist = False)
fig.add_trace(go.Scatter(x = [population_mean,population_mean], y =[0,0.2], mode="lines", name = "mean"))
fig.show()