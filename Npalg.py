
#------------------- 1
def adicionaFinal(colecao, qtd, elem ):
   if qtd < 100:
      colecao[qtd]=elem
      qtd+=1
   return qtd
#--------------------2 
def addpos(colecao, qtd, elem, pos):
    if qtd < 100:
        for pos in range(len(colecao)):
            if colecao[pos]>elem:
                break
        colecao = colecao[:pos]+[elem]+colecao[pos:]
        qtd+=1
    return colecao
#--------------------3
def rempos(colecao, qtd, elem, pos):
    if qtd<100:
            l = len(colecao)

            if pos >= l:
                pos = l - 1
            elif pos <= 0:
                pos = 0

            return [colecao[i] for i in range(l) if i != pos]
            qtd+=1
            
#--------------------4
def rempri(colecao, qtd, elem, pos):
    string2 = ''
    length = len(string)
    i = 0

    while(i < length):
        if(colecao[i] == char):
            string2 = colecao[0:i] + colecao[i + 1:length]
            break
        i = i + 1
        print(string2)
#--------------------5

#--------------------6

#--------------------7



#--------------------
def main():
   #declara o vetor
   colecao = [0]*100
   qtd = 0 #quantidade de elementos validos
   
   opc = 0
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
            elem = int(input("Digite um elemento:"))
            qtd = adicionaFinal(colecao, qtd,elem )
            print(colecao)
        if opc == 2:
            elem = int(input("Digite um elemento"))
            pos = int(input("Digite uma posição:"))
            qtd = addpos(colecao, qtd, elem)
            print(qtd)
            print(colecao)
        if opc == 3:
            elem = int(input("Digite um elemento:"))
            pos = int(input("Digite uma posição:"))
            qtd = rempos(colecao, qtd, elem)
            print(qtd)
            print(colecao)
        if opc == 4:
            elem = int(input("Digite um elemento:"))
            qtd = rempri(colecao, qtd, elem)
            print(qtd)
            print(colecao)
        if opc == 5:    
            elem = int(input("Digite um elemento:"))
            qtd = rempos(colecao, qtd, elem)
            print(qtd)
            print(colecao)
        if opc == 6:
            elem = int(input("Digite um elemento:"))
            qtd = rempos(colecao, qtd, elem)
            print(qtd)
            print(colecao)
        if opc == 7:
            elem = int(input("Digite um elemento:"))
            qtd = rempos(colecao, qtd, elem)
            print(qtd)
            print(colecao)
        if opc == 8:
            print("Fim do programa")
            break
        

#----- chama a funcao principal
main()