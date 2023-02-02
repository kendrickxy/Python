text = 'EPIC'

# ONLY SINGLE CHARACTER ALLOWED

print(f'{text}')            #No format
print(f'{text:t<20}')       # adding after the text
print(f'{text:_>20}')       # adding before the text
print(f'{text:.^20}')       # surrounding text

print('\n')   # Separating the sections

var = 'cat'
var2 = 1000

print(f'{var }')            # printing just the value
print(f'{var2 = }')          # Printing the name and value

print('\n')   # Separating the sections

design1 = "A temperature Sensor"
design2 = 'A hygro sensor'

print('\n')   # Separating the sections

print(f"{design1:25} : Is used to monitor an environment's temperature")       #Adding a specific amount of space between the variable and the last bit
print(f"{design2:25} : Is used to monitor an environment's humidity")      #Adding a specific amount of space between the variable and the last bit

print('\n')   # Separating the sections