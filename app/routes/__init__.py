from flask import Blueprint, session

Routes = Blueprint('routes', __name__, template_folder='views')

from . import index