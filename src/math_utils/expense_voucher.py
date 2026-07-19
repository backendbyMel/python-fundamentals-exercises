"""
A console tool 
for junior clerks to input employee expenses 
and generate a standardized, formatted summary 
for reimbursement
"""
VAT_RATE = 0.12

def calculate_tax(base_price):
    """
    Calculate the VAT tax and added it on the base price
    """
    vat = VAT_RATE * base_price
    price_tax = vat + base_price
    return vat, price_tax

def input_validation(prompt, constructor):
    """
    Verify if the input is number.
    """
    while True:
        try:
            return constructor(input(prompt))
        except ValueError:
            print("Please input number only")


def main():
    """
    Main function that gets all the user input
    """
    employee_name = input("Enter your name: ")
    number_of_items = input_validation("Enter how many items: ", int)
    total_price = 0
    expenses = []
    for i in range(number_of_items):
        item_name = input("Enter item name: ")
        item_price = input_validation("Enter the price: ", float)
        tax = calculate_tax(item_price)
        expenses.append({"Name":item_name, "Base Price": item_price, "VAT":tax[0], "Price With Tax": tax[1]})
    
    print(f"Voucher for : {employee_name}")
    print("-" * 60)
    print(f"{'Item':<20} {'Base':>10} {'VAT':>10} {'Total':>12}")
    print("-" * 60)
    for item in expenses:
        print(
            f"{item['Name']:<20}"
            f"{item['Base Price']:>10.2f}"
            f"{item['VAT']:>12.2f}"
            f"{item['Price With Tax']:>12.2f}"
        )
        total_price += item["Price With Tax"]
    
    print(f"The total price is: {total_price:>35.2f}")
    
        
        
if __name__ == "__main__":
    main()
