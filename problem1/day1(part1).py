# https://adventofcode.com/2015/day/1
# my input must be read from input.txt 
my_input = ""
balance = 0

for char in my_input:
    if char == "(":
        balance = balance + 1
    elif char == ")":
        balance = balance - 1

print(balance)
