'''
6. Create class complex with members real and imaginary and create a method for addition
and multiplication of two complex numbers.
'''

class Complex():
    def __init__(self,real=0.0,imaginary=0.0):
        self.real=real
        self.imaginary=imaginary

    def add(self,n1,n2):
        self.real=n1.real+n2.real
        self.imaginary=n1.imaginary+n2.imaginary
        return Complex(self.real,self.imaginary)
    
def main():
    n1=Complex(20,1)
    n2=Complex(30,1)
    temp=Complex()
    temp=temp.add(n1,n2)

    print('Real: ',temp.real)
    print('imaginary: ',temp.imaginary)

main()

        
