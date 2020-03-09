import pandas as pd 
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "=" * 25
SalesData = xl.parse("Orders")
SalesDataYear = SalesData
SalesDataYear["Year"] = SalesDataYear["Order Date"].dt.year 
years = SalesDataYear.Year.unique()
print(years)

SubCatData = SalesDataYear[["Sub-Category", "Profit", "Year"]]

for year in years:
	SubCatDataByYear = SubCatData.loc[SubCatData["Year"]==year]
	#Remove year column so that .sum doesn't total it
	SubCatProfitNoYear = SubCatDataByYear[["Sub-Category", "Profit"]]
	SubCatProfit = SubCatProfitNoYear.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
	print(lines)
	print(year)
	print(SubCatProfit.head(10))
