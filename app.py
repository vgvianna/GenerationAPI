from flask_cors import CORS
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from swagger import (
    swaggerui_blueprint,
)  # Importar aqui, se o swagger estiver configurado corretamente

app = Flask(__name__)
CORS(app)

# Configurar a URL do banco de dados usando uma variável de ambiente
# Se DATABASE_URL não estiver definido, usará SQLite como fallback
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", "sqlite:///school_db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importar e registrar o blueprint do Swagger após a criação do app
app.register_blueprint(swaggerui_blueprint, url_prefix="/swagger")


class Aluno(db.Model):
    __tablename__ = "alunos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    nome_professor = db.Column(db.String(100), nullable=False)
    numero_sala = db.Column(db.String(10), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "nome_professor": self.nome_professor,
            "numero_sala": self.numero_sala,
        }


@app.route("/api/v1/alunos", methods=["GET"])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.as_dict() for aluno in alunos]), 200


@app.route("/api/v1/alunos/<int:id>", methods=["GET"])
def get_aluno(id):
    aluno = Aluno.query.get(id)
    if aluno is None:
        return jsonify({"message": "Aluno não encontrado"}), 404
    return jsonify(aluno.as_dict()), 200


@app.route("/api/v1/alunos", methods=["POST"])
def create_aluno():
    data = request.json
    novo_aluno = Aluno(
        nome=data["nome"],
        idade=data["idade"],
        nota_primeiro_semestre=data["nota_primeiro_semestre"],
        nota_segundo_semestre=data["nota_segundo_semestre"],
        nome_professor=data["nome_professor"],
        numero_sala=data["numero_sala"],
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(novo_aluno.as_dict()), 201


@app.route("/api/v1/alunos/<int:id>", methods=["PUT"])
def update_aluno(id):
    aluno = Aluno.query.get(id)
    if aluno is None:
        return jsonify({"message": "Aluno não encontrado"}), 404

    data = request.json
    aluno.nome = data["nome"]
    aluno.idade = data["idade"]
    aluno.nota_primeiro_semestre = data["nota_primeiro_semestre"]
    aluno.nota_segundo_semestre = data["nota_segundo_semestre"]
    aluno.nome_professor = data["nome_professor"]
    aluno.numero_sala = data["numero_sala"]

    db.session.commit()
    return jsonify(aluno.as_dict()), 200


@app.route("/api/v1/alunos/<int:id>", methods=["DELETE"])
def delete_aluno(id):
    aluno = Aluno.query.get(id)
    if aluno is None:
        return jsonify({"message": "Aluno não encontrado"}), 404

    db.session.delete(aluno)
    db.session.commit()
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
