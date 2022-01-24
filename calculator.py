#!/usr/bin/env python3

# Created by: Logan S
# Created on: Jan. 24, 2022
# This program calculates.
import math


def calculate(sign, number_1, number_2):

    # Calculate the equation with whichever operator
    if sign == "+":
        return number_1 + number_2
    elif sign == "-":
        return number_1 - number_2
    elif sign == "x" or sign == "*":
        return number_1 * number_2
    elif sign == "/" or sign == "÷":
        return number_1 / number_2
    elif sign == "%":
        return number_1 % number_2
    else:
        return "invalid (Invalid operator)"


def main():

    # Get user input
    user_num_1 = input("Enter your first number: ")
    user_num_2 = input("Enter your second number: ")
    user_sign = input("Enter you Operator (Sign): ")
    print()

    # Error checking
    try:
        num_1_float = float(user_num_1)
        num_2_float = float(user_num_2)

        solution = calculate(user_sign, num_1_float, num_2_float)
        print()
        print("The answer is {:.2f}".format(solution))
    except Exception:
        print("The answer is invalid (Invalid numbers)")


if __name__ == "__main__":
    main()
