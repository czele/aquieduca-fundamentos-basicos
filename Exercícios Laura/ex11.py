try:
    p=float(input('Digite seu peso em quilos: '))
    a=float(input('Digite sua altura em metros: '))
    imc=p/(a*a)
    if imc<=18.5:
        print('Você está abaixo do seu peso ideal!')
    if imc>18.5 and imc<=24.9:
        print('Você está dentre seu peso ideal!')
    if imc>24.9 and imc<30:
        print('Você está com sobrepeso!')
    if imc>=30:
        print('Você está obeso. Dá uma maneirada no chocolate!')
except:
    print('Você deve ter digitado algo errado. Tente novamente')