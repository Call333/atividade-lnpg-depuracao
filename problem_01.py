def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Error: na linha 14 e 15, antes estava com o tipo int e agora está com o tipo float.
def get_numbers():
    numbers :float = input("Enter numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    return numbers

def main():
    numbers : float = get_numbers()
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_max(numbers))

if __name__ == "__main__":
    main()