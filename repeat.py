#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Oct 2020
# This program print the users string using a loop


def main():

    # this function has a loop

    # this is to keep track of the loop
    loop_counter = 1

    # input
    user_string = input("Enter a string (ex. hello) : ")
    times_repeated_as_string = input("How many time you would like it to repeat : ")
    print("")

    # process
    try:
        times_repeated = int(times_repeated_as_string)
        if times_repeated > 0:
            for loop_counter in range(times_repeated):
                if loop_counter % times_repeated == times_repeated:
                    print("{0}".format(user_string))
                    loop_counter = loop_counter + 1
                else:
                    print("{0}".format(user_string), end="")
        else:
            print("Negative number entered, please try again.")
    except Exception:
        print("Invalid input entered, please try again.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
