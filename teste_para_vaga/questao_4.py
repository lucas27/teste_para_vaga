def calculo_percentual():
    # fiz dessa forma pra ser mais fácil de visualizar os estados e os valores
    dados = [
        {'estado': 'SP', 'valor': 67836.43},
        {'estado': 'RJ', 'valor': 36678.66},
        {'estado': 'MG', 'valor': 29229.88},
        {'estado': 'ES', 'valor': 27165.48},
        {'estado': 'Outros', 'valor': 19849.53}
    ]

    # Calcula o valor total usando list comprehension
    valor_total = sum([i['valor'] for i in dados])

    # Calcula e imprime o percentual de cada estado
    for dado in dados:
        porcentagem = (dado['valor'] / valor_total) * 100
        print(f"{dado['estado']}, porcentagem: {porcentagem:.2f}%")
    
if __name__ == '__main__':
    calculo_percentual()