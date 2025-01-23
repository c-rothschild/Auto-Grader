#!/usr/bin/env python3

def get_wind_speed_factor(wind_speed: float):
    return wind_speed**0.16

def get_wind_chill(temp: float, wind_speed: float):
    # gross evil formula
    return 35.74 + (0.6215 * temp) - (35.75 * get_wind_speed_factor(wind_speed)) + (0.4275 * temp * get_wind_speed_factor(wind_speed))

def get_rounded_wind_chill(temp: float, wind_speed: float):
    return round(get_wind_chill(temp, wind_speed), 1)

print("Welcome to the wind chill calculator 3000, where we do the ugly math so you don't have to!")

temp_f = float(input("Enter the current temperature in degrees fahrenheit: "))
wind_speed_mph = float(input("Enter the current wind speed in mph: "))

print(f"When the tempreature is {temp_f}°f and the wind speed is {wind_speed_mph} mph, the wind chill is {get_rounded_wind_chill(temp_f, wind_speed_mph)}°f")
