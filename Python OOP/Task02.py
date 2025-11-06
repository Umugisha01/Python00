

def generate_multiplication_table(number, start=1, end=10):

    print(f"Multiplication table of {number}:")
    for multiplier in range(start, end + 1):
        product = number * multiplier
        print(f'{number} x {multiplier} = {product}')


def get_user_input():
    
    try:
        num = int(input("Enter any number:"))
        return num
    except ValueError:
        print("Please enter any valid Integer!")
        return get_user_input()

if __name__ == "__main__":
    user_number = get_user_input()
    generate_multiplication_table(user_number)