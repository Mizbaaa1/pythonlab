nums = list(map(int,input("enter numbers seperated by spaces:").split()))
odds = [n for n in nums if n % 2 != 0]
print("list after removing even numbers :",odds)
