"""
This program is about calculating the area of the rectangle
"""
import math
def get_valid_number():
    while True:
        try:
            l = float(input("Enter the length: "))
            w = float(input("Enter the width: "))
            if w < 0 or l < 0:
                print("The variable cannot be negative. It should be positive")
                continue
            return l,w
        except ValueError:
            print("Please input invalid number.")

def calculate_area(num):
    return num[0] * num[1]
 
def main():
    print("=====\nInput Length and Width to calculate the Area of the Rectangle: ")
    number = get_valid_number()
    area = calculate_area(number)

    print(f"The area of the rectangle is {area:.2f}")


if __name__ == "__main__":
    main()
