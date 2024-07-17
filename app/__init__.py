from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_caching import Cache
from flask_talisman import Talisman
from config import Config
from app.extensions import db, migrate, login_manager, socketio, cache, talisman
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

bootstrap = Bootstrap5()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
socketio = SocketIO()
cache = Cache()
talisman = Talisman()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)
    cache.init_app(app)
    talisman.init_app(app, content_security_policy=None)
    bootstrap.init_app(app)
    csrf.init_app(app)

     # Import semua model di sini
    from app.models.users import User
    from app.models.user_profile import UserProfile
    from app.models.provinsi import Provinsi



    # Import dan daftarkan blueprint di sini
    # from app.routes import main_bp
    # app.register_blueprint(main_bp)
    from app.routes import auth_bp
    app.register_blueprint(auth_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # @login_manager.provinsi_loader
    # def load_provinsi(kode_provinsi):
    #     return Provinsi.query.get(int(kode_provinsi))

    return app