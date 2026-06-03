"""

Simple Calculator Program

"""
 
def calculator():

    print("Simple Calculator")

    print("Operations:")

    print("1. Addition (+)")

    print("2. Subtraction (-)")

    print("3. Multiplication (*)")

    print("5. Modulus (%)")

    print("6. Exponent (**)")

    print("7. Exit")
 
    while True:

        try:

            # Get user input for operation

            choice = input("Enter operation (1/2/3/4/5/6) or 'q' to quit: ")
 
            if choice.lower() == 'q':

                print("Exiting calculator. Goodbye!")

                break
 
            num1 = float(input("Enter first number: "))

            num2 = float(input("Enter second number: "))
 
            result = None
 
            if choice == '1':

                result = num1 + num2

            elif choice == '2':

                result = num1 - num2

            elif choice == '3':

                result = num1 * num2

            elif choice == '4':

                if num2 == 0:

                    print("Error! Division by zero.")

                    continue

                result = num1 / num2

            elif choice == '5':

                result = num1 % num2

            elif choice == '6':

                result = num1 ** num2

            else:

                print("Invalid input. Please try again.")

                continue
 
            print(f"Result: {num1} ', {'+' if choice == '1' else '-' if choice == '2' else '*' if choice == '3' else '/' if choice == '4' else '%' if choice == '5' else '**'} ', {num2} = {result}")
 
        except ValueError:

            print("Invalid input. Please enter a valid number.")

        except Exception as e:

            print(f"An error occurred: {e}")
 
if __name__ == "__main__":

    calculator()
 