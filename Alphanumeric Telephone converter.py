
mapping = {
    '2': ('A','B','C'),
    '3': ('D','E','F'),
    '4': ('G','H','I'),
    '5': ('J','K','L'),
    '6': ('M','N','O'),
    '7': ('P','Q','R','S'),
    '8': ('T','U','V'),
    '9': ('W','X','Y','Z')
}

def check(character):
    for element in mapping:
        for ch in mapping[element]:
            if character == ch:
                return element

date = input('Please input 10 digit Tel number in the format XXX-XXX-XXXX ')

output =''
for item in date:
    value = check(item)
    if value is None:
        value = item
    output += value
print(output)
