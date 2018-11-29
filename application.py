from flask import Flask

application = Flask(__name__)
application.config['SECRET_KEY'] = 'any secret string'

application.run(threaded=True)

import routes
