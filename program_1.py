# Eliya Statema
# 3/27/25
# Item Counter

def count_file_lines():
    file = open("names.txt", "r")
    name_count = len(file.readlines())
    print(f"The file 'names.txt' contains {name_count} names.")

    file.close()

if __name__ == '__main__':
    count_file_lines()

