# input the amout of minutes to calculate
input = float(input('Number of minutes: '))

# 1440 minutes in 1 day
day = 1440
# 24 hours in a day
hday = 24
# 60 minutes in 1 hour
hour = 60
#60 seconds in a minute
msecond = 60



# How many days in the input
daycalc = input//day

# How many hours in the input, minus the days already counted.
hourcalc = (input//hour)-(daycalc*hday)

# How minutes left in an hour
minutecalc = input%hour

# How many seconds left in a minute
secondcalc = input%1

# What's the value in seconds
secondval = input * msecond

# First part of the text
print(input, 'minutes are equal to:     ', end = ' ')

# Second part of the text

if input >= day:
    if daycalc > 1:
        print(daycalc, 'days', end = ' ')
    else: print(daycalc, 'day', end = ' ')

if hourcalc > 1:
    print(hourcalc, 'hours', end = ' ')
elif hourcalc == 0:
    print('', end = ' ')
else: print(hourcalc, 'hour', end = ' ')

if minutecalc > 1 and input > 60:
    print(minutecalc, 'minutes', end = ' ')
elif input < 60 and input > 1:
    print(minutecalc, 'minutes...Duh!', end = ' ')
elif minutecalc < 1:
    print('', end = ' ')
else: print(minutecalc, 'minute', end = ' ')


# CHALLENGE: THE SECONDS MODULE IS BROKE. TRY TO FIX IT YOURSELF!

#if secondcalc < 1:
#    print(secondval, 'seconds', end = ' ')
#elif secondval <= 1:
#    print(secondval, 'second', end = ' ')