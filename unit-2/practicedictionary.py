

# #get associated value from first item in key pair
# capitals = {"Minnesota": "St.Paul",
#             "New York": "Albany",
#             "Hawaii": "Honolulu",
#             "Nebraska": "Lincoln",
#             "Ohio": "Columbus"}
# print(capitals.get("Ohio"))

# #see if an item exists
# capitals = {"Minnesota": "St.Paul",
#             "New York": "Albany",
#             "Hawaii": "Honolulu",
#             "Nebraska": "Lincoln",
#             "Ohio": "Columbus"}
# if capitals.get("New Jersey"):
#     print("That capital exists")
# else:
#     print("That item is not in the list")

# #update list to include another key pair or update an existing one
# capitals = {"Minnesota": "St.Paul",
#             "New York": "Albany",
#             "Hawaii": "Honolulu",
#             "Nebraska": "Lincoln",
#             "Ohio": "Columbus"}

# capitals.update({"Montana": "Helena"})
# capitals.update({"Hawaii": "Waikiki"})
# print(capitals)

# #print just the key values
# capitals = {"Minnesota": "St.Paul",
#             "New York": "Albany",
#             "Hawaii": "Honolulu",
#             "Nebraska": "Lincoln",
#             "Ohio": "Columbus"}
# print(capitals.keys())

# #how to do a for loop over just the keys by making the key an object first
# capitals = {"Minnesota": "St.Paul",
#             "New York": "Albany",
#             "Hawaii": "Honolulu",
#             "Nebraska": "Lincoln",
#             "Ohio": "Columbus"}
# key = capitals.keys()
# for key in capitals.keys():
#     print(key)

#     #how to do a for loop over just the values by making the value an object first
# capitals = {"Minnesota": "St.Paul",
#             "New York": "Albany",
#             "Hawaii": "Honolulu",
#             "Nebraska": "Lincoln",
#             "Ohio": "Columbus"}
# values = capitals.values()
# for value in capitals.values():
#     print(value)

# #print each value pair
# capitals = {"Minnesota": "St.Paul",
#             "New York": "Albany",
#             "Hawaii": "Honolulu",
#             "Nebraska": "Lincoln",
#             "Ohio": "Columbus"}
# for key, value in capitals.items():
#     print (f"{key}: {value}")