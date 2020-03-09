#Imports Pandas package
#Saves the excel file to a variable named xl
#Saves formatting to variable named lines
#Stores the sales data from the Excel sheet in variable named SalesData
import pandas as pd 
xl = pd.ExcelFile("OSSalesData.xlsx")
lines = "=" * 25
SalesData = xl.parse("Orders")

#Defines the main menu function for interactivty for users. 
def menu():
    while True:
    	print("\nEnter (1) to see Sub-Category Profits" + 
    	"\nEnter (2) to see Sub-Categories with Negative Profits" +
    	"\nEnter (3) to see the Sales and Profits of the 10 least profitable products" +
    	"\nEnter (4) to see Sub-Categories Profits by Customer Segment" +
    	"\nEnter (5) to see Sub-Categories Profits by Region" +
    	"\nEnter (6) to see Sub-Categories Profits by Year" +
    	"\nEnter (7) to see Sub-Category Discount Averages" +
    	"\nEnter (8) to Exit")
    	choice = input("Please enter your selection here: ")
    	if choice == "1":
    		getProfit()
    	elif choice == "2":
    		getProfitByProduct()
    	elif choice == "3":
    		getProfitByCategory()
    	elif choice == "4":
    		getProfitByRegion()
    	elif choice == "5":
    		getProfitBySegment()
    	elif choice == "6":
    		getProfitByYear()
    	elif choice == "7":
    		getDiscount()
    	elif choice == "8":
    		break
    	else:
    		print("\nPlease enter an option ONLY from 1-8 below: ")

#Defines function to get profit by sub-categories
def getProfit():
	SubCatData = SalesData[["Sub-Category", "Profit"]]
	print(lines)
	SubCatProfit = SubCatData.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
	print(SubCatProfit.head(10))

#Defines function to get profit for the 10 worst profitable products
def getProfitByProduct():
	ProductData = SalesData[["Product Name", "Profit", "Sales"]]
	print(lines)
	ProdProfSales = ProductData.groupby(by = "Product Name").sum().sort_values(by = "Profit")
	print(ProdProfSales.head(10))

#Defines function to get profits by categories
def getProfitByCategory():
	ProductData = SalesData[["Sub-Category", "Product Name", "Profit"]]
	NegSubCats = ["Tables", "Bookcases", "Supplies"]
	for subcat in NegSubCats:
		ProductInfo = ProductData.loc[ProductData["Sub-Category"]== subcat]
		ProdProfit = ProductInfo.groupby(by = "Product Name").sum().round().sort_values(by = "Profit")
		print(subcat)
		print(ProdProfit)
		print(lines)

#Defines function to get profits by U.S. regions
def getProfitByRegion():
	regions = SalesData.Region.unique()
	print(regions)
	SubCatData = SalesData[["Sub-Category", "Profit", "Region"]]
	for region in regions:
		RegSubCatData = SubCatData.loc[SubCatData["Region"]==region]
		SubCatProfit = RegSubCatData.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
		print(lines)
		print(region)
		print(SubCatProfit.head(10))

#Defines function to get profits by product segments
def getProfitBySegment():
	segments = SalesData.Segment.unique()
	print(segments)
	SubCatData = SalesData[["Sub-Category", "Profit", "Segment"]]
	for segment in segments:
		RegSubCatData = SubCatData.loc[SubCatData["Segment"]==segment]
		SubCatProfit = RegSubCatData.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
		print(lines)
		print(segment)
		print(SubCatProfit.head(10))

#Defines function to get profits by specific years
def getProfitByYear():
	SalesDataYear = SalesData
	SalesDataYear["Year"] = SalesDataYear["Order Date"].dt.year 
	years = SalesDataYear.Year.unique()
	print(years)
	SubCatData = SalesDataYear[["Sub-Category", "Profit", "Year"]]
	for year in years:
		SubCatDataByYear = SubCatData.loc[SubCatData["Year"]==year]
		SubCatProfitNoYear = SubCatDataByYear[["Sub-Category", "Profit"]]
		SubCatProfit = SubCatProfitNoYear.groupby(by = "Sub-Category").sum().sort_values(by = "Profit")
		print(lines)
		print(year)
		print(SubCatProfit.head(10))

#Defines function to get most discounted products
def getDiscount():
	SubCatData = SalesData[["Sub-Category", "Discount"]]
	print(lines)
	SubCatDiscount = SubCatData.groupby(by = "Sub-Category").mean().sort_values(by = "Discount")
	print(SubCatDiscount)

#Runs the scripts menu in the terminal window
menu()



