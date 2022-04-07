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
                    print("It is a leap year".format(user_input_string))
                else:
                    print("It is not a leap year".format(user_input_string))
            else:
                print("It is a leap year.".format(user_input_string))
                print("")
        else:
            print("It is a common year.".format(user_input_string))
            print("")

    except Exception:
        print("Really? (-_-)ゞ゛pick a year pls.".format(user_input_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
