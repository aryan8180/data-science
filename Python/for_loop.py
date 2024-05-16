expenses = [120,350,1300,1500,1700]

total = 0
for expense in expenses:
    total += expense 

print("The total expenses is: ", total)

for i in range(len(expenses)):
    print("Month: ", i+1, "Expense: ", expenses[i])

key_location = "living room"

locations = ["garage", "living room", "chair room", "closet"]
for i in range(len(locations)):
    if(locations[i]==key_location):
        print("Key is in the ", key_location)
        break
    else:
        print("Key is not present in the ", locations[i])