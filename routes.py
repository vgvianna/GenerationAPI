from flask import request, jsonify
from app import app, db
from models import Aluno


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
