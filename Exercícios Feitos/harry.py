'''
1 - Realize 2 inputs de números no terminal e faça com que ele imprima a seguinte frase: 
    A soma entre (1º número) e (2º número) é (resultado da soma entre eles)!
'''
print()
print('========== EXERCICIO 1 ==========')
num1 = input('Insira o primeiro Nº: ')
num2 = input('Insira o segundo Nº: ')
result = int(num1) + int(num2)
print(f'A soma entre {num1} e {num2} é {result}!')
print()


'''
2 - Realize o input de uma palavra qualquer (com mais de 4 letras) 
    e faça com que o termina escreva ela na vertical
'''
print('========== EXERCICIO 2 ==========')

while(True):
    word = input('Insira uma palavra com mais de 4 letras: ')

    try:
        int(word)
        print('ERRO: Insira uma palavra')
        print()
    except:
        if(len(word) > 4):
            for c in word:
                print(c)

            break
        else:
            print('ERRO: Palavra deve ter mais de 4 letras')
            print()

print()


'''
3 - Realize 2 inputs de números no terminal e faça com que o 2º número seja elevado ao 1º número
'''
print('========== EXERCICIO 3 ==========')

num1 = input('Insira o expoente: ')
num2 = input('Insira a base: ')
result = pow(int(num2), int(num1))
print(f'{num2} elevado a {num1} é igual a {result}')