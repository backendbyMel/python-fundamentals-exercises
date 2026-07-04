"""
Temperature converter 
1. Celcius to Farenheit
2. Farenheit to Celcius
"""

def convert_temp(operation, num):
    match operation:
        case 1:
            return (num * 1.8) + 32
        case 2:
            return (num  - 32) * (5/9) 

def get_operation(prompt):
    while True:
        try:
            operation = int(input(prompt))

            if operation in (1, 2):
                return operation

            print("Please choose 1 or 2.")

        except ValueError:
            print("Invalid input.")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("=== TEMPERATURE CONVERTER ====")

    operation = get_operation(
        "Choose an operation \n " \
        "type 1 to convert from Celcius to Farenheit" \
        "\n type 2 to convert from Farenheit to Celcius: "
    )

    user_input = get_number("Enter the number: ")
    result = convert_temp(operation, user_input)
    if operation == 1:
        print(f"{user_input:.2f} °C = {result:.2f} °F")
    else:
        print(f"{user_input:.2f} °F = {result:.2f} °C")
    
if __name__ == "__main__":
    main()