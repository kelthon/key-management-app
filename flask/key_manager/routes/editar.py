from key_manager import app
from key_manager.models import db
from key_manager.models.category import Category
from key_manager.models.key import Key
from key_manager.models.user import User
from key_manager.models.registry import Registry
from key_manager.forms.formUser import FormUser
from key_manager.forms.formReg import RegForm
from key_manager.forms.formKey import KeyForm
from key_manager.forms.formCat import CatForm
from flask import (
    Blueprint, render_template,
    request, url_for, redirect, 
    flash, session
)
import hashlib

edit = Blueprint("edit", __name__, url_prefix="/edit")

app.register_blueprint(edit)