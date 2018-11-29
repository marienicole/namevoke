from flask import Flask

secretsanta = Flask(__name__)
secretsanta.config['SECRET_KEY'] = 'any secret string'

from secretsanta import routes
