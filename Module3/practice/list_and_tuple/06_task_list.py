first_number = int(input())  # Первое число
second_number = int(input())  # Второе число

first_number= (first_number//3+1)*3

while first_number <= second_number:
    print(first_number)
    first_number += 3
