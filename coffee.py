#Main
# Declare variables and contants for this program
    # Delcare name of the items
    # Declare the number of items purchased
    # Declare the price of the item

# input: Get input from the customer:
 

def main():
# Declare Variables and constants for this program
    nameOfItem = 'Coffee'
    nameOfItem2 = 'Muffin'
    numberOfItemsPurchased = 0

#Get input from the customer
    nameOfItem = input("What are you purchasing? " )
    nameOfItem2 = input("What are you purchasing? " )
    numberOfItemsPurchased = int(input("Please enter the priceof the items bought: "))
    priceOfItem = int(input("Please enter the price of the item: " ))

#Calculate the total 
    totalCost = 0
    totalCost = numberOfItemsPurchased * priceOfItem

#Display the receipt to the customer
    print( "___ Receipt __")
    print("Item Purchased: ")
    print("Number purchased: ", numberOfItemsPurchased)
    print("Price of Each Item: ", priceOfItem)
    print("Total Cost: ", totalCost)
main()

