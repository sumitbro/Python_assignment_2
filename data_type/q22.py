#Write a Python program to remove duplicates from a list.



a = [1,2,3,2,1,5,6,4,8,5,4]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)