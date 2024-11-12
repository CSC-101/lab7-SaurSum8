import sys
import convert

#When this file runs, we iterate through the given run arguments stored as list of string
#Using convert.str_to_float, we get the float values and store them in list
#Finally, the sum of all the elements of that list is printed
if __name__ == "__main__":
    l = []

    for i in sys.argv:
        x = convert.str_to_float(i)
        print(i)
        if x is not None:
            l.append(x)

    s = sum(l)
    print(s)
