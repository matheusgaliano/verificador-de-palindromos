import unicodedata

def verifica_palindromo(palavra):
    processado = unicodedata.normalize('NFD', palavra)
    palavra_limpa = "".join(c for c in processado if unicodedata.category(c) != 'Mn')
    palavra_limpa = palavra_limpa.lower().replace(" ", "")
    palavra_invertida = palavra_limpa[::-1]
    return palavra_limpa == palavra_invertida #retirada do if e else desnecessários
       

texto_usuario = input("Digite uma palavra: ")

resultado = verifica_palindromo(texto_usuario)

if resultado:
    print("A palavra que você digitou é um Palíndromo!")
else:
    print("A palavra que você digitou não é um Palíndromo!")
