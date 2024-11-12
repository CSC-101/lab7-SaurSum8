import convert

#Takes an arbitrary amount of string inputs from user
#Tries to convert each input to string using convert.str_to_float
#Stores it in a list as a float, if possible, then returns the list
#at the end of execution
def gather_numbers() -> list[float]:
    x = ''
    l = []
    while x != 'done':
        x = input("Enter Value (or \'done\' to close): ")

        t = convert.str_to_float(x)

        if t is not None:
            l.append(t)

    return l

if __name__ == '__main__':
    gather_numbers()