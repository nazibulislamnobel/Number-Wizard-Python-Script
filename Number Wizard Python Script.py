def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def get_sum_of_odd(numbers):
    return sum([num for num in numbers if num % 2 != 0])

def get_sum_divisible_by_3(numbers):
    return sum([num for num in numbers if num % 3 == 0])

def replace_with_1s_and_0s(numbers):
    return [1 if num % 2 == 0 else 0 for num in numbers]

def swap_first_and_last(numbers):
    if len(numbers) >= 2:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers

def main():
    user_input = input("Enter numbers on the same line: ")
    numbers = [int(num) for num in user_input]

    even_numbers = get_even_numbers(numbers)
    sum_of_odd = get_sum_of_odd(numbers)
    sum_divisible_by_3 = get_sum_divisible_by_3(numbers)
    ones_and_zeros = replace_with_1s_and_0s(numbers)
    swapped_list = swap_first_and_last(numbers)

    print("List of even numbers:", even_numbers)
    print("Sum of odd:", sum_of_odd)
    print("Sum of numbers divisible by 3:", sum_divisible_by_3)
    print("New list of 1s and 0s", ones_and_zeros)
    print("List after replacing first with last:", swapped_list)

if __name__ == "__main__":
    main()