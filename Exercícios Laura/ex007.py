try:
    tf=float(input('Digita e temperatura em Fahrenheit: '))
    tc=((5*(tf-32))/9)
    print(f'A temperatura em Célcius é de {tc}.')
except:
    print('Você deve ter digitado algo errado. Tente novamente')