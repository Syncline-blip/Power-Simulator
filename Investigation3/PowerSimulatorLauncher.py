# Program name:
#              PowerSimulatorLauncher.py: Simulates appliance usage and consumption for a street of houses.
#
# Created by:
#            Name - John Aaron Dayao Lumagbas
#            StudentID - 20165510
# 'Finalised version of 'PowerModelLauncher.py - 31.05.2020'


# Libraries
import pandas as pd
from house_sim import  housing, houseappliances
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count, cycle


# Prompts the user to launch the simulator
print('[ HOUSE ENERGY CONSUMPTION SIMULATOR ]')
launcher = input('[ START? (Y) ]: ')

# Data Opener: Opens required .csv for each house
h1 = pd.read_csv('House1.csv')
h2 = pd.read_csv('House2.csv')
h3 = pd.read_csv('House3.csv')
h4 = pd.read_csv('House4.csv')
h5 = pd.read_csv('House5.csv')

# House Menu: stores the houses in Spooner Street and displays it for user input
print(' [ AVAILABLE HOUSES ]')
house1 = housing('29 Spooner Street','1').displayhouse()
house2 = housing('30 Spooner Street','7').displayhouse()
house3 = housing('31 Spooner Street','4').displayhouse()
house4 = housing('33 Spooner Street','3').displayhouse()
house5 = housing('35 Spooner Street','2').displayhouse()
print()

# House Selector: Each addresses have individual .csvs that store their common appliances and its hourly usage
  # Note: onoff = Simply calculates the hours used for each appliances and adds them together
  #       totalusage = Calculates the watt usage of the appliances and adds them together to show the total energy consumption

slct = input(' [ CHOOSE A HOUSE TO SIMULATE: ] ')
if slct == '29 Spooner Street':  # Condition for 29 Spooner Street
    print(h1)
    tv = h1['TV_Living']
    fridge = h1['Fridge']
    ov = h1['Oven']
    wmc = h1['Washing_Machine']
    mwave = h1['Microwave']
    dryer = h1['Dryer']
    hdryer = h1['Hairdryer']
    lamp = h1['StudyTable_Lamp']
    computer = h1['Computer']
    lap = h1['Laptop']
    onoff = sum(tv+fridge+ov+wmc+mwave+dryer+hdryer+lamp+computer+lap)
    totalusage = sum((tv*120)+(fridge*300)+(ov*2000)+(wmc*700)+(mwave*1150)+(dryer*550)+(hdryer*1600)+(lamp*5)+(computer*600)+(lap*40))
elif slct == '30 Spooner Street': # Condition for 30 Spooner Street
    print(h2)
    tv = h2['TV_Living']
    fridge = h2['Fridge']
    ov = h2['Oven']
    wmc = h2['Washing_Machine']
    mwave = h2['Microwave']
    dryer = h2['Dryer']
    hdryer = h2['Hairdryer']
    lamp = h2['StudyTable_Lamp']
    computer = h2['Computer']
    lap = h2['Laptop']
    onoff = sum(tv+fridge+ov+wmc+mwave+dryer+hdryer+lamp+computer+lap)
    totalusage = sum(
        (tv * 400) + (fridge * 250) + (ov * 2400) + (wmc * 730) + (mwave * 1150) + (dryer * 550) + (hdryer * 1600) + (
                    lamp * 5) + (computer * 550) + (lap * 70))
elif slct == '31 Spooner Street': # Condition for 31 Spooner Street
    print(h3)
    tv = h3['TV_Living']
    fridge = h3['Fridge']
    ov = h3['Oven']
    wmc = h3['Washing_Machine']
    mwave = h3['Microwave']
    dryer = h3['Dryer']
    hdryer = h3['Hairdryer']
    lamp = h3['StudyTable_Lamp']
    computer = h3['Computer']
    lap = h3['Laptop']
    onoff = sum(tv+fridge+ov+wmc+mwave+dryer+hdryer+lamp+computer+lap)
    totalusage = sum(
        (tv * 100) + (fridge * 200) + (ov * 2000) + (wmc * 700) + (mwave * 1150) + (dryer * 700) + (hdryer * 2000) + (
                    lamp * 5) + (computer * 750) + (lap * 50))
elif slct == '33 Spooner Street': # Condition for 33 Spooner Street
    print(h4)
    tv = h4['TV_Living']
    fridge = h4['Fridge']
    ov = h4['Oven']
    wmc = h4['Washing_Machine']
    mwave = h4['Microwave']
    dryer = h4['Dryer']
    hdryer = h4['Hairdryer']
    lamp = h4['StudyTable_Lamp']
    computer = h4['Computer']
    lap = h4['Laptop']
    onoff = sum(tv+fridge+ov+wmc+mwave+dryer+hdryer+lamp+computer+lap)
    totalusage = sum(
        (tv * 100) + (fridge * 250) + (ov * 2100) + (wmc * 600) + (mwave * 1150) + (dryer * 650) + (hdryer * 1600) + (
                    lamp * 5) + (computer * 500) + (lap * 65))
