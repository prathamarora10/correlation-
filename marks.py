import numpy as np
import csv
import plotly.express as px

def plotFigure():
    with open('/Users/prathamarora/Downloads/Python_Projects/correlation/marks_in_percentage vs days_present.csv', newline = '') as f:
        file_data = csv.DictReader(f)
        figure = px.scatter(file_data, x='Marks In Percentage', y='Days Present')
        figure.show()

def getDataSource(data_path):
    marks = []
    days = []

    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))
    
    return{'x' : marks, 'y' : days}

def findCorrelation(dataSource):
    data_correlation = np.corrcoef(dataSource['x'], dataSource['y'])
    print('Correlation between :- Marks In Percenatge & Days Present', data_correlation[0, 1])

def setup():
    data_path = '/Users/prathamarora/Downloads/Python_Projects/correlation/marks_in_percentage vs days_present.csv'
    
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure()

setup()