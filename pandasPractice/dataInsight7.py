import pandas as pd 
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "=" *25 
SalesData = xl.parse("Orders")
SubCatData = SalesData[["Sub-Category", "Discount"]]
print(lines)
#Use functions to group by state and sum then sort
SubCatDiscount = SubCatData.groupby(by = "Sub-Category").mean().sort_values(by = "Discount")
#Print top 10 this time
print(SubCatDiscount)