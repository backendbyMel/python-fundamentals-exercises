"""
Polymorphic adder that works on any objects supporting '+'.
"""

def add_stuff(a, b):
    try:
        return a + b
    except TypeError:
        print(f"Error: Cannot add {type(a).__name__} and {type(b).__name__}.")
        return None

# Test Cases
print(add_stuff(1, 2.5))        
print(add_stuff('spam', ' eggs')) 
print(add_stuff('spam', 42))    