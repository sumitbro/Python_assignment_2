#Write a Python function to find the Max of three numbers.


def max_num(a,b,c):
    if a>b & a>c:
        print("a is maximum number",a)
    elif b>a & b>c:
        print("b is maximum", c)
    else:
        print("c is maximum number", c)

print(max_num(2,3,4))
