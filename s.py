"""
# A tech based slot machine
# Complex project
# We need to collect the users deposit, add that to their balance
# We need to allow them to bet on a line or on multiple lines
# We need to generate the slot machines, so it can spin
# We need to generate the different items that are going to be in the slot machine

# A user will deposit a certain amount of money
# We're going to allow them to bet on 1, 2 ,3 lines of the slot machines
# We will determine if they won and if they did we're going to multiple their bet by the values of the line
# Add that to their balances and then allow them to keep playing until they want to cash out or run out of money

# First step
# Collecting some user input
# We need to get the deposit that the user's entering as well as their bet
"""

import random


# This is a global constant
# This is a constant value that will never change
# All caps means constant
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Generate what symbols are going to be in each column
# Based on the frequency of symbols that we have here
# Randomly pick a number
# When using items it gives you the keys and the values associated with a dictionary
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
# STEP 1
# def deposit():
# This is a function that we can call that's going to execute a certain block of code
# That can potentially return us a value

# while True:
# The while statement takes an expression and executes the loop body while the expression evaluates to (boolean) "true"
# "True" always evaluates to boolean "true" and thus executes the loop body indefinitely
# We need a while loop because we're going to continually ask the user a deposit amount until it's a valid amount

# isdigit() is a Python string method
# Checks if all the characters in the text are digits
# Returns true if all the characters are digits, otherwise ise FALSE
# LOGIC we need to check to make sure it's a digit, because they can type any answer

# break
# break will allow for us to break away from the while loop and move on to the conditional statements

# return statement is like a print statement where we can use the number that is correct from the while loop
# Thous returning the value we need back to the amount variable
welcome = input("Hello, welcome to the slot machine.")

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# STEP 2
# This will collect the bet from the user
# This will determine how much they want to bet and how many lines they want to bet on
# Then I will multiply their bet amount by the numbers of lines
# Checking a value in between something is like this  if 1 <= lines <= MAX_LINES:
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
