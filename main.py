# Solicita os dados do usuário

nome = input("Digite seu nome completo: ")

# A idade é convertida para int porque será armazenada como número inteiro.
# Sem a conversão, o valor seria uma string (texto).
idade = int(input("Digite sua idade: "))

# O ano também é convertido para int para permitir cálculos matemáticos.
# Sem a conversão, não seria possível subtrair do ano atual.
ano_inicio = int(input("Digite o ano em que começou a estudar programação: "))

linguagem = input("Digite sua linguagem de programação favorita: ")

# A nota é convertida para float porque pode conter casas decimais.
nota = float(input("Digite sua nota de satisfação com o curso (0 a 10): "))

# Processamento
anos_estudando = 2026 - ano_inicio

# Saída formatada
print("============================================")
print("FICHA DO DESENVOLVEDOR")
print("============================================")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Anos estudando: {anos_estudando} ano(s)")
print(f"Linguagem fav.: {linguagem}")
print(f"Nota de satisfação: {nota}")
print("============================================")