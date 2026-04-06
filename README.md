# python-foundation-task
▎README

▎Overview

This repository contains implementations of three classic programming challenges in Python: a Prime Number Checker, a Fibonacci Sequence Generator, and a Tic-Tac-Toe game. Each implementation is designed to demonstrate fundamental programming concepts such as conditionals, loops, and object-oriented programming.

---

▎1. Prime Number Checker

▎Description

The Prime Number Checker is a function that determines whether a given integer is a prime number. A prime number is defined as a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.

▎Usage

• Call the is_prime(n: int) -> bool function with an integer n.
• The function returns True if n is prime and False otherwise.
• The script prompts the user to input a number and displays whether it is prime.

▎Example

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


---

▎2. Fibonacci Sequence Generator

▎Description

The Fibonacci Sequence Generator creates a list of Fibonacci numbers up to a specified count. The Fibonacci sequence is defined as follows: the first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding ones.

▎Usage

• Input an integer n representing how many Fibonacci numbers to generate.
• The script will output the Fibonacci sequence up to the nth number.

▎Example

n = int(input("Enter how many Fibonacci numbers you want: "))
# Output: [0, 1, 1, 2, 3, 5, ...] (depending on n)


---

▎3. Tic-Tac-Toe Game

▎Description

The Tic-Tac-Toe game is an interactive console application where two players can play against each other on a 3x3 grid. Players take turns placing their markers (X or O) in an attempt to align three of their markers either horizontally, vertically, or diagonally.

▎Usage

• Run the script, and players will be prompted to enter their moves by selecting positions numbered from 1 to 9.
• The game continues until one player wins or the game ends in a draw.

▎Example

game = TicTacToe()
game.play()


---

▎Requirements

• Python 3.x

▎How to Run

1. Clone this repository.
2. Run the desired script in your Python environment.
3. Follow the on-screen prompts for input.

▎License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as you wish!