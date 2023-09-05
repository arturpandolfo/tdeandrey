def uniao(set1, set2):
    return set1.union(set2)


def interseccao(set1, set2):
    return set1.intersection(set2)


def diferenca(set1, set2):
    return set1.difference(set2)


def produto_cartesiano(set1, set2):
    return {(x, y) for x in set1 for y in set2}


while True:
  operacao = input("Digite a operação que será realizada (U,I,D,C, 0 para sair)")
  variavel = operacao.upper()
  if operacao == "0":
    break
  set1 = set(input("Digite os elementos do primeiro conjunto separados por virgula: ").split(","))
      
  set2 = set(input("Digite os elementos do segundo conjunto separados por virgula: ").split(","))

  if operacao == 'U':
        resultado = uniao(set1, set2)
        operacao_descricao = "União"
  elif operacao == 'I':
        resultado = interseccao(set1, set2)
        operacao_descricao = "Intersecção"    
  elif operacao == 'D':
        resultado = diferenca(set1, set2)
        operacao_descricao = "Diferença"
  elif operacao == 'C':
        resultado = produto_cartesiano(set1, set2)
        operacao_descricao = "Produto Cartesiano"
  
  print(f"{operacao_descricao}: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}\n")
  