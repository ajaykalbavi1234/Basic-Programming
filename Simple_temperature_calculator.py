def Celsius_to_farenheit(temp):
    return round((9/5)*temp + 32,2)
def Celcius_to_Kelvin(temp):
    return round(temp + 273.15,2)
def Farenheit_to_Celcius(temp):
    return round((5/9)*(temp-32),2)
def Kelvin_to_Celcius(temp):
    return round(temp - 273.15,2)
def Farenheit_to_Kelvin(temp):
    return round((5/9)*(temp-32) + 273.15,2)
def Kelvin_to_Farenheit(temp):
    return round((9/5)*(temp-273.15) + 32,2)

temperature = int(input())
temp_scale = str(input())
if temp_scale == 'C':
    print(Celcius_to_Kelvin(temperature),Celsius_to_farenheit(temperature))
elif temp_scale == 'F':
    print(Farenheit_to_Celcius(temperature),Farenheit_to_Kelvin(temperature))
else:
    print(Kelvin_to_Celcius(temperature),Kelvin_to_Farenheit(temperature))