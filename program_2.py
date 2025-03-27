# Eliya Statema
# 3/27/25
# Random Number File Writer

import random

def generate_random_numbers(number_of_numbers):
    file = open("numbers.txt", "w")
    for _ in range(number_of_numbers):
        random_number = random.randint(1, 1001)
        file.write(str(random_number) + "\n")
    print(f"Successfully wrote {number_of_numbers} random numbers to 'numbers.txt'")

    file.close()

if __name__ == "__main__":
    while True:
        number_of_numbers = int(input("Enter the number of random numbers to generate (1-1000): "))

        if 1 <= number_of_numbers <= 1000:
            generate_random_numbers(number_of_numbers)
            break
        else:
             print("Invalid input. Please enter a number between 1 and 1000.")