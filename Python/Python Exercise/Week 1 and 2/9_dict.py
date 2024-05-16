# 1
# country = {
#     "china" : "143",
#     "india" : "136",
#     "usa" : "36",
#     "pakistan" : "21"
# }

# ask = input("What would you like to do? print, add, remove, query\n")
# if ask == "print":
#     print("china==>",country["china"])
#     print("india==>",country["india"])
#     print("usa==>",country["usa"])
#     print("pakistan==>",country["pakistan"])
# elif ask == "add":
#     more_country = input("What more country would you like to add?")
#     if more_country in country:
#         print("The following country already exists.")
#     else:
#         population = int(input("Enter the population of the country: "))
#         country.update({more_country:population})
#         print(country)
# elif ask == "remove":
#     country_name = input("Enter the country name you want to remove:")
#     if country_name in country:
#         country.pop(country_name)
#         print(country)
#     else:
#         print("This country doesn't exist")
# elif ask == "query":
#     enter_country = input("Enter the name of the country:")
#     if enter_country in country:
#         print({country[enter_country]})
#     else:
#         print("The country entered is not present")

# 2
# def average(info):
#     sum = 0
#     for i in range(len(info)):
#         sum += info[i]
#         i+=1
#     return round((sum/(len(info))),2)

# info = [600,630,620]
# ril = [1430,1490,1567]
# mtl = [234,180,160]
# gross = [info,ril,mtl]

# ask = input("Enter the operation to be carried out: print or add\n")
# if ask == "print":
#     print("info ==>",info, "==> avg: ",average(info))
#     print("ril ==>",ril,"==> avg: ",average(ril))
#     print("mtl ==>",mtl,"==> avg:",average(mtl))
# elif ask == "add":
#     sticket = input("Enter the stock ticket:")
#     sprice = input("Enter the price:")
#     if sticket in gross:
#         print("This stock already exists")
#     else:
#         sticket = [sprice]
#         gross.append(sticket)
#         print(gross)

# 3
