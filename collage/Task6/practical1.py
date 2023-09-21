class Fraction(object):
	"""docstring for Fraction"""
	numerator=1
	denominator=1
	def __init__(self, numerator,denominator):
		super(Fraction, self).__init__()
		self.numerator=numerator
		self.denominator=denominator

	def add(self,fraction):
		if self.denominator==fraction.denominator:
			return (self.numerator+fraction.numerator),self.denominator
		else:
			n1=(self.numerator*fraction.denominator)+(self.denominator*fraction.numerator)
			n2=self.denominator*fraction.denominator
			return n1,n2

		 
	def multiply(self,fraction):
		if self.denominator==fraction.denominator:
			return (self.numerator*fraction.numerator),self.denominator
		else:
			n1=(self.numerator*fraction.denominator)*(self.denominator*fraction.numerator)
			n2=self.denominator*fraction.denominator
			return n1,n2


def main():
	obj1=Fraction(1,2)
	obj2=Fraction(3,8)

	num,deno=obj2.add(obj1)
	print(f"Addition of 1/2 + 3/8 : {num}/{deno}")

	num,deno=obj2.multiply(obj1)
	print(f"multiplication 1/2 * 3/8 : {num}/{deno}")	

main()
