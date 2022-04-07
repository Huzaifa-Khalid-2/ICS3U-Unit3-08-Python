#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# this function checks if the year inserted by user
# is a leap year


def main():
    # this function checks if the year inserted by user
    # is a leap year

    # input
    user_input_string = input("Enter the number of the year (integer): ")
    print("")

    # process and output
    try:
        user_input_number = int(user_input_string)
        if user_input_number % 4 == 0:
            if user_input_number % 100 == 0:
                if user_input_number % 400 == 0:
                    print("It is a leap year")
                else:
                    print("It is not a leap year")
            else:
                print("It is a leap year.")
                print("")
        else:
            print("It is a common year.")
    except Exception:
        print("Really? (-_-)ゞ゛pick a year pls.")
    print("\nDone.")


if __name__ == "__main__":
    main()
