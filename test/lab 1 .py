# Simple Calculator with History

history = []

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero!"
    return x % y

def show_history():
    if not history:
        print("No calculations yet.")
    else:
        print("\n--- Calculation History ---")
        for record in history:
            print(record)
        print("---------------------------")

def clear_history():
    history.clear()
    print("History cleared.")

def main():
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Show History")
        print("7. Clear History")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"
            elif choice == '5':
                result = modulus(num1, num2)
                operation = f"{num1} % {num2} = {result}"

            print("Result:", result)
            history.append(operation)

        elif choice == '6':
            show_history()

        elif choice == '7':
            clear_history()

        elif choice == '8':
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option (1-8).")

if __name__ == "__main__":
    main()
