from app import (
    app,
    db,
    Aluno,
)  # Certifique-se de que 'app' e 'Aluno' são importados corretamente


def add_sample_data():
    # Crie alguns alunos de exemplo
    aluno1 = Aluno(
        nome="João Silva",
        idade=15,
        nota_primeiro_semestre=7.5,
        nota_segundo_semestre=8.0,
        nome_professor="Prof. Maria",
        numero_sala="101",
    )

    aluno2 = Aluno(
        nome="Ana Souza",
        idade=14,
        nota_primeiro_semestre=9.0,
        nota_segundo_semestre=8.5,
        nome_professor="Prof. João",
        numero_sala="102",
    )

    # Adicione os alunos ao banco de dados
    with app.app_context():
        db.create_all()  # Certifique-se de que as tabelas estão criadas
        db.session.add(aluno1)
        db.session.add(aluno2)
        db.session.commit()
        print("Dados adicionados com sucesso!")


if __name__ == "__main__":
    add_sample_data()
