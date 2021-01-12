people = ["Johny", "Marry", "Francis","Ion","Marius","Boris"]




print("BEFORE",people)
place_to_change=int(input("What place do you want to change?"))-1
where_to_change=int(input("Where you want to change?"))-1

if len(people)<place_to_change or len(people)<where_to_change:
    print("Error, wrong number")
else:
    temp=people[place_to_change]
    people[place_to_change]=people[where_to_change]
    people[where_to_change]=temp
    print("AFTER", people)