#Write a Python program to get a single string from two given strings, separated
#by a space and swap the first two characters of each string.

def chars(x, y):
  new_x = y[:2] + x[2:]
  new_y = x[:2] + y[2:]

  return new_x + ' ' + new_y
print(chars('abc', 'xyz'))



