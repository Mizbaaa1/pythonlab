user_input = input("Enter first names separated by commas: ")
names = [name.strip() for name in user_input.split(',')]
count = 0
for name in names:
    count += name.lower().count('a')
    print("total occurrences of 'a':", count)



