#creating a function that calculates the final price after applying discount

price = int(input("original price: "))
discount_percent = int(input("discount% "))

def calculate_discount(price,discount_percent):
    if discount_percent > 20:
        y = price -(price*discount_percent/100 )
        print("new price: ", y)
    else:
        print("price:", price)

calculate_discount(price, discount_percent )