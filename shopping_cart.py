# shopping_cart.py

#imports to use in program
from nis import match


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
#keys: id name department aisle price

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output


subtotal = 0     #variable to hold total for transaction
transaction_ids = []    #list to hold all of the products in the transaction

#Condition to get user out of the loop
#??? How do I fail gracefully right now my code accepts letters as an input
while True:
    #ASK FOR USER INPUTS
    #product_id variable is a string for each product in a transaction
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")   
    
    #LET CASHIER END TRANSACTION
    if product_id == "DONE":
        break
    else:
        transaction_ids.append(product_id)

#PROGRAM OUTPUT
#Header
print("-----------------------")
print("HEB GROCERY")
print("WWW.HEBGROCERY.COM")
print("-----------------------")
#got help from Eugenie Chandon-Moet for Date and Time code
#????how do I make this say PM
from datetime import datetime
current_date = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
print("CHECKOUT AT:", current_date)
print("-----------------------")

#List of products in transaction
print("SELECTED PRODUCTS: ")
for product_id in transaction_ids:
    #matching_products is a list of everything in the transaction
    matching_products = [x for x in products if str(x["id"]) == str(product_id)]
        
    item = matching_products[0] #go into the list of dictionaries and grab the corresponding ID
    subtotal = subtotal + item["price"]   #add the current item to total price
    print(f"... {item['name']} ({to_usd(item['price'])})") #print the name of the item

print("-----------------------")
print(F"SUBTOTAL: {to_usd(subtotal)}")
import os
TAXRATE = float(os.getenv("TAXRATE", default="0.0875"))    #ask user for a tax rate environment variable
tax = subtotal * TAXRATE
print(F"TAX: {to_usd(tax)}")
total = subtotal + tax
print(F"TOTAL: {to_usd(total)}")
print("-----------------------")
print("THANKS, SEE Y'ALL REAL SOON!")
print("-----------------------")



