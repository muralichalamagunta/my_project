import pandas as pd


# di = {"Name": ["abd","def","mna"], "Roll": [1,2,3], "per": [89.9,90.8,99]}
# df=pd.DataFrame(di)
# print(df)

# L=[("abd",10,89,1), ("abv",10,89,1), ("abk",10,89,1)]
# df=pd.DataFrame(L)
# print(df)


# pd.set_option('display.max_columns', None)
# d=pd.read_csv("C:\\Users\\rahan\\OneDrive\\Desktop\\mental_health_remote_workers.csv")
# df=pd.DataFrame(d)
# # print(df.head())

# df.to_csv("output.csv")

d=pd.read_csv("C:\\Users\\rahan\\OneDrive\\Desktop\\mental_health_remote_workers.csv")
df=pd.DataFrame(d)
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.shape)
# print(df[2:10:2])
# print(df[["Name", "Age"]][2:10:2])
# for rec in df.iterrows():
#     print(rec) 

# print("Using LOC")
# print(df.loc[2])
# print(df.loc[2, ["Age"]])
# print(df.loc[99, ["Age", "Country"]])
# print(df.loc[0:2])  
# print(df.loc[0:2,["Age"]])
# print(df.loc[0:2,["Age","Country"]])
# print(df.head())
# print(df.loc[0:2,"Name":"Job_Role"]) 

# print("Sorting Dataframe")
# print(df.sort_values("Age"))
# print(df.sort_values("Age",ascending=False)) 

# print("Manipulating Dataframe")
# print("Adding column")
# print(df.head())
# df["Age2"] = 20
# df["Total"] = 0
# df["Total"] = df["Age"] + df["Age2"]
# df.drop(columns="Experience_Years", inplace=True)
# print(df.head())

# print("Removing Dupilcates")
# pd.set_option('display.max_rows', None)
# print(df.duplicated(subset = 'Country')) 

print("Removing Missing and filling Data")
print(df.head())  