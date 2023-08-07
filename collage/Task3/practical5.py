# Write a Python program to Print those numbers which are divisible by 7 and
# multiple of 5, between 1500 and 2700 (both included), also print total of such
# numbers.

for i in range(1500,2700):
    if i%7==0 and i%5==0:
        print(i,end=" ")