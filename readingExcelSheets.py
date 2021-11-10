import pandas as pd
file = pd.ExcelFile("/Users/dell/Desktop/sales.xlsx")
print(file.sheet_names)
sheet = file.parse("sales")
print("************************************")

print(sheet)
print("************************************")

print(type(sheet))
print("************************************")

print(sheet.Date)
print("************************************")

print(sheet.Amount.sum())
print("************************************")

print(sheet.loc[0])
print("************************************")
print(sheet.loc[0, "Amount"])