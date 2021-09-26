import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

dataset = pd.read_csv('medium_data.csv')
dataset = dataset["reading_time"].to_list()

def oneMeanByOne(dataPoints):
    meanList = []
    for i in range(0, dataPoints):
        randomInteger = random.randint(0, len(dataset)-1)
        meanList.append(dataset[randomInteger])
    mean = statistics.mean(meanList)
    return mean

def graph(list):
    meanOfMean = statistics.mean(list)
    figure = ff.create_distplot([list], ["Reading Time"], show_hist = False)
    figure.add_trace(go.Scatter(x = [meanOfMean, meanOfMean], y = [0,10], mode = "lines", name = "Mean"))
    figure.show()

def setup():
    meanOfMeanList = []
    for i in range(0, 100):
        meanSet = oneMeanByOne(30)
        meanOfMeanList.append(meanSet)
    graph(meanOfMeanList)

    sampleMean = statistics.mean(meanOfMeanList)
    sampleStandardDeviation = statistics.stdev(meanOfMeanList)
    populationMean = statistics.mean(dataset)
    populationStandardDeviation = statistics.stdev(dataset)
    print(f"The mean of the sample is {sampleMean}. The standard deviation of the sample is {sampleStandardDeviation}.")
    print(f"The mean of the pouplation is {populationMean}. The standard deviation of the population is {populationStandardDeviation}.")

setup()