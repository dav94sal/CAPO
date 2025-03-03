from flask import Blueprint
from .player_routes import players_bp
from .match_routes import match_bp
from .round_routes import round_bp

api_router = Blueprint("api", __name__)

api_router.register_blueprint(players_bp, url_prefix="/players")
api_router.register_blueprint(match_bp, url_prefix="/matches")
api_router.register_blueprint(round_bp, url_prefix="/rounds")
