import datetime


input_file = open('input.txt', 'r')
global possible_dates
possible_dates = []


def if_valid_date(year, month, day):
    valid_state = None
    if year < 2000:
        year += 2000
    try:
        newDate = datetime.datetime(year, month, day)
        valid_state = True
    except ValueError:
        valid_state = False
    return valid_state


def add_date(year, month, day):
    global possible_dates
    if if_valid_date(year, month, day):
        possible_dates.append([year, month, day])


def get_min_date(list_of_dates):
    min = list_of_dates[0]
    for date in list_of_dates:
        if date < min:
            min = date
    return min


# Get variables from input file and save input line
for line in input_file:
    input_line = line
    items = line.split('/')
x = int(items[0])
y = int(items[1])
z = int(items[2])


# Check all possible date combinations and add them to list
add_date(x, y, z)
add_date(x, z, y)
add_date(y, x, z)
add_date(y, z, x)
add_date(z, x, y)
add_date(z, y, x)


if (possible_dates):
    min_date = get_min_date(possible_dates)
    if min_date[0] < 2000:
        min_date[0] += 2000
    print('%i-%i-%i' % (min_date[0], min_date[1], min_date[2]))
else:
    print(input_line + ' is illegal')
