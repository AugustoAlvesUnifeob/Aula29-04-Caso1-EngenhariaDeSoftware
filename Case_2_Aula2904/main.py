from flask import Flask
from controller.usuario_controller import UsuarioController
from view.usuario_view import UsuarioView

app = Flask(__name__)

view = UsuarioView()
controller = UsuarioController(view)

@app.route("/")
def home():
    return controller.home()

@app.route("/criar")
def criar():
    return controller.tela_criar()

@app.route("/salvar", methods=["POST"])
def salvar():
    return controller.criar_usuario()

if __name__ == "__main__":
    app.run(debug=True)