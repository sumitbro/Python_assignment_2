#Write a Python program to count the number of characters (character
#frequency) in a string. Sample String : google.com'

def character(string):
	    dict = {}
	    for n in string:
	        keys = dict.keys()
	        if n in keys:
	            dict[n] += 1
	        else:
	            dict[n] = 1
	    return dict
print(character('google.com'))
















