# The function .split() will split a text into individual string between each space
km , kmh = input('Enter both the distance and the speed separated but a single space (km km/h): ').split()


print('Distance in kilometers (km): ', km)
print('Speed in kilometers per hour (km/h): ', kmh)

print ('distance: ', km, 'kilometers')

print('speed: ', kmh, 'km/h')

# Distance / Speed = Time

print('The time of flight is: ', int(km)/int(kmh), 'hour(s)')


#EXAMPLE:
#   The light takes 8 and 1/3 minutes to reach us.

#   Try for yourself:

#   Sun to earth distance: 150000000 (150 million kms)
#   Speed of light in km/h: 1080000000 (300 000 km/s or 1.08 billion km/h)