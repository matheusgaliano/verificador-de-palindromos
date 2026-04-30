def verifica_palindromo(palavra):
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        return True
    else:
        return False

texto_usuario = input("Digite uma palavra: ")

resultado = verifica_palindromo(texto_usuario)

if resultado:
    print("A palavra que você digitou é um Palíndromo!")
else:
    print("A palavra que você digitou não é um Palíndromo!")
