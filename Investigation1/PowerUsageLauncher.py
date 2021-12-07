# Program name:
#              PowerUsageLauncher.py: displays current energy readings and cumulative/total used readings within each day
#
# Created by:
#            Name - John Aaron Dayao Lumagbas
#            StudentID - 20165510
# 'Finalised version of 'PowerUsageLauncher.py - 29.05.2020'


#Libraries Used, availablefiles is my own function/defined module
import matplotlib.pyplot as plt
import pandas as pd
from availablefiles import *
import os



            ###########################################################
            #                                                         #
            #           User Selection and File Validator             #
            #  prompts if user wants to plot/display energy readinfs  #
            #  which then sees if correct file exists, return to 1st  #
            #  to selection menu. Selection menu from availablefiles  # 
            #                                                         #
            ###########################################################
    
# User Selection and File Validator
user_ask = input('[ WOULD YOU LIKE TO OUTPUT CURRENT ENERGY READINGS? Y/N ]: ').upper()
if user_ask == 'Y':
    handler = None
    while handler is None:
        try:
            filename = input(' [PLEASE ENTER ENERGY READING (.csv)]: ')
            handler = pd.read_csv(filename)
        except FileNotFoundError:
            print(' [ ' + (filename) + ' DOES NOT EXIST ] ')
            av_files()
elif user_ask == 'N':
    exit('[ PROGRAM TERMINATED ]')

            #########################################################
            #                     Data Plotter                      #
            # This plotter plots 'Date' as its x axis, and 'Reading #
            # which are the energy readings as Y axis, plots a line #
            # graph for Nightly/Midday/Morning readings and a mixed #
            # /combined bar and line plot for Cumulative energy use #
            # for each day.                                         #
            #                                                       #
            #########################################################

# Data Plotter 
dates = handler['Date'].iloc[0:22].values
energyreading = handler['Reading'].iloc[0:22].values
plt.style.use('ggplot')
plt.plot(dates,energyreading, linestyle='-', marker='o', color='red')
plt.title(os.path.splitext(filename)[0]+' Energy usage within 22 days')
plt.xlabel('Date')
plt.ylabel('Energy Usage(kw/h)')
if filename== 'Cumulative.csv':
    plt.bar(dates,energyreading,color='purple')
    plt.xticks(rotation=45)
plt.xticks(rotation = 45)
plt.show()



# JLUMAGBAS
