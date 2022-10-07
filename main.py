import Utilities.functions
from Utilities import functions

def main():
    project_number = input('''Enter Project number for the project you want to see
                            1.Maximum of Numbers
                            2.FizzBuzz (Code determines if number is divisible by 3 or 5 and returns a corresponsding output
                             based on the number given Otherwise, it should return the same number)
                            3.Driver Speed Test
                            4.Find Odd numbers from 0 to a particular number
                            5. Sum of Multiples that are 3 and 5 
                            6. Show stars
                            7. Prime number printer....
    ''')

    for project in project_number:
        if project_number == '1':
            numbers = input('Please input the number(s) that you want to use')
            print(Utilities.functions.maximum(numbers))
        elif project_number == '2':
            entry = input('Please enter any number')
            print(Utilities.functions.fizzBuzz(entry))
        elif project_number == '3':
            speed = input('Enter current speed limit')
            print(Utilities.functions.speed_checker(speed))
        elif project_number == '4':
            entry = input('Enter number limit')
            Utilities.functions.show_numbers(entry)
        elif project_number == '5':
            limit = input('Enter the limit for the programme')
            print(Utilities.functions.sum_of_multiples(limit))
        elif project_number == '6':
            star_limit=input('Enter number of rows to print stars')
            Utilities.functions.show_stars(star_limit)
        elif project_number == '7':
            prime_number = input("""
            Enter any number to get all its prime.. """)
            Utilities.functions.prime_number(prime_number)

main()