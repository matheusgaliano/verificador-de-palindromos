# Verificador de Palíndromos

## Antes de mais nada, vamos ver o que é isso.

Palíndromo é uma palavra, frase ou número que se lê da mesma forma da esquerda para a direita e vice-versa. O termo deriva do grego palin (novamente) e dromos (percurso), significando "correr em sentido inverso".

## Sobre o Projeto
Este projeto consiste em uma aplicação web que identifica se uma entrada é um palíndromo. A lógica foi desenvolvida para ser robusta, ignorando diferenças entre maiúsculas e minúsculas, acentuações e caracteres especiais.

## Destaques Técnicos
1. Tratamento de caracteres especiais: Uso da biblioteca unicodedata para normalizar a string (NFD), permitindo a remoção de acentos sem descaracterizar as letras.

2. Filtragem via Expressões Regulares (Regex): Implementação do módulo re para garantir que apenas caracteres alfanuméricos sejam considerados, ignorando espaços, pontuações e símbolos.

3. Padronização de Case: Uso do método .lower() para garantir que a comparação seja agnóstica a letras maiúsculas ou minúsculas.

## Arquitetura e Fluxo de Dados 
O projeto utiliza Python com o framework Flask para a interface web. O fluxo de dados funciona da seguinte forma:

1. Entrada: O usuário insere o texto no formulário HTML (Frontend).

2. Processamento: O Flask (Backend) recebe os dados e aciona a lógica core no arquivo palindromo.py.

3. Lógica: A string é limpa, invertida e comparada.

4. Resposta: O resultado é injetado dinamicamente no template via Jinja2 e exibido ao usuário.

## Instruções de Execução 
Para rodar este projeto localmente:

1. Clonar o repositório:
`bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio`

2. Instalar as dependências:
`pip install -r requirements.txt`

3. Iniciar o servidor:
`python app.py`

4. Acessar a aplicação:
Abra o navegador em: `[http://127.0.0.1:5000](http://127.0.0.1:5000)`

---

**Desenvolvido por Matheus Galiano** 
https://www.linkedin.com/in/matheusgaliano/ | galiano.matheus@outlook.com
