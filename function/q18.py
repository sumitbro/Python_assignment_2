#Write a Python program to check whether a given string is number or not
#using Lambda.


is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26'))
print(is_num('4.2'))
print(is_num('-147'))
print(is_num('0'))
print(is_num('A1'))
print(is_num('01'))
print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))