#1.
def formated(num,char):
    format_string="num:{0},char:{1}".format(num,char)
    return format_string
string=formated(145,"o")
print(string)

#2
radius=84
pi=3.14
area=pi*(radius**2)
print(area)

#2bonus
radius=float(input("Enter ther radius: "))
pi=3.14
area=pi*(radius**2)
water_per_sqm=1.4
water=area*water_per_sqm

print(round(water))

#3.
distance=490
time=7*60
speed=distance/time

print(round(speed),"meter/sec")