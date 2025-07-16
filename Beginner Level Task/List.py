justice_league=["superman","Batman","wonder woman","flash","aquaman","green lantern"]

#1. Calculate the number of members in the Justice League.
print(len(justice_league))

#2. Batman recruited Batgirl and Nightwing as new members. Add them to your list. 

new=["bat girl","Nightwing"]
justice_league.extend(new)
print(justice_league)

#3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.

justice_league[0],justice_league[2]=justice_league[2],justice_league[0]
print(justice_league)

#4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash. 

justice_league[4],justice_league[5]=justice_league[5],justice_league[4]
print(justice_league)

#5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following 
#   new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".

justice_league=["cyborg","shazam","hawkgirl","martian manhunter","green arrow"]
print(justice_league)

#6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.

justice_league.sort()
print(justice_league)
print(f"{justice_league[0]} will lead the new team...")
