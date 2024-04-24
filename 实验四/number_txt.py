with open('C:/Users/zezr/Desktop/number.txt', 'r') as file:
    content = file.read().strip()

    numbers_str = content.strip('[]').split(',')

    numbers = [int(num.strip("'"))
               for num in numbers_str
                    if num.strip("'").isdigit()]

    numbers.sort()

print(numbers)