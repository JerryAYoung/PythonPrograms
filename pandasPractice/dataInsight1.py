import pandas as pd 
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "=" * 25
SalesData = xl.parse("Orders")
SubCatData = SalesData[["Sub-Category", "Profit"]]
print(lines)
#Use functions to group bvy state and sum then sort
SubCatProfit = SubCatData.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
#Print top 10 this time
print(SubCatProfit.head(10))