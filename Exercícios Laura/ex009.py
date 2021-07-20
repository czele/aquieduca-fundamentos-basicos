try:
    n1=int(input('Digite o primeiro número inteiro: '))
    n2=int(input('Digite o segundo número inteiro: '))
    n3=float(input('Digite um número real: '))
    c1=(2*n1)*(n2/2)
    c2=(3*n1)+n3
    c3=n3**3
    print('O produto do dobro do primeiro com metade do segundo é {}. O resultado da soma do triplo do primeiro com o terceiro é {} e o terceiro número elevado ao cubo é {}'.format(c1,c2,c3))
except:
    print('Você deve ter digitado algo errado. Tente novamente')