# 1
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# count = 0
# for i in range(len(result)):
#     if result[i] == "heads":
#         count += 1
# print("There are",count," heads")

# 2
# for i in range(1,11):
#     if i%2!=0:
#         print(i*i)
#     i += 1

# 3
# expense_list = [2340, 2500, 2100, 3100, 2980]
# month_expense = int(input("Enter the expenses whose month you want to find out: "))
# for i in range(len(expense_list)):
#     if(expense_list[i]==month_expense):
#         print(f"The entered expenses is of the month ", i+1)
#         break
#     else:
#         i += 1
#         continue
# print("The entered expense is not in the expense list")


# 4
# start = 0
# while(start<5):
#     tired_or_not = input("Are you tired?")
#     if tired_or_not == "no":
#         start+=1
#         if start == 5:
#             print("Congratulations, you have completed the reace") 
#     else:
#         print("You didn't complete the race")
#         break 

# 5
# num = int(input("Enter the number: "))
# for i in range(1,6):
#     s = ''
#     for j in range(i):
#         s += '*'
#     print(s)