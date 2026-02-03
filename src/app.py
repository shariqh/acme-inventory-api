from flask import Flask

from .routes.inventory import inventory_bp
from .routes.users import users_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(inventory_bp, url_prefix='/api')
    app.register_blueprint(users_bp, url_prefix='/api')

    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
