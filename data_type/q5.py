#Write a Python program to add 'ing' at the end of a given string (length should
#be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
#string length of the given string is less than 3, leave it unchanged.


def add_string(x):
  length = len(x)

  if length > 2:
    if x[-3:] == 'ing':
      x += 'ly'
    else:
      x += 'ing'

  return x
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))

