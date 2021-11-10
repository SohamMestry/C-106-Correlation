import numpy as np
import csv
import plotly.express as pe

def getDataSource(file):
    row1 = []
    row2 = []
    with open(file) as filedata:
        df = csv.DictReader(filedata)
        for row in df:
            row1.append(float(row["Marks In Percentage"]))
            row2.append(float(row["Days Present"]))
        #fig3 = pe.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        #fig3.show()
    return {"x" : row1, "y" : row2}

def getDataCorrel(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print("The correlation between MARKS and DAYS PRESENT is ", correlation[0,1])

def main():
    dataSource  =  "Student Marks vs Days Present.csv"
    datafile = getDataSource(dataSource)
    getDataCorrel(datafile)