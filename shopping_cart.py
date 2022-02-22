
from datetime import datetime
import os
from dotenv import load_dotenv


products = [
    {
        "id":1, 
        "name": "Chocolate Sandwich Cookies", 
        "department": "snacks", 
        "aisle": "cookies cakes", 
        "price": 3.50},
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

tax_rate = float(os.getenv("TAX_RATE", default=0.0875))

def to_usd(my_price):
        """
        Converts a numeric value to usd-formatted string, for printing and display purposes.

        Param: my_price (int or float) like 4000.444444

        Example: to_usd(4000.444444)

        Returns: $4,000.44
        """
        return f"${my_price:,.2f}" #> $12,000.71

if __name__ == "__main__":

    length = 0
    u = 0
    ids = []
    i = 0
    cart = []
    cartP = []
    x = 0
    rudone = 0
    y = 0
    subtotal = 0
    total = 0
    z = 0

    u = input("Please enter product ID:\n")
    length = len(products)  
    while(i<length):
        ids.append(str(products[i]["id"]))
        i = i+1
 
# when rudone is 0, loop will continue. When rudone is 1, loop will stop 
    while(rudone == 0):
        while(x<length):
            if u == ids[x]:
                print(products[x]["name"])
                print(to_usd(products[x]["price"]))
                cart.append(products[x]["name"])
                cartP.append(products[x]["price"])
            x = x+1
        x = 0
        u = input("Please enter product ID:\n")
        if (u == "done" or u == "DONE" or u == "Done"):
            rudone = 1
    
    while (y<len(cartP)):
        subtotal = subtotal + cartP[y]
        y=y+1
    
    total = subtotal*(1+tax_rate)

    datentime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")   
    print("\n\n--------------------------------")
    print("Elizabeth's Grocery Store")
    print("--------------------------------")
    print("999-999-0090 | elizabethgrocery.com\n--------------------------------", 
        "\nCheckout at", datentime,"\n--------------------------------\n")   
    print("Items:\n")

    while (z<len(cart)):
        print("- " + cart[z]+ " ... " + to_usd(cartP[z])+"\n")
        z=z+1
    
    print("--------------------------------")
    print("Subotal: " + to_usd(subtotal))
    print("Sales Tax: " + to_usd(total-subtotal))
    print("Checkout Total: " + to_usd(total))
    print("--------------------------------")
    print("THANK YOU FOR SHOPPING WITH US, PLEASE COME AGAIN!")
    print("--------------------------------")