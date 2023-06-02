# Compulsory Task 1
# Follow these steps:
# ● Create a simple calculator application that asks a user to enter two
#   numbers and the operation (e.g. +, -, x, etc.) that they’d like to perform on
#   the numbers. Display the answer to the equation. Every equation entered
#   by the user should be written to a text file. Use defensive programming to
#   write this program in a manner that is robust and handles unexpected
#   events and user inputs.
# ● Now extend your program to give the user the option to either enter two
#   numbers and an operator, like before, or to read all of the equations from a
#   new txt file (the user should add the name of the txt file as an input) and
#   print out all of the equations together with the results. Use defensive
#   coding to ensure that the program does not crash if the file does not exist
#   and that the user is prompted again to enter the name of the file.

print("Calculator\n")
# User open a txt file
while True:
    try:
        filename = input("Please enter the name of your txt file with ending .txt: ")
        if not filename.lower().endswith(".txt"):
            print("File name not end with .txt, please enter again.")
            continue

        else:
            # User need to choose whether calculate or read file
            while True:
                try:
                    with open(filename.lower(), 'a') as f:
                        option = input("Enter calculator or read file?(cal/file): ")
                        # When user choose to use calculate
                        if option.lower() == "cal":
                            while True:
                                # Use defensive programming to handle any input error
                                try:
                                    x = float(input("Please enter the first number: "))
                                    y = float(input("Please enter the second number: "))
                                    z = input("Please enter the operator(+,-,*,/): ")

                                    if z == '+':
                                        answer = x + y
                                    elif z == '-':
                                        answer = x - y
                                    elif z == '*':
                                        answer = x * y
                                    elif z == '/':
                                        answer = x / y
                                    else:
                                        print("Invalid operator, please try again!")
                                        continue

                                    print(f"Your equation is {x} {z} {y} = {answer}")
                                    f.write(f"Your equation is {x} {z} {y} = {answer}\n")
                                    break

                                except ValueError:
                                    print("Invalid input, please enter again")
                                except ZeroDivisionError:
                                    print("Cannot divide by zero, please enter again")
                                except KeyboardInterrupt:
                                    print("\nProgram terminated, goodbye!")
                                    exit()
                        # When user choose to read file
                        elif option.lower() == "file":
                            while True:
                                # Use defensive programming to handle any input error
                                try:
                                    file = input("Enter the name of the file: ")
                                    with open(file.lower(), 'r') as f:
                                            equations = f.read()
                                            print(equations)
                                            break
                                except FileNotFoundError:
                                    print("File not found. Please try again.")
                                except KeyboardInterrupt:
                                    print("\nProgram terminated, goodbye!")
                                    exit()
                        else:
                            print("Invalid input, please enter again")

                except IOError:
                    print("Error: the file could not be opened or written to.")
                    exit()
                except KeyboardInterrupt:
                    print("\nProgram terminated, goodbye!")
                    exit()
    except KeyboardInterrupt:
        print("\nProgram terminated, goodbye!")
        exit()