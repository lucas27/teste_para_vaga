import json
       
with open('dados.json') as arquivo:
    dados = json.load(arquivo)

def menor_faturamento(dados, lista):
    # armazena o valor mínimo
    menor_valor = min(lista)

    for dado in dados:
        # ele compara é retorna o dia e o valor
        if dado['valor'] == menor_valor:
            return dado
            
def maior_faturamento(dados, lista):
    # armazena o valor máximo
    maior_valor = max(lista)
    
    for dado in dados:
        # ele compara é retorna o dia e o valor
        if dado['valor'] == maior_valor:
            return dado

def faturamento_superior_mensal(dados, lista):
    # faz a média
    media = sum(lista) / len(lista)

    contador = 0
    # conta o número de dias que tiveram o valor maior que a média
    for dado in dados:
        if dado['valor'] > media:
            contador += 1
    return contador

if __name__ == '__main__':
    # uma forma reduzida usando list comprehension para armazena os valores e removendo o zero 
    lista = [i['valor'] for i in dados if i['valor'] > 0]

    menor = menor_faturamento(dados, lista)
    maior = maior_faturamento(dados, lista)
    dia_superior = faturamento_superior_mensal(dados, lista)

    print(f"O menor faturamento foi no dia {menor['dia']} com valor de {menor['valor']:.2f}")
    print(f"O maior faturamento foi no dia {maior['dia']} com valor de {maior['valor']:.2f}")
    print(f'foram {dia_superior} dias')