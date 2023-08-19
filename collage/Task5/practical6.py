'''
Take two values of feet and inches from user. Create a function to add the values of feet 
with feet and inch with inch. Display the valid total result. (Inch should not be more than 11)
'''

def sumFitInch(feet1,feet2,inch1,inch2):
    Sumfeet=feet1+feet2
    SumInchs=inch1+inch2
    return Sumfeet,SumInchs

feet1=int(input("Enter value of Feet 1: "))
feet2=int(input("Enter value of Feet 2: "))
inch1=int(input("Enter value of Inch 1: "))
inch2=int(input("Enter value of Inch 2: "))


totalFeets,totalInchs=sumFitInch(feet1=feet1,feet2=feet2,inch1=inch1,inch2=inch2)
print(f"Feets: {totalFeets} \nInchs: {totalInchs}")