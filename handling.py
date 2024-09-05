num=int (input ("Numerator: "))
deno=int(input("Denominator:"))
try:
 quo=num/deno
print("QUOTIENT: ",quo)
except ZeroDivisionError:
print("Denominator can’t be zero")
