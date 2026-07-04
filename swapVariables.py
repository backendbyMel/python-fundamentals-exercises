"""
This program is about swapping variable without temporary variable"""


a = input("Input first value: ")
b = input("Input second value: ")
a,b=b,a
print(f"New value of a is: {a}")
print(f"New value of a is: {b}")