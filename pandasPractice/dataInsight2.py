import pandas as pd 
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "=" * 25
SalesData = xl.parse("Orders")
ProductData = SalesData[["Product Name", "Profit", "Sales"]]
print(lines)
#We are going to use functions to group by state and sum then sort
ProdProfSales = ProductData.groupby(by = "Product Name").sum().sort_values(by = "Profit")
#Print top 10 again
print(ProdProfSales.head(10))