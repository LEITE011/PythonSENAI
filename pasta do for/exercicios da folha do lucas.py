#criar lista com os nomes de 5 objetos
objetos = ["lapis","caneta","borracha","folha","mesa"]
print("lista de objetos criada")

#adicione mais um objeto ao final da lista
objetos.append("pulseira")
print("objeto adicionado ao final da lista")

#acesse o objeto que esta na 2 posiçao e exiba-o
print(objetos[1])
print("o objeto que esta na 2 posiçao foi acessado e exibido")

#remova um objeto da lista e exiba-o
obj = (objetos.pop(4))
print(obj)
print("o objeto foi removido da lista e exibido")

#exiba o tamanho da lista
print(len(objetos))
print("tamanho da lista exibido")

#mostrar todos os itens com o for
for objeto in objetos:
    print(objeto)
    print("todos os itens foram exibidos com o for")
    
#verifique se a 'cadeira' esta na lista. se sim remova-a, senao adicione
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print("cadeira removida")
else:
    objetos.append("cadeira")
    print("cadeira adicionada")
    
#ordene a lista em ordem alfabetica, exiba o antes e o depois
print(objetos)
objetos.sort()
print(objetos)
print("lista em ordem alfabetica entregue junto com o antes e o depois")

#exiba o primeiro e o ultimo objeto e exiba eles
num = len(objetos)
n1 = objetos[0]
n2 = objetos[num - 1]
print("primeiro: ",n1,"ultimo: ",n2)
print("primeiro e ultimo numero exibidos")

#limpe toda a lista
objetos.clear()
print("lista limpa")