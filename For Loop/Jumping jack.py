total_jumping_jack=100
sets=10
completed=0

for i in range(0,total_jumping_jack,sets):
    print(f"Performed {sets} jumping jacks.")
    completed+=sets
    remaining=total_jumping_jack-completed

    tried=input("Are you tried?(Yes/no): ")
    if tried == "yes" or "y":
        skip_remaining=input("Do you want to skip the remaining sets?(yes/no):")
        if skip_remaining=="yes":
            print(f"You have completed totl of {completed} jumping jack")
            break
    if remaining>0:
        print(f"you have {remaining} jumping jack remaining.")
    if i==total_jumping_jack-sets:
        print("Congratulations! you completed the workout")
