import os
import time

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def potenciacao(x, y):
    return x ** y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        print('Impossível. Divisão por zero.')

def calculadora():
    while True:
        print('-' * 20)
        print('CALCULADORA')
        print('-' * 20)
        print('1. Adição')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Potenciação')
        print('5. Divisão')
        print('6. Limpar terminal')
        print('7. Sair')

        time.sleep(1)

        operaçao = input('Informe a operação: ')
        
        try:
            operaçao = int(operaçao)

            if operaçao == 6:
                os.system('cls')
                continue

            if operaçao == 7:
                print('Encerrando a calculadora...')
                time.sleep(1)
                break
        except:
            print('Informe uma operação válida.')
            continue

        operaçoes_validas = (1, 2, 3, 4, 5, 6, 7)

        if operaçao not in operaçoes_validas:
            print('você não informou uma operação válida.')
            continue

        num1 = input('Digite um número: ')
        num2 = input('Digite um número: ')
        try:
            num1 = float(num1)
            num2 = float(num2)

            time.sleep(1)

            if operaçao == 1:
                print(f'Resultado: {soma(num1, num2)}')

            elif operaçao == 2:
                print(f'Resultado: {subtracao(num1, num2)}')

            elif operaçao == 3:
                print(f'Resultado: {multiplicacao(num1, num2)}')

            elif operaçao == 4:
                print(f'Resultado: {potenciacao(num1, num2)}')

            elif operaçao == 5:
                print(f'Resultado: {divisao(num1, num2)}')
        
        except ValueError:
            print('Digite apenas números válidos.')
            continue
        

if __name__ == '__main__':
    calculadora()