elif slct == '35 Spooner Street': # Condition for 35 Spooner Street
    print(h5)
    tv = h5['TV_Living']
    fridge = h5['Fridge']
    ov = h5['Oven']
    wmc = h5['Washing_Machine']
    mwave = h5['Microwave']
    dryer = h5['Dryer']
    hdryer = h5['Hairdryer']
    lamp = h5['StudyTable_Lamp']
    computer = h5['Computer']
    lap = h5['Laptop']
    onoff = sum(tv+fridge+ov+wmc+mwave+dryer+hdryer+lamp+computer+lap)
    totalusage = sum(
        (tv * 150) + (fridge * 300) + (ov * 2300) + (wmc * 700) + (mwave * 1200) + (dryer * 800) + (hdryer * 1000) + (
                    lamp * 7) + (computer * 600) + (lap * 70))
else:
    print('[ HOUSE NOT IN STREET ]') # Outputs if house doesnt exist

# Calculator/s
kWh = (totalusage)/1000/24# Converts total w to kwh



# Plot
# Plotter : The aim of this plot is to visualise when each appliances are being used and does so through a plot animation.
#           Graph plotter is live, so it will show each hourly use progressively per second.
# This plotter method is also used for Investigation 2, in PowerModelLauncher.py

# Appliance Assignment
app1 = tv
app2 = fridge
app3 = ov
app4 = wmc
app5 = mwave
app6 = dryer
app7 = hdryer
app8 = lamp
app9 = computer
app10 = lap

# Using an imported plot style for visual aesthetic
plt.style.use('seaborn')


x_axis = []
# Each appliances are re-stored into a list for later plotting
y_axis1 = []
y_axis2 = []
y_axis3 = []
y_axis4 = []
y_axis5 = []
y_axis6 = []
y_axis7 = []
y_axis8 = []
y_axis9 = []
y_axis10 = []
def animate(i): # Creates a function to use for the animation
    x_axis.append(next(ind_count))
    y_axis1.append(next(y_axiscyc1))
    y_axis2.append(next(y_axiscyc2))
    y_axis3.append(next(y_axiscyc3))
    y_axis4.append(next(y_axiscyc4))
    y_axis5.append(next(y_axiscyc5))
    y_axis6.append(next(y_axiscyc6))
    y_axis7.append(next(y_axiscyc7))
    y_axis8.append(next(y_axiscyc8))
    y_axis9.append(next(y_axiscyc9))
    y_axis10.append(next(y_axiscyc10))
    plt.cla()
    plt.plot(x_axis, y_axis1, marker='o', color='red', label = 'TV')
    plt.plot(x_axis, y_axis2, marker='o', color='green', label = 'Fridge')
    plt.plot(x_axis, y_axis3, marker='o', color='orange', label = 'Oven')
    plt.plot(x_axis, y_axis4, marker='o', color='blue', label = 'W.Machine')
    plt.plot(x_axis, y_axis5, marker='o', color='pink', label = 'Dryer')
    plt.plot(x_axis, y_axis6, marker='o', color='magenta', label = 'M.Wave')
    plt.plot(x_axis, y_axis7, marker='o', color='cyan' ,label = 'Dryer')
    plt.plot(x_axis, y_axis8, marker='o', color='brown', label = 'H.Dryer')
    plt.plot(x_axis, y_axis9, marker='o', color='black', label = 'PC')
    plt.plot(x_axis, y_axis10, marker='o', color='yellow',label = 'Laptop')
    plt.title('Hourly Appliance Usage of:' + slct)
    plt.xlabel('Time (0000-2400hr)')
    plt.ylabel('Usage within 1 hour')
    plt.xticks(rotation = 45)
    plt.xlim(-1, 24.5)
    plt.legend(loc='upper left')
    plt.tight_layout()


# Cycles through each data in csv
ind_count = count()
y_axiscyc1 = cycle(app1)
y_axiscyc2 = cycle(app2)
y_axiscyc3 = cycle(app3)
y_axiscyc4 = cycle(app4)
y_axiscyc5 = cycle(app5)
y_axiscyc6 = cycle(app6)
y_axiscyc7 = cycle(app7)
y_axiscyc8 = cycle(app8)
y_axiscyc9 = cycle(app9)
y_axiscyc10 = cycle(app10)

# Applying the matplotlib animation module to our animate(i) function
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

# Summary: Shows the house details, its consumption etc, fomatted through the imported object
summary = houseappliances(onoff, totalusage, kWh).displayappliances()
print()















