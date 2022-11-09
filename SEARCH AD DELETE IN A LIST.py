import random

# ( -> list ) is just to show that this function should return a list
def create_rand_list() -> list:
    # create the number of elements as required by the instructor
    num_of_elements = random.randint(5, 15)
    # get a minimum value for the minimum range as required
    min_value = random.randint(5, 10)
    # get a maximum value for the maximum range as required
    max_value = random.randint(20, 50)
    # create an empty list to hold the random numbers that would be generated
    rand_list = []
    # a for loop that would run with the number if elements as the stopping value
    for i in range(num_of_elements):
        # getting a random number between the range gotten from line 38 and 40
        value = random.randint(min_value, max_value)
        # appending the value i.e. the random number generated between the range gotten from above to the list in
        # line 42
        rand_list.append(value)
        # returning the list
    return rand_list

# ( -> None ) is just to show that this function should not return any value

def print_list(rand_list) -> None:
    if rand_list:
        print('---list---')
        print(rand_list)
    else:
        print('---list---')
        print('Empty')


# ( -> int ) is just to show that this function should return an integer
def delete_item_from_list(rand_list, item) -> int:
    if item in rand_list:
        index = rand_list.index(item)
        rand_list.remove(item)
        return index
    else:
        return -1


again = 'y'
while again == 'y':
    random_list = create_rand_list()
    print_list(random_list)
    item = int(input('What item would you wish to delete from the list? '))
    delete = delete_item_from_list(random_list, item)
    if delete != -1:
        print(f'Successful! Item found in index {delete} of the list')
    else:
        print('Item not found!')
    again = input('Do you want to try again?')
    # converting it to lower is safer because what if the user types with caps on?
    again = again.lower()
