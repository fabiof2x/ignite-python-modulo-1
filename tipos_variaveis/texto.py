# Declaração
nome_completo = "Fábio Dias"

nome_completo_aspas = """Fábio 
Dias"""

nome_completo_quebra = "Fábio \
Dias"

nome = "Fábio"
sobrenome = "Dias"

# Formatação
print("Nome completo (1ª forma):", nome_completo)
print("Nome completo (2ª forma):" + nome_completo)
print("Nome completo (3ª forma):" + "Fábio" + "Dias")
print("Nome completo (4ª forma):", "Fábio", "Dias")
print("Nome completo (5ª forma):", nome_completo_aspas)
print("Nome completo (6ª forma):", nome_completo_quebra)
print("Nome completo (7ª forma): %s" % nome_completo)
print("Nome completo (8ª forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9ª forma): {nome} {sobrenome}")
print("Nome completo (10ª forma): {} {}".format(nome, sobrenome))