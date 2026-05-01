from flask import Flask, render_template, request
from palindromo import verifica_palindromo

app = Flask(__name__)

# Rota principal
@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    texto = ""
    
    if request.method == "POST":
        texto = request.form.get("palavra")
        if texto:
            es_palindromo = verifica_palindromo(texto)
            resultado = "É um palíndromo! ✅" if es_palindromo else "Não é um palíndromo! ❌"
            
    return render_template("index.html", resultado=resultado, texto_digitado=texto)

if __name__ == "__main__":
    app.run(debug=True)