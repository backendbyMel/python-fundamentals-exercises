"""
This program is about calculating the area of the circle
"""
import math

def calculate_area(r):
    try:
        area = math.pi * (r**2)
        return area
    except ValueError:
        print("Invalid input. Please enter a number.")
 
def main():
    print("=====\nInput Radius to calculate the Area of the Circle: ")
    area = calculate_area(float(input("Enter a number: ")))
    print(f"The area of the circle is: {round(area,2)}")

if __name__ == "__main__":
    main()
