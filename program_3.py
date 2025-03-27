# Eliya Statema
# 3/27/25
# Number Total

def sum_numbers_from_file():
    file = open("numbers.txt", "r")
    total = 0
    try:
        for line in file:
            number = int(line)
            total += number
        print(f"The total of the numbers in 'numbers.txt' is: {total:,}")

    except ValueError:
        print("Invalid value found in file.")
    except IOError:
        print("An error occurred while reading the file.")

        file.close()

if __name__ == '__main__':
    sum_numbers_from_file()