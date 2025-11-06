s = input("enter a string:")
if s.endswith("ing"):
    s += "ly"
else:
    s += "ing"
print("modified string :", s)


