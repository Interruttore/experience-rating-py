from os import name, system


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def print_menu(arg):
    print(30 * "-", "MENU", 30 * "-")
    if(arg == "main"):
        print("1. Search movie")
        print("0. Exit program")
    elif(arg == "movie_search"):
        print("1. Search movie")
        print("2. Repeat search with more result if possible")
        print("3. Add movie to excel")
        print("0. Back")
    elif(arg == "movie_add"):
        print("1. Add another movie")
        print("0. Back")
    print(67 * "-")


def check_input(input, rangeStart, rangeEnd):
    try:
        temp = int(input)
        if(temp >= rangeStart and temp <= rangeEnd):
            return temp
        else:
            return -1
    except ValueError:
        return -1


def joiner(title, release_date, genres):
    complete = title + '    ' + release_date + \
        '    '
    for j in genres[:2]:
        complete += j + '/'

    complete = complete[0:-1]
    return complete


def getIndex(sheet):
    i = 0
    index = 0
    for value in sheet.iter_rows(min_row=3, min_col=1, max_col=1, values_only=True):
        if(value[0] != None):
            i += 1
        else:
            index = i+3
            break
    return index
