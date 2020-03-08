#--------------------
def printaColecao(colecao,qtd):
   print("\ncolecao=[",end=' ')
   for i in range(qtd):
      print( colecao[i],end=' ')
   
   print("]\n")
#--------------------
#--------------------1
def adicionarvalorFinal(colecao, qtd, elem ):
   if qtd < 100:
      colecao[qtd]=elem
      qtd+=1
   return qtd
#--------------------
#---------------------2
#adiciona um elemento a colecao na posicao desejada
def adicionarvalor(colecao, qtd, elem, position):
  
  if position >= qtd:
    colecao[qtd] = elem
    print()
    print("A coleção não possui esta posição, o valor será adicionado ao final dela")
    qtd += 1
  else:
    #Se for um valor na "borda" da coleção, ele faz o que está na borda "ir" 1 para frente e o novo valor na posição desejada
    if colecao[position+1] == 0:
      colecao[position+1] = colecao[position]
      colecao[position] = elem
      qtd += 1   
    else:
      #então se não for o caso acima, ele move todos os elementos da coleção para a direita, a partir da posição inserida pelo usuário, inseri o valor digitado e soma 1 aos valores válidos da coleção
      for i in range(qtd, position, -1):
        colecao[i] = colecao[i-1]
      colecao[position] = elem
      qtd += 1
  return qtd
#---------------------
#---------------------3
def removecomaposicao(colecao, qtd, position):
  if colecao[position+1] == 0:
    colecao[position] = 0
    qtd -= 1    
  else:
    for i in range(position, qtd):
      colecao[i] = colecao[i+1]
    qtd -= 1
  return qtd
#---------------------
#---------------------4
#ele remove a primeira ocorrência do value na colecao
def removeprimeiraocorrencia(colecao, qtd, value):
  #armazena a posição do elemento a ser removido
  position = 0
  for i in range(qtd):
    if colecao[i] == value:
      position = i
      for g in range(position, qtd):
        colecao[g] = colecao[g+1]
      qtd -= 1  
      return qtd
  else:
    print("O valor digitado não está na coleção")
#-----------------------
#-----------------------5
def removetodos(colecao, qtd, value):
  position = 0
  iguais = 0
  for h in range(qtd):
    if colecao[h] == value:
      iguais += 1
  for i in range(iguais):
    if colecao[i] != value:
      print("")
    else:
      position = i
      for g in range(position, qtd):
        colecao[g] = colecao[g+1]
        print(colecao[g])
      qtd -= 1
  return qtd
#-----------------------
#-----------------------6
def procura(colecao, qtd, value):
  for i in range(qtd):
    if colecao[i] == value:
      return i
  else:
    return -1
#-----------------------
#-----------------------7
def procursomadedois(colecao, qtd, value):
  #usa uma flag para checar o estado da condição ali embaixo, para não retornar direto e brecar o loop
  flag = False
  for i in range(qtd):
    for g in range(qtd):
      if (colecao[i] + colecao[g]) == value:
        flag = True
      else:
        flag = False
      if flag == True:
        return flag
  return flag
#-----------------------
def main():
   #declara o vetor
   colecao = [0]*100
   #---------------- 

   qtd = 0 #quantidade de elementos validos
   
   opc = 0 #opcao escolhido pelo usuário

   # laco principal do menu
   while opc != 8:
      print('''[1] Adicionar um elemento no final da coleção
        [2] Adicionar um elemento em uma posição da coleção
        [3] Remover um elemento em uma posição na coleção 
        [4] Remover a primeira ocorrência do elemento na coleção 
        [5] Remover todas as ocorrências de um elemento na coleção 
        [6] Verificar se dado um elemento está contido na coleção
        [7] Verificar se dado um valor existem dois elementos na coleção que somados é igual ao valor informado
        [8] Sair''' )
      print() 
      opc = int(input())
      #adiciona no final
      if opc == 1:
        elem = int(input("digite um elemento:"))
        qtd = adicionarvalorFinal(colecao, qtd,elem )
      if opc == 2:
        elem = int(input("digite um elemento a adicionar: "))
        position = int(input("Digite a posição a ser inserida o elemento: "))
        qtd = adicionarvalor(colecao, qtd, elem, position)
      if opc == 3:
        position = int(input("digite a posição para excluir o elemento: "))
        qtd = removecomaposicao(colecao, qtd, position)
      if opc == 4:
        value = int(input("Digite o valor a ser removido: "))
        qtd = removeprimeiraocorrencia(colecao, qtd, value)
      if opc == 5:
        value = int(input("Digite o valor a ser removido: "))
        qtd = removetodos(colecao, qtd, value)
      if opc == 6:
        value = int(input("Digite o valor a ser procurado: "))
        print(procura(colecao, qtd, value))
      if opc == 7:
        value = int(input("Digite o valor a ser procurado: "))
        print(procursomadedois(colecao, qtd, value))
      # imprime o vetor colecao
      printaColecao(colecao,qtd)
   print("fim do programa")   
#----- chama a funcao principal
main()
