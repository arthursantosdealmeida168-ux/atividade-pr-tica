O que aconteceria sem int()?

Se você digitasse 20 para a idade, o Python armazenaria "20" como texto (string). Nesse caso, operações matemáticas não funcionariam corretamente. Por exemplo:

idade = input("Digite sua idade: ")
print(idade + 1)

Geraria erro, porque o Python tentaria somar um número a um texto. Por isso usamos int() para converter a entrada em um número inteiro.
