# Declaração
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a minha lista
print("Minha lista:", minha_lista)

# Exibindo a lista
minha_lista[0] = "python"
print("Minha lista depois da alteração:", minha_lista)

print("minha_lista[0]", minha_lista[0])
print("minha_lista[5]", minha_lista[5])
print("minha_lista[1:7]", minha_lista[1:7])
print("minha_lista[:6]", minha_lista[:6])
print("minha_lista[2:]", minha_lista[2:])

# Métodos da lista
# Método append(): Adiciona um elemento no final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Método index(): Retorna o índice de um elemento
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert(): Adiciona um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após insert(2, 10):", minha_lista)

# Método pop(): Remove um elemento da lista
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove(): Remove um elemento da lista
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Método sort(): Ordena a lista
minha_lista_nr = [2, 4, 1, 5, 3] # Criando uma lista numérica para evitar incompatibilidade de tipos
print("Antes do sort():", minha_lista_nr)
minha_lista_nr.sort()
print("Após sort():", minha_lista_nr)