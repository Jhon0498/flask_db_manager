from flask import render_template, session, redirect, url_for, flash
from app import app, db
from models import User, Role
from forms import NameForm, UserForm, RoleForm

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route handling the homepage form, checking if the user exists in SQLite.
    """
    # Instantiate the name form from WTForms
    form = NameForm()
    
    # Check if the request method is POST and form validations pass
    if form.validate_on_submit():
        # Query the database to see if a user with this username already exists
        user = User.query.filter_by(username=form.name.data).first()
        
        if user is None:
            # If user does not exist, set role to User by default (if available) or create a new user entry
            user_role = Role.query.filter_by(name='User').first()
            if user_role is None:
                # Fallback: create a default Role if none exists yet
                user_role = Role(name='User')
                db.session.add(user_role)
                db.session.commit()
            
            # Create a new User object and add it to the database session
            user = User(username=form.name.data, role=user_role)
            db.session.add(user)
            db.session.commit()
            
            # Save user state into session for template conditional rendering
            session['known'] = False
            flash('Looks like you are a new user! We added you to our database.')
        else:
            # Mark user as known if found in database
            session['known'] = True
            
        # Store name in Flask session object
        session['name'] = form.name.data
        form.name.data = ''
        
        # Implement Post/Redirect/Get pattern to prevent duplicate submissions on refresh
        return redirect(url_for('index'))
        
    # Render template with variables stored in session
    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False)
    )


@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    """
    Route for listing users, registering new users, and assigning roles (CRUD: Create/Read).
    """
    form = UserForm()
    
    # Populate the dynamic dropdown list with active roles from database
    form.role.choices = [(role.id, role.name) for role in Role.query.order_by('name').all()]
    
    if form.validate_on_submit():
        # Fetch the selected Role object by ID
        selected_role = Role.query.get(form.role.data)
        
        # Create new user record using form data
        new_user = User(username=form.username.data, role=selected_role)
        db.session.add(new_user)
        db.session.commit()
        
        flash(f'User {new_user.username} successfully registered with role {selected_role.name}!')
        return redirect(url_for('manage_users'))
        
    # Query all users registered in SQLite
    users = User.query.all()
    return render_template('users.html', form=form, users=users)


@app.route('/delete-user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """
    Route for removing a user record from the SQLite database (CRUD: Delete).
    """
    # Fetch user by ID or trigger a 404 error if not found
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    flash(f'User {user.username} has been deleted.')
    return redirect(url_for('manage_users'))


@app.errorhandler(404)
def page_not_found(e):
    """
    Global error handler for missing pages (HTTP 404).
    """
    return render_template('404.html'), 404
