import unicodedata
import re

def verifica_palindromo(palavra):
    processado = unicodedata.normalize('NFD', palavra)
    
    palavra_limpa = "".join(c for c in processado if unicodedata.category(c) != 'Mn')
    
    palavra_limpa = re.sub(r'[^a-zA-Z0-9]', '', palavra_limpa).lower()
    
    palavra_invertida = palavra_limpa[::-1]
    
    return palavra_limpa == palavra_invertida #retirada do if e else desnecessários

if __name__ == "__main__":       
    while True:
        texto_usuario = input("\nDigite uma palavra (ou 'sair' para encerrar): ")
        
        if texto_usuario.lower() == "sair":
            print("Encerrando o programa... Até mais!")
            break


        resultado = verifica_palindromo(texto_usuario)

        if resultado:
            print("A palavra que você digitou é um Palíndromo!")
        else:
            print("A palavra que você digitou não é um Palíndromo!")
