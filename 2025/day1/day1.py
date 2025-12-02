
from input import input

def day1():
    number = 50
    zero_count = 0
    for direction in input:
        if direction[0] == 'L':
            number = (number+100-int(direction[1:])) % 100
        else:
            number = (number + int(direction[1:])) % 100
        if number == 0:
            zero_count += 1
    print(zero_count)

# day1()

def day2():
    number = 50
    zero_count = 0
    for direction in input:
        if direction[0] == 'L':
            new_number = number - int(direction[1:])
            if new_number <= 0:
                zero_count += new_number//-100 + (1 if number != 0 else 0)
            number = new_number % 100
        else:
            new_number = (number + int(direction[1:]))
            if new_number >= 100:
                zero_count += new_number//100
            number = new_number % 100
        print(f"{number}, {zero_count}")
    print(zero_count)

day2()