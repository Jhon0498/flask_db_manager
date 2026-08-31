import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment

# Define base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize Flask app
app = Flask(__name__)

# Application configurations
app.config['SECRET_KEY'] = 'hard-to-guess-string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)

# Import models and routes after extension initialization
import models
import routes

if __name__ == '__main__':
    app.run(debug=True)