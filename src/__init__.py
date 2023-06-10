from flask import Flask
from flask_jwt_extended import (
    JWTManager,
)

from config import Config
from src.database.db import init_db
from src.common.exceptions.custom_exceptions import (
    UnauthorizedException,
    ConflictException,
    BadRequestException,
    NotFoundException,
)
from src.common.exceptions.exception_handlers import (
    unauthorized_exception,
    conflict_exception,
    server_exception,
    bad_request_exception,
    not_found_exception,
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Register blueprints
    from src.auth.auth_routes import auth_bp
    from src.water_intake.water_intake_routes import water_intake_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(water_intake_bp)

    # Register error handlers
    app.register_error_handler(400, bad_request_exception)
    app.register_error_handler(BadRequestException, bad_request_exception)
    app.register_error_handler(NotFoundException, not_found_exception)
    app.register_error_handler(UnauthorizedException, unauthorized_exception)
    app.register_error_handler(ConflictException, conflict_exception)
    app.register_error_handler(Exception, server_exception)

    init_db(app)
    JWTManager(app)

    return app
