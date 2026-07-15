"""
Verify if the number is positive, negative or zero.
"""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please input number only.")

def verify_number(prompt):
    if prompt > 0:
        return f'{prompt} is a positive number'
    elif prompt < 0:
        return f'{prompt} is a negative number'
    else:
        return f'{prompt} is neither positive nor negative.'

def main():
    print("===Input a number to check if it is positive, negative or zero.====")

    num = get_number("Enter a number: ")
    result = verify_number(num)
    print(result)

if __name__ == "__main__":
    main()