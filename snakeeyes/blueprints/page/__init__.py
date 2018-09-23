# snakeeyes/blueprints/page/__init.py
from flask import Blueprint
page = Blueprint('page', __name__, template_folder='templates')
from snakeeyes.blueprints.page import views
