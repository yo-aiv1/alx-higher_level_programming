#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        rslt = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        rslt = None

    return (rslt)
