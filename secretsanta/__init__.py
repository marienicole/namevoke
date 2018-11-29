from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

from secretsanta import routes
