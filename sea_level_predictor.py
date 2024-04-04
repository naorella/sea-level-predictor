#sea_level_predictor.py
#Code Author: Nelson Orellana
#code template form freecodecamp.org
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


#draw_plot(): uses the epa-sea-level.csv to read data and creates scatter plots
#draw_plot(): None -> plt.gca()
#Requires: that a csv named "epa-sea-level" be present with data under columns
#   'Year', 'CSIRO Adjusted Sea Level'
def draw_plot():
    # Read data from file
    file_df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8,6))
    x = file_df['Year']
    y = file_df['CSIRO Adjusted Sea Level']
    ax.scatter(x,y)

    #extend years to make prediction
    future = range(2014,2051)
    future = pd.Series(future)
    

    # Create first line of best fit
    line_fit1 = linregress(x = x, y = y)
    x = pd.concat(objs =[x, future])
    #plot the line using the now extended years
    plt.plot(x,line_fit1.intercept + line_fit1.slope*x,'r')

    # Create second line of best fit
    #need to filter the x values, so that years are only listed from 2000, to now
    present_df = file_df.query('`Year` >= 2000')
    x = present_df['Year']
    y = present_df['CSIRO Adjusted Sea Level']
    #create line of best fith filtered data
    line_fit2 = linregress(x,y)
    #we create the line before adding the years, so that the line
    #represent only the data we gave it first
    x = pd.concat(objs = [x, future])
    plt.plot(x,line_fit2.intercept + line_fit2.slope*x,'g')


    # Add labels and title
    ax.set(title = 'Rise in Sea Level',
           xlabel = 'Year',
           ylabel = 'Sea Level (inches)')
    xtick_loc = [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
    ax.set_xticks(ticks = xtick_loc)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()