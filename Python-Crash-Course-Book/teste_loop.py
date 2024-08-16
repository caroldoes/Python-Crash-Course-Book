n = int(input('Digite um número inteiro '))

texto = f' A tabuada de {n} equivale a:\n'

for multiplicador in range(1,11):
    resultado = n * multiplicador 
    texto += f'{n} x {multiplicador} = {resultado}\n'

print(texto)
  