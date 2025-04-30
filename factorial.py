#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Apr. 29, 2025
# This program calculates the factorial of a
# whole number entered by the user.


# Define the main function.
def main():
    # Initialize the loop counter to 0.
    loop_counter = 0
    # Initialize the factorial answer to 1.
    factorial_answer = 1
    # Get the whole number from the user as a string.
    user_number_str = input("\nEnter a whole number: ")

    # Try to check the validity of the user input.
    try:
        # Attempt to convert the entered string into an integer.
        user_number_int = int(user_number_str)

        # Check if the entered integer is a whole number.
        if user_number_int >= 0:
            # Proceed to the workaround do..while loop for
            # determining the factorial of the whole number.
            while True:
                # Increment the loop counter by one.
                loop_counter = loop_counter + 1
                # Multiply the factorial answer by the loop counter.
                factorial_answer = factorial_answer * loop_counter

                # Check if the loop counter is greater than or
                # equal to the user's entered whole number.
                if loop_counter >= user_number_int:
                    # Break the while loop to
                    # simulate the do..while.
                    break
            # Display the resulting factorial answer.
            print(f"\n{user_number_int}! = {factorial_answer}.")

        # Otherwise, the user entered a negative integer.
        else:
            # Display to the user that they
            # did not enter a whole number.
            print(f"\n{user_number_int} is not a whole number.")

    # Runs if int() could not convert the user's string
    # input into an integer.
    except ValueError:
        # Display to the user that they
        # did not enter a whole number.
        print(f"\n{user_number_str} is not a whole number.")

    # Finally, run the exit message.
    finally:
        # Thank the user for using this program.
        print("\nThanks for using this program!")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
