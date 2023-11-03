#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, add, mul, div

    a = 10 
    b = 5
    result_subtract = subt(a, b)
    result_add = add(a, b)
    result_multiply = mul(a, b)
    result_divide = div(a, b)

    print("{:d} - {:d} = {:d}".format(a, b , sub(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div`(a, b)))
