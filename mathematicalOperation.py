"""
Simple Calculator using match-case.
"""

def calculate(operation, first_number, second_number):
    match operation:
        case "addition":
            return first_number + second_number

        case "subtraction":
            return first_number - second_number

        case "multiplication":
            return first_number * second_number

        case "division":
            if second_number == 0:
                return "Error: Division by zero is not allowed."
            return {
                "quotient": first_number / second_number,
                "remainder": first_number % second_number,
            }

        case _:
            return "Invalid operation."


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=== Simple Calculator ===")

    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    operation = input(
        "Choose an operation (addition, subtraction, multiplication, division): "
    ).strip().lower()

    result = calculate(operation, first_number, second_number)

    print(f"\nResult: {result}")


if __name__ == "__main__":
    main()