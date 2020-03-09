import pandas as pd 
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "=" * 25
SalesData = xl.parse("Orders")
regions = SalesData.Region.unique()
print(regions)
SubCatData = SalesData[["Sub-Category", "Profit", "Region"]]

for region in regions:
	RegSubCatData = SubCatData.loc[SubCatData["Region"]==region]
	SubCatProfit = RegSubCatData.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
	#Print top 10
	print(lines)
	print(region)
	print(SubCatProfit.head(10))