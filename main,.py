import random

def check_if_number_complies_with_requirements(number_to_check: str) -> bool:
    ''' 
    This function checks if given number meets specific criteria
    
    Requirements:
    - Must be a four digit number
    - All digits must not be the same (at least two different digits)
    '''

    try:
        digits_list = [int(digit) for digit in number_to_check]
        if len(digits_list) != 4:
            print("⚠️  Length is not 4")
            return False
        if len(set(digits_list)) < 2:
            print("⚠️  Number needs to contain at least two different digits")
            return False
        return True
    except:
        print("⚠️  You didn't give me a number consisting of at least different digits")
        return False


def apply_Kaprekar_algorithm(given_number: str, iterator_counter = 1) -> int:
    digits_list = [int(digit) for digit in given_number]

    sorted_digits_list = list(digits_list) #.sort()
    sorted_digits_list.sort()
    # print(sorted_digits_list)
    sorted_number = 1000*sorted_digits_list[0] + 100*sorted_digits_list[1] + 10*sorted_digits_list[2] + sorted_digits_list[3]

    reverse_sorted_digits_list = list(digits_list)
    reverse_sorted_digits_list.sort(reverse=True)
    # print(reverse_sorted_digits_list)
    reverse_sorted_number = 1000*sorted_digits_list[3] + 100*sorted_digits_list[2] + 10*sorted_digits_list[1] + sorted_digits_list[0]

    diff_result = reverse_sorted_number - sorted_number
    print(f"> Result of #{iterator_counter} diff is {diff_result}")


    if diff_result == 6174:
        print(f"ℹ️  Reached Kaprekar's constant 6174 in {iterator_counter} iterations ℹ️")
    else:
        iterator_counter += 1
        apply_Kaprekar_algorithm(str(diff_result), iterator_counter = iterator_counter)
    pass

def main():
    given_number = input("Enter a four digit positive number with at least two different digits or pass RAND in order to choose number randomly: ")

    if given_number.upper() == "RAND":
        while True:
            given_number = str(random.randint(1000, 9999))
            if check_if_number_complies_with_requirements(given_number):
                print(f"Randomly chosen number is {given_number}")
                break

    if check_if_number_complies_with_requirements(given_number):
        apply_Kaprekar_algorithm(given_number)
    else:
        print(f"❗Given number {given_number} does not meet the requirements.❗")


if __name__ == "__main__":
    main()