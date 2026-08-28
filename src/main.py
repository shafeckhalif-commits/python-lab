
from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    user_name = input("Enter your name: ")
    print(greet(user_name))


    num = float(input("Enter a number: "))
    print(f"Square of {num}: {square(num)}") 
    print(f"Is {num} even? {is_even(num)}")
    print(f"{num}°C in Fahrenheit: {celsius_to_fahrenheit(num)}°F")

main()

