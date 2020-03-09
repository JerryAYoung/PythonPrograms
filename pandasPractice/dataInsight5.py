import pandas as pd 
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "=" * 25
SalesData = xl.parse("Orders")
segments = SalesData.Segment.unique()
print(segments)
SubCatData = SalesData[["Sub-Category", "Profit", "Segment"]]

for segment in segments:
	RegSubCatData = SubCatData.loc[SubCatData["Segment"]==segment]
	SubCatProfit = RegSubCatData.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
	#Print top 10
	print(lines)
	print(segment)
	print(SubCatProfit.head(10))
