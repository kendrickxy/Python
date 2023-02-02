#Initial values
num = int(input('INPUT IN DAYS: '))     # Here we're requesting the user to enter a value, which will be integer and called 'num'.

# Day in hours, Hour in minutes, minute in seconds.
hoursDay = 24
minHour = 60
secMin = 60

#Math and print!
# end = ' ' will keep the next print in line.
print ('IN ' , end =' ')
print(num , end = ' ')
print('day(s), are:' , end = ' ')
print ((((num*hoursDay)*minHour)*secMin) , end =' ')
print ('seconds.')