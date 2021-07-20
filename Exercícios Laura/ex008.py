try:
    tc=float(input('Digita e temperatura em Celcius: '))
    tf=tc*1.8+32
    print(f'A temperatura em Fahrenheit é de {tf}.')
except:
    print('Você deve ter digitado algo errado. Tente novamente')