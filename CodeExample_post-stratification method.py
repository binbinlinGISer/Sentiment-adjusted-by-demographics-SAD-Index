import pandas as pd


# Import data
DataExample = pd.read_excel('Data_example.xlsx',sheet_name='Sheet1')

# The original percentage of negative Twitter users
Original_Negative_Pecentage = (DataExample["# Nagtive Twitter users"].sum() / DataExample["# Total Twitter users"].sum()) *100
print ("Original negative percentage is " + str(Original_Negative_Pecentage) +".")

############## Start to adjust the percentage ######################

# Calculate the percentage of Twitter users in each social group over the whole Twitter users
DataExample["% Twitter users"] = (DataExample["# Total Twitter users"] / DataExample["# Total Twitter users"].sum()) * 100

# Calculate the percentage of Twitter users in each social group over the whole Twitter users
DataExample["% Population"] = (DataExample["# Population"] / DataExample["# Population"].sum()) * 100

# Calculate the weight
DataExample["weight"] = DataExample["% Population"] / DataExample["% Twitter users"]

# Adjust the number of Twitter users in each social group according to the weight
DataExample["Adjusted_# Negtive Twitter users"] = DataExample["# Nagtive Twitter users"] * DataExample["weight"]
DataExample["Adjusted_# Neutral Twitter users"] = DataExample["# Neutral Twitter users"] * DataExample["weight"]
DataExample["Adjusted_# Postive Twitter users"] = DataExample["# Postive Twitter users"] * DataExample["weight"]

# The SAD index
SAD = (DataExample["Adjusted_# Negtive Twitter users"].sum() / (DataExample["Adjusted_# Negtive Twitter users"].sum() + DataExample["Adjusted_# Neutral Twitter users"].sum() + DataExample["Adjusted_# Postive Twitter users"].sum())) * 100
print ("The SAD index is " + str(SAD) + ".")