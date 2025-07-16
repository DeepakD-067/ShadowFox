import random
n=30
count6=0
count1=0
double6=0
previousdie= None

for i in range(n):
    die=random.randint(1,6)
    if die==6:
        count6+=1
        if previousdie==6:
            double6+=1
    elif die==1:
        count1+=1
    previousdie=die

print(f"Number of times rolls:{n}")
print(f"Number of time die is six:{count6}")
print(f"Number of time die is one:{count1}")
print(f"Number of time die is  two 6 in row: {double6}")
