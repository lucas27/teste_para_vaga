import os
from time import sleep

def fibonacci(valorIn):
    # listOFNumber fica com os dois primeiros números de fibonnaci
    listOfNumber = [0,1]
    
    while True:
        # já dentro do loop ele soma o último e o penultimo valor da lista
        total = listOfNumber[-1] + listOfNumber[-2]
        
        listOfNumber.append(total)

        # verifica se é igual ao número armazenado no valorIn
        if total == valorIn:
            return f'Existe na sequência de fibonacci\n{listOfNumber}'
        
        elif total > valorIn:
            return f'Não existe na sequência de fibonacci\n{listOfNumber}'

if __name__ == '__main__':
    while True:
        # uma das formas de empedir que alguem não coloque letra em vez de número        
        try:
            valorIn = int(input('Escreva um número para verificar se existe na sequência de fibonacci: '))
            os.system('cls')

            output = fibonacci(valorIn)
            print(output)

            sleep(0.8)
            
            d = input('Deseja continuar [S]im ou [N]ão:')            
            
            if d.upper() == 'S':
                os.system('cls')
                pass
            elif d.upper() == 'N':
                break

        except ValueError:
            print('por favor escreva apenas números')
