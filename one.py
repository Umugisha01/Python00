try:

    number = int(input("Enter a number: "))

    print(f"You Entered the Number: {number}")

    print(f"Multiplication table of {number};")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

except ValueError:
    print("Please enter a valid number!")
