def isFib(n):
	def is_perfect_square(x):
		s = int(x**0.5)
		return s * s == x

	# o numero pertence a sequencia se: 
	# (5*n^2 + 4) ou (5*n^2 - 4) é um quadrado perfeito
	def checkFib(n):
		return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

	# checar valor negativo
	if (n < 0):
		return False


	if checkFib(n):
		return f"{n} está na sequência de Fibonacci."
	else:
		return f"{n} não está na sequência de Fibonacci."


# entrada
num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(isFib(num))
