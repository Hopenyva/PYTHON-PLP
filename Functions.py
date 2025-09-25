def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
       final_price = price - (price * discount_percent / 100)
       return final_price
    else:
        return price
    #Prompt user
     
    price = float(input("Please enter the original price of the item:"))
    discount_percent = float(input("Please enter the discount percent:"))
    final_price = calculate_discount(original_price, discount_percent)
    if final_price < original_price:
        print(f"Final price after {discount_percent}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")
        