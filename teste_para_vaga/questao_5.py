def inverter_string(string):
    string_invertida = string[::-1]
    print(string_invertida)
    

if __name__ == '__main__':
    
    string = input('digite uma string: ')
    
    # para aceitar apenas letras
    if string.isalpha():
        inverter_string(string)
    else:
        print('escreva apenas letras')