#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2020
# This program shows formatting output


def main():
    # this function shows formatting output

    # input
    year = int(input("Enter a year (Positive): "))

    # process & output
    if year %4 == 0:
        if year %100 == 0:
            if year % 400 == 0:
                print("It is a leap year")
            else:
                print("It is not a leap year")
        else:
            print("it is a leap year")
    else:
        print("It is not a leap year")
    print("\nDone.")


if __name__ == "__main__":
    main()
