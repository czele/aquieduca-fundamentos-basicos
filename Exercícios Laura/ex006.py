try:
    ch=int(input('Quanto que você ganha por hora: '))
    ht=int(input('Quanto você trabalhou este mês: '))
    tt=ch*ht
    print('Seu salário mensal foi {}'.format(tt))
except: 
    print('Você deve ter digitado algo errado. Tente novamente')