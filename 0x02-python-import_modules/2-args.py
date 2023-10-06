#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenght = len(sys.argv)
    if 1 >= lenght:
        print('0 arguments.')
    elif 2 == lenght:
        print('1 argument:')
    else:
        print('{} arguments:'.format(lenght - 1))
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        else:
            print("{}:".format(i), "{}".format(arg))
