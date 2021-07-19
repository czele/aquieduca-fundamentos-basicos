try:
    c=float(input('Digite a medida centímetros: '))
    print('A medida em metros é: {}'.format(c*0.01))
except: 
    print('Você deve ter digitado algo errado. Tente novamente')