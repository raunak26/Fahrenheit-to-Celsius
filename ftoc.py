# ftoc.py
# Raunak Anand
# program to convert a temperature
# from degrees Farenheit to degrees Celsius

ftemp = float(input("Enter degrees in Fahrenheit: ")) # user input 
ctemp = (5 / 9) * (ftemp - 32) # Fahrenheit to Celsius formula
ctemp = '{0:.2f}'.format(ctemp) # round off Celsius to two decimal places
print(ftemp, "degrees Fahrenheit is", ctemp, "degrees centigrade")
