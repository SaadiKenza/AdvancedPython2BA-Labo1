def fact(n):
	if n<0:					#si n est négatif, on obtient une valueerror
		raise ValueError	#cette condition d'erreur doit etre définie avant le return sinon ilisible
	résultat=1
	for i in range(1,n+1):	#on crée une boucle multipliant les résultat compris entre 1(compris) et n+1(non compris)
		résultat*=i
	return résultat			#on ressort à la sortie la valeur du résultat
		
	"""Computes the factorial of a natural number.
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	pass

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
