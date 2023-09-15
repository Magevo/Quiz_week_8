import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

def grab():
    connection = sqlite3.connect(r".\climate.db")
    cursor = connection.cursor()

    cursor.execute("SELECT  Year, CO2, Temperature FROM ClimateData")
    data = cursor.fetchall()

    for info in data:
        years.append(info[0])
        co2.append(info[1])
        temp.append(info[2])

    connection.close()


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
    plt.savefig("co2_temp_1.png") 

if __name__ == "__main__":
    grab()
    plot()