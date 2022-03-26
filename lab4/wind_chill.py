"""CS 108 Lab 4.1

This application uses user input temperature and wind speed to
calculate the wind chill and tells you how many layers to wear.

@author: Sam Hoogewind (sth6)
@date: Fall, 2020
"""

# Prompt the user for the temperature and wind speed
temp = float(input('Temperature: '))
wind_speed = float(input('Wind speed: '))

# If the wind speed and temperature are out of the bounds of the formula,
# print an error
if (wind_speed < 2) or (-58 > temp) or (temp > 41):
    print('Invalid input')

# If they are in the bound, calculate and print the wind chill
else:
    wc_temp = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) \
    + (0.4275 * (temp * (wind_speed ** 0.16)))
    print('Wind chill: ' + str(wc_temp))

# Print how many layers you should wear depending on the wind chill result
    if (wc_temp < -40):
        print('Stay home!')
    if (-40 <= wc_temp < -10):
        print('Four layers')
    if (-10 <= wc_temp < 20):
        print('Three layers')
    if(20 <= wc_temp < 40):
        print('Two layers')
    if(wc_temp >= 40):
        print('One layer')
    