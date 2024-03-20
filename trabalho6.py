
numeros = [10, 20, 30, 40]
frase = "Python é uma linguagem de programação poderosa"
palavra = "programação"


media = sum(numeros) / len(numeros)
print("A média aritmética dos números é:", media)


numero_quadrado = numeros[0] ** 2
print("O quadrado do primeiro número é:", numero_quadrado)


numero_dobro = numeros[1] * 2
print("O dobro do segundo número é:", numero_dobro)


quantidade_letras = len(palavra)
print("A quantidade de letras na palavra é:", quantidade_letras)


quantidade_espacos = frase.count(" ")
print("A quantidade de espaços em branco na frase é:", quantidade_espacos)


primeiro_maior = numeros[0] > numeros[1]
print("O primeiro número é maior que o segundo:", primeiro_maior)


maior_numero = max(numeros)
print("O maior número é:", maior_numero)
