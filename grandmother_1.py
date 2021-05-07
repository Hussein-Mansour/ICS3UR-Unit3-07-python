#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Fri/May7/2021
# This program is grandmother age checker


def main():
    # this function checks if the age is accepted or not

    # input
    age_string = input("please enter your age:")

    # process  & output
    try:
        age_input = int(age_string)

        if (age_input >= 25 and age_input <= 40):
            print("your accepted to date my grandchild.")
        elif (age_input > 40):
            print("You are too old!")
        else:
            print("you are too young, come back later when you are older")
    except Exception:
        print("{},is not vaild input.".format(age_string))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
