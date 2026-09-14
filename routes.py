from flask import render_template, session, redirect, url_for, flash
from app import app, db
from models import User, Role
from forms import UserForm

@app.route('/', methods=['GET', 'POST'])
def index():

    #Garate que a função seja execultada
    default_roles = [
        'Administrator',
        'Moderator',
        'User'
    ]

    # Percorre a lista para verificar cada função
    for role_name in default_roles:

        # Procura a função pelo nome
        role = Role.query.filter_by(
            name=role_name
        ).first()

        # Se ela ainda não existir, é criado
        if role is None:

            role = Role(
                name=role_name
            )

            db.session.add(role)

    # Salva as funções no banco
    db.session.commit()


    # Cria o formulário
    form = UserForm()


    # Busca funções do banco

    roles = Role.query.order_by(
        Role.id
    ).all()

    # Preenche o select do formulário
    
    # O SelectField precisa receber:
    #
    # [(valor, texto), ...]
    #
    # Ex:
    #
    # [
    #     (1, 'Administrator'),
    #     (2, 'Moderator'),
    #     (3, 'User')
    # ]

    form.role.choices = [
        (role.id, role.name)
        for role in roles
    ]

    # Processa o cadastro

    if form.validate_on_submit():

        # Verifica se o usuário já existe
        user = User.query.filter_by(
            username=form.username.data
        ).first()


        if user is None:


            # Pega a função desejada

            # form.role.data contém o ID da função.
            # Administrator 
            # Moderator 
            # User          

            role = Role.query.get(
                form.role.data
            )
            # Cria usuários
            user = User(
                username=form.username.data,
                role=role
            )


            # Adiciona o usuário à sessão do SQLAlchemy
            db.session.add(user)


            # Persiste o usuário no banco
            db.session.commit()


            # Informações usadas pela mensagem da página
            session['known'] = False
            session['name'] = user.username


            flash(
                'Usuário cadastrado com sucesso!'
            )


        else:

            # Usuário já existe
            session['known'] = True
            session['name'] = user.username

            flash(
                'Este usuário já está cadastrado.'
            )


        # Limpa o formulário depois do cadastro
        form.username.data = ''


        # Redireciona para a página principal
        #  evita cadastrar novamente o usuário
        # caso a página seja atualizada.
        return redirect(
            url_for('index')
        )
    # Busca usuários

    users = User.query.order_by(
        User.id
    ).all()
    # conta usuários
    user_count = User.query.count()

    # Contador de funções
    role_count = Role.query.count()
    
    # Envia os dados para o HTLM
    return render_template(

        'index.html',

        # Formulário
        form=form,

        # Nome utilizado no cabeçalho
        name=session.get('name'),

        # Indica se o usuário já existia
        known=session.get(
            'known',
            False
        ),

        # Lista de usuários
        users=users,

        # Lista de funções
        roles=roles,

        # Número de usuários
        user_count=user_count,

        # Número de funções
        role_count=role_count
    )


@app.errorhandler(404)
def page_not_found(e):

    return render_template(
        '404.html'
    ), 404