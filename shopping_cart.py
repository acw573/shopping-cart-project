# shopping_cart.py

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


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output


# 1) capture product ids until we're done
# (use infinite while loop)



valid_inputs = []
for p in products:
        valid_inputs.append(str(p["id"]))

selected_ids = []

subtotal = 0

while True:
    selected_id = input("Please select / scan a valid product id or write DONE if there are no more items: ")
    if selected_id.upper() == "DONE":
        break
    elif selected_id not in valid_inputs:
        print("INVALID INPUT. PLEASE TRY AGAIN.")
    else:
        selected_ids.append(selected_id)

# 2) Perform product lookups to determine what the product's name and price are
#selected_ids = ["1","2","3","2","1"]
for selected_id in selected_ids:
    print(selected_id)
    # lookup the corresponding product!
    # or maybe display the selected product's name and price
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal = subtotal + matching_product["price"]
    print(matching_product["name"], "(", to_usd(matching_product["price"]), ")")


print("------------------------------")
print("ADAM'S GROCERY STORE")
print("www.adamsgrocerystore.com")
print("PHONE: (973) 902-9137")
print("------------------------------")

import datetime

start_time = '2021-03-04T19:00:00-05:00' # this is the given string we want to parse
template = '%Y-%m-%dT%H:%M:%S%z' # this is the format code corresponding with the given string we want to parse

now = datetime.datetime.now()
print("CHECKOUT AT:", now.strftime("%Y-%m-%d %H:%M:%S")) #> 2017-07-04 10:59:59
print("------------------------------")
print("SUBTOTAL: " + str(to_usd(subtotal)))
tax_rate = .0875
sales_tax = subtotal * tax_rate
total_price = subtotal + sales_tax
print("SALES TAX @ 8.75%: ", to_usd(sales_tax))
print("TOTAL PRICE: ", to_usd(total_price))
print("------------------------------")
print("THANKS, SEE YOU AGAIN!")
print("------------------------------")

# ATTEMPT AT EMAIL AUTOMATION
# import os
# from dotenv import load_dotenv
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# 
# load_dotenv()
# 
# SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
# SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
# SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
# 
# ## this must match the test data structure
# template_data = {
#     "total_price_usd": to_usd(total_price),
#     "human_friendly_timestamp": dt_string,
#    "products":[
#     {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#     {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#     {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#     {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#     {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#     {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#     {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#     {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#     {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#     {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#     {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#     {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#     {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#     {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#     {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#     {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#     {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#     {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#     {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#     {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# ]
# } # or construct this dictionary dynamically based on the results of some other process :-D
# 
# client = SendGridAPIClient(SENDGRID_API_KEY)
# print("CLIENT:", type(client))
# 
# message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
# message.template_id = SENDGRID_TEMPLATE_ID
# message.dynamic_template_data = template_data
# print("MESSAGE:", type(message))
# 
# try:
#     response = client.send(message)
#     print("RESPONSE:", type(response))
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# 
# except Exception as err:
#     print(type(err))
#     print(err)
# 

# A grocery store name of your choice --> DONE
# A grocery store phone number and/or website URL and/or address of choice  --> DONE
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM) --> DONE
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.) --> DONE
# The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices --> DONE
# The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax) --> DONE
# The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items --> DONE
# A friendly message thanking the customer and/or encouraging the customer to shop again --> DONE