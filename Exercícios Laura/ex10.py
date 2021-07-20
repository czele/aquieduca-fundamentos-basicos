try:
    a=float(input('Digite sua altura em centímetros: '))
    pi=((72.7*a) - 58)/1000
    # Assumi que a resposta é em gramas, mas quando insiro os valores, eles não parecem
    print('Seu peso ideal é de {} kg'.format(pi))
except:
    print('Você deve ter digitado algo errado. Tente novamente')