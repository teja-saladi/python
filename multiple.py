string = input("Enter a String:")
try:
num = int(input("Enter a number:"))
print(string+num)
except TypeError as e:
print(e)
except ValueError as e:
print(e)
