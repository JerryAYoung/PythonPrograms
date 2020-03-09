import pandas as pd 
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "=" * 25 + "\n"
SalesData = xl.parse("Orders")

ProductData = SalesData[["Sub-Category", "Product Name", "Profit"]]
NegSubCats = ["Tables", "Bookcases", "Supplies"]

for subcat in NegSubCats:
	ProductInfo = ProductData.loc[ProductData["Sub-Category"]== subcat]
	ProdProfit = ProductInfo.groupby(by = "Product Name").sum().round().sort_values(by = "Profit")
	print(subcat)
	print(ProdProfit)
	print(lines)