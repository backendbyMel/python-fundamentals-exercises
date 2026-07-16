#Program that asks user's name and print it in uppercase, lowercase, 
#and with only the first letter capitalized.

name = input("Enter your name: ")
print(f"Hi, {name.lower()}! Nice meeting you!")
print(f"Hi, {name.upper()}! Nice meeting you!")
print(f"Hi, {name.capitalize()}! Nice meeting you!")