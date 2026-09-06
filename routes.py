from flask import render_template, session, redirect, url_for, flash
from app import app, db
from models import User, Role
from forms import NameForm


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Rota principal que processa o formulário de nome e exibe
    a tabela de usuários cadastrados e suas funções.
    """
    form = NameForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()

        if user is None:
            user_role = Role.query.filter_by(name='User').first()

            if user_role is None:
                user_role = Role(name='User')
                db.session.add(user_role)
                db.session.commit()

            user = User(username=form.name.data, role=user_role)
            db.session.add(user)
            db.session.commit()

            session['known'] = False
            flash('Looks like you are a new user! We added you to our database.')
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''

        return redirect(url_for('index'))

    users = User.query.all()

    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False),
        users=users
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404