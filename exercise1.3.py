numbers = [0, 0, 0]

for i in range(len(numbers)):
    while True:
        try:
            numbers[i] = input(f"Enter {i + 1} number: ")
            if numbers[i].isdigit():
                numbers[i] = int(numbers[i])
                break
        except ValueError:
            print("Error")

def sum_of_squares(numbers):
    min_value = min(numbers[0], numbers[1], numbers[2])
    
    #if (min_value == numbers[0]):
    #    print(numbers[1] * numbers[1] + numbers[2] * numbers[2])
    #elif (min_value == numbers[1]):
    #    print(numbers[0] * numbers[0] + numbers[2] * numbers[2])
    #elif (min_value == numbers[2]):
    #    print(numbers[1] * numbers[1] + numbers[0] * numbers[0])
    #else:
    #    print("Error")

    match(min_value):
        case x if min_value == numbers[0]:
            print(numbers[1] * numbers[1] + numbers[2] * numbers[2])
        case y if min_value == numbers[1]:
            print(numbers[0] * numbers[0] + numbers[2] * numbers[2])
        case z if min_value == numbers[2]:
            print(numbers[1] * numbers[1] + numbers[0] * numbers[0])
        case _:
            print("Error")

sum_of_squares(numbers)
