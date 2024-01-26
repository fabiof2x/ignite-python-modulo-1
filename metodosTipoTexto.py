nome = "Fábio"
sobrenome = "Dias"
nome_completo = "Fábio Dias"

# Upper: deixa todas as letras em maiusculo
print(nome.upper())

# Lower: deixa todas as letras em minusculo
print(nome.lower())

# Count: conta quantas vezes um caracter aparece na string
print(nome_completo.count("i"))

# Find: retorna a posição da primeira ocorrência do caracter
print(nome_completo.find("i"))

# Encode: converte a string para bytes
print(nome.encode())
print(nome.encode().decode()) # converte bytes para string

# Replace: substitui um caracter por outro
print(nome_completo.replace("i", "y"))

# Join: junta os caracteres com o caracter passado como parametro
print("-".join(nome)) 

# Split: separa a string em uma lista de strings
print(nome_completo.split(" ")) # Para um espaço em branco pode usar somente .split()

# Strip: remove os espaços ou caracteres em branco do inicio e do fim da string
print("  Fábio Dias  ".strip())
print("xFábio Diasx".strip("x"))
print("xFábio Diasx".rstrip("x")) # remove somente da direita
print("xFábio Diasx".lstrip("x")) # remove somente da esquerda

# Startswith: verifica se a string começa com o caracter passado como parametro
print(nome_completo.startswith("F")) # retorna True, pois a variável nome_completo começa com F
print(nome_completo.startswith("M")) # retorna False, pois a variável nome_completo começa com F e não com M

# Endswith: verifica se a string termina com o caracter passado como parametro
print(nome_completo.endswith("s")) # retorna True, pois a variável nome_completo termina com s
print(nome_completo.endswith("x")) # retorna False, pois a variável nome_completo termina com s e não com x

# In: verifica se o caracter passado como parametro está na string
print("bio" in nome_completo) # retorna True, pois a variável nome_completo contém a string bio
print("abc" in nome_completo) # retorna False, pois a variável nome_completo não contém a string abc

# Not in: verifica se o caracter passado como parametro não está na string
print("bio" not in nome_completo) # retorna False, pois a variável nome_completo contém a string bio
print("abc" not in nome_completo) # retorna True, pois a variável nome_completo não contém a string abc
