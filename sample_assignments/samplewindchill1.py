print('This program computes wind chill in Fahrenheit.')
temperature = float(input('Enter the current temperature in degrees F: '))
wind_speed = float(input('Enter the current wind speed in miles/hour: '))
# set the formula for windchill
wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** .16 + 0.4275 * temperature * wind_speed ** .16
# print the outcome
print(f'When the temp is {temperature} and the wind speed is {wind_speed} the windchill is {wind_chill}')

