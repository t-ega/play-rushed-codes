def maximum(numbers):
    list_numbers = []
    numbers = numbers.split(' ')
    for i in numbers:
        numbers = int(i)
        list_numbers.append(numbers)
    max = list_numbers[0]
    for number in list_numbers:
        if max < number:
            max = number

    return max

def fizzBuzz(input):
    input=int(input)
    if input%3 ==0 and input%5 ==0:
        return 'FizzBuzz'
    elif input%3 ==0:
        return 'Fizz'
    elif input%5 ==0:
        return 'Buzz'
    else:
        return input

def speed_checker(speed):
    speed=int(speed)
    speed_limit=70
    demerit_points=0
    demerit=(speed-speed_limit)

    if speed <= speed_limit:
        return 'Speed is Okay'
    elif speed > speed_limit:
        demerit_points = (demerit//5)
        print('Loading...')
        print('Checking if point is above 12')
        if demerit_points>12:
            print(f'Points:{demerit_points}')
            return 'License has been suspended'
        else:
            print(f'Points:{demerit_points}')
            return 'Okay good to go'

def show_numbers(limit):
    limit=int(limit)
    for number in range(limit+1):
        if number%2 == 0:
            number_value='EVEN'
            print(f'{number} {number_value}')
        else:
            number_value='ODD'
            print(f'{number} {number_value}')


def sum_of_multiples(limit):
    limit = int(limit)
    multiple = []
    sum = 0
    for i in range(limit+1):
        if i % 3 == 0:
            multiple.append(i)
        elif i % 5 == 0:
            multiple.append(i)
    for element in multiple:
            sum += element
    return sum

def show_stars(rows):
    rows=int(rows)
    for star in range(rows+1):
        print('*'*star)

def prime_number(number):
    number=int(number)
    prime_list=[]
    for prime in range(number + 1):
        if prime % 2 == 1:
            prime_list.append(prime)
            print(prime)
















