import matplotlib.pyplot as plt
import pandas as pd
import csv

years = []
co2 = []
temp = []

def grab(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            years.append(int(row[0]))
            co2.append(int(row[1]))
            temp.append(float(row[2]))

def plot():
    plt.subplot(2, 1, 1)
    plt.plot(years, co2, 'b--') 
    plt.title("Climate Data") 
    plt.ylabel("[CO2]") 
    plt.xlabel("Year (decade)") 

    plt.subplot(2, 1, 2)
    plt.plot(years, temp, 'r*-') 
    plt.ylabel("Temp (C)") 
    plt.xlabel("Year (decade)") 
    plt.show() 
    plt.savefig("co2_temp_2.png") 

if __name__ == "__main__":
    grab('climate.csv')
    plot()
