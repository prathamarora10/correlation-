import numpy as np
import csv
import plotly.express as px

def plotFigure():
    with open('/Users/prathamarora/Downloads/Python_Projects/correlation/cups_of_coffee vs hours_of_sleep.csv', newline = '') as f:
        file_data = csv.DictReader(f)
        figure = px.scatter(file_data, x='Coffee in ml', y='sleep in hours')
        figure.show()

def getDataSource(data_path):
    coffee = []
    sleep = []

    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    
    return{'x' : coffee, 'y' : sleep}

def findCorrelation(dataSource):
    data_correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Correlation between :- Coffee In Ml & Hours Of Sleep', data_correlation[0, 1])

def setup():
    data_path = '/Users/prathamarora/Downloads/Python_Projects/correlation/cups_of_coffee vs hours_of_sleep.csv'
    
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure()

setup()