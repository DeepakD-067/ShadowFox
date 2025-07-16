#1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result. 
#   Try to identify the representation used.

def formated(num,char):
    format_string="num:{0},char:{1}".format(num,char)
    return format_string
string=formated(145,"o")
print(string)

#2.In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π r^2. 
#  (Use the value 3.14 for π) Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? 
#  Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter 

radius=84
pi=3.14
area=pi*(radius**2)
print(area)

#Bonus

radius=float(input("Enter ther radius: "))
pi=3.14
area=pi*(radius**2)
water_per_sqm=1.4
water=area*water_per_sqm

print(round(water))

#3.  If you cross a 490meterlong street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it.
#    Hint: Speed = Distance / Time

distance=490
time=7*60
speed=distance/time

print(round(speed),"meter/sec")
