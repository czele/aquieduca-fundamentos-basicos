import statistics

n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
n3=float(input('Digite a terceira nota: '))
n4=float(input('Digite a quarta nota: '))

print('A média entre as quatro notas é: {}'.format(statistics.mean([n1, n2, n3, n4])))

