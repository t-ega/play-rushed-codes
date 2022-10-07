def month_converter(date):
    date = date.split('-')
    months={
        '01':'January',
        '02': 'Febuaray',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    output = ''
    for character in date:
        output += months.get(character, character) +' '
    print(output)

