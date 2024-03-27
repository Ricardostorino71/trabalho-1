def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista) if lista else 0
    return soma, media

numeros = [1, 2, 3, 4]
soma, media = calcular_soma_e_media(numeros)
print("Soma:", soma)
print("Média:", media)

def substituir_palavra(lista, palavra_antiga, palavra_nova):
    nova_lista = [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]
    return nova_lista

palavras = ["banana", "morango", "limão"]
palavra_antiga = "limão"
palavra_nova = "laranja"
nova_lista = substituir_palavra(palavras, palavra_antiga, palavra_nova)
print("Lista original:", palavras)
print("Nova lista:", nova_lista)

def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print("*" * i)


num_linhas = 4
gerar_triangulo(num_linhas)

