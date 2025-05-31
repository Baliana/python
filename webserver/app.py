from flask import Flask, render_template



# --- Templates (modelos)
# -- Estrutura para criar html


# --- Static (estaticos/não-dinamicas/não muda)
# -- Tudo que está nela fica visivel

app = Flask(__name__)

# 
@app.route("/")
def firt_page():
    return render_template("index.html")

@app.route("/usuario")
def aboutuser_page():
    return render_template("usuario.html")



# Atualizar sozinho sem precisar rodar novamente a aplicação
app.run(debug=True)

