##1. BMI calculator

height=float(input("Enter height in meters: "))
weight=float(input("Enter weight in Kilograms: "))

BMI=weight/(height**2)

if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 or BMI<25:
    print("Normal")
elif BMI>=25 or BMI<29:
    print("Overweight")
else:
    print("Obesity1.75")


#2. Write a program to determine which country a city belongs to. Given list of cities per country: 
 
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UnAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]

city=input("Enter a citAbu Dhabiy name:")

if city in Australia:
    print(f"{city} is in Australia")
elif city in UnAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print("Enter vaild city name")


#3. Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the same country or not. 

city1=input("Enter the first city:")
city2=input("Enter the second city:")

if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in UnAE and city2 in UnAE:
    print("Both cities are in UAE")
elif city1 in India and city2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")



