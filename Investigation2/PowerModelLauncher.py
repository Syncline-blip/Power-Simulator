# Program name:
#              PowerModelLauncher.py: displays hourly usage and consumption of appliances within the house
#
# Created by:
#            Name - John Aaron Dayao Lumagbas
#            StudentID - 20165510
# 'Finalised version of 'PowerModelLauncher.py - 29.05.2020'

# Neccessary Libraries
import sys
import pandas as pd
from selectionmenu import *
import matplotlib.pyplot as plt
from itertools import count, cycle
from matplotlib.animation import FuncAnimation



# Launch and Select Menu
#
selector = select() #Outputs a selection of Appliances to choose from

# Data Reader
    # If conditions are met from selector, it uses the data referenced as 'y'
    # Note: w is the energy consumption rate of each appliances
    # If the incorrect appliance is inputted, the program starts again
    # data is a simple file opener to which opens the designated .csv file which stores each appliances usage
data = pd.read_csv('AppliancesUsage.csv')
residents = 3
if selector == 'TV':
    y = data['TV_Living']
    w = 400
elif selector == 'Fridge':
    y = data['Fridge']
    w = 250
elif selector == 'Oven':
    y = data['Oven']
    w = 2400
elif selector == 'Washing Machine':
    y = data['Washing_Machine']
    w = 730
elif selector == 'Microwave':
    y = data['Microwave']
    w = 1150
elif selector == 'Dryer':
    dryer_winter1 = input(' [ Would you like to simulate a winter usage? ]')
    if dryer_winter1 == 'Y':
        y = data['Winter_Dryer']
        w = 520
    elif dryer_winter1 == 'N':
        y = data['Dryer']
        w = 520
elif selector == 'Hairdryer':
    y = data['Hairdryer']
    w = 1600
elif selector == 'Study Lamp':
    y = data['StudyTable_Lamp']
    w = 5
elif selector == 'Computer':
    y = data['Computer']
    w = 550
elif selector == 'Laptop':
    y = data['Laptop']
    w = 45
else:
    print(' [ Invalid Appliance ]')
    sys.exit('[ PROGRAM TERMINATED ]')


# Plotter : The aim of this plot is to visualise when each appliances are being used and does so through a plot animation.
#           Graph plotter is live, so it will show each hourly use progressively per second.
ytrue = y
plt.style.use('seaborn')

x_axis = []
y_axis = []
def animate(i):
    x_axis.append(next(ind_count))
    y_axis.append(next(y_axiscyc))
    plt.cla()
    plt.plot(x_axis, y_axis, marker = 'o', color = 'red')
    plt.title('Hourly '+ selector + ' usage')
    plt.xlabel('Time (0000-2400hr)')
    plt.ylabel('Usage within 1 hour')
    plt.xticks(rotation = 45)
    plt.xlim(-1, 24.5)

    plt.tight_layout()


ind_count = count()
y_axiscyc = cycle(ytrue)
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

# Summary: Finds the daily summary of for each appliances
#          Finds the total energy consumption and finds its per/hour rate
#          Outputs results from total, total_power and w (appliance consumption rate
total = sum(ytrue)
totalconsump = total*w
total_power = total*w/24
print('----------------------------------------------------------------------------')
print('----------------------------------------------------------------------------')
print(' [ USAGE DATA ]' )
print(ytrue)
print('----------------------------------------------------------------------------')
print('----------------------------------------------------------------------------')
print('\n [ SUMMARY ] \n')
print(' [ TOTAL TIME USED: ' + str(total) + ' ] ')
print(' [ RESIDENTS: ' + str(3) + ' ] ')
print(' [ POWER CONSUMPTION RATE OF: ' + str(w) + ' ] ')
print(' [ TOTAL POWER CONSUMPTION: ' + str(totalconsump) + ' ] ')
print('\n [ TOTAL POWER CONSUMPTION: ' + str(total_power) + ' w/hr ] \n')
print('----------------------------------------------------------------------------')
print('----------------------------------------------------------------------------')