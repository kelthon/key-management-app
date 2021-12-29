from key_manager import app
from key_manager.models import db
from key_manager.models.category import Category
from key_manager.models.key import Key
from key_manager.models.user import User
from key_manager.models.news import News
from key_manager.models.registry import Registry
from key_manager.forms.formUser import FormUser, EditPassword
from key_manager.forms.formReg import RegForm
from key_manager.forms.formKey import KeyForm
from key_manager.forms.formCat import CatForm
from key_manager.forms.formNews import NewsForm
from flask import (
    Blueprint, render_template,
    request, url_for, redirect, 
    flash, session
)
import hashlib

edit = Blueprint("edit", __name__, url_prefix="/edit")

@edit.route("/category/<category_slug>", methods=['GET', 'POST'])
def editCategory(category_slug):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        category = Category.query.filter_by(slug=category_slug).first()
        if category is None:
            flash("Categoria não encontrada", "error_msg")
            return redirect(url_for('view.viewIndex'))
        editCategoria = CatForm()
        if request.method == 'POST':
            newName = request.form.get("name")
            newSlug = request.form.get("slug").lower()
            if editCategoria.validate_on_submit():
                category.name=newName
                category.slug=newSlug
                db.session.commit()
                flash("Categoria atualizada com Sucesso", "success_msg")
                return redirect(url_for('view.viewCat', category_slug=category_slug))
        return render_template("editar_categoria.html", category=category, form=editCategoria, action=url_for('edit.editCategory', category_slug=category_slug), title="Editar Categoria", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

@edit.route('/key/<key_slug>', methods=['GET', 'POST'])
def editKey(key_slug):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        key = Key.query.filter_by(slug=key_slug).first()
        if key is None:
            flash("Chave não encontrada", "error_msg")
            return redirect(url_for('view.viewIndex'))
        editKey = KeyForm()
        editKey.key_category_id.choices = [(cat.id, cat.name) for cat in Category.query.order_by("name")]
        if request.method == 'POST':
            newName = request.form.get("name")
            newSlug = request.form.get("slug").lower()
            new_key_avaliable = request.form.get("key_avaliable") == 'True'
            new_key_category_id = int(request.form.get("key_category_id"))
            
            if editKey.validate_on_submit():
                key.name = newName
                key.slug = newSlug
                key.key_avaliable = new_key_avaliable
                key.key_category_id = new_key_category_id
                db.session.commit()
                flash("Chave atualizada com Sucesso", "success_msg")
                return redirect(url_for('view.viewKey', key_slug=key_slug))
            else:
                flash("Dados inválidos", "error_msg")
                return redirect(url_for('view.viewIndex'))
        return render_template("editar_chave.html", key=key, form=editKey, action=url_for('edit.editKey', key_slug=key_slug), title="Editar Chave", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

@edit.route('/user/password/<user_username>', methods=['GET', 'POST'])
def editPassword(user_username):
    if session.get("user_auth", False) and session.get("user_username", False) == user_username:
        user = User.query.filter_by(username=user_username).first()
        
        if user is None:
            flash("Usuário não existe", "error_msg")
            return redirect(url_for('index'))

        editpass = EditPassword()
        if request.method == 'POST':
            from key_manager.__init__ import logging
            log = logging.getLogger('waitress')
            
            username = request.form.get("username")
            password = request.form.get("password")
            hash_password = hashlib.md5(password.encode("utf8")).hexdigest()
        
            newPassword = request.form.get("newpassword")
            confirm_password = request.form.get("confirm_password")
            hash_new_password = hashlib.md5(newPassword.encode("utf8")).hexdigest()
            
            if confirm_password == newPassword and username == user.username and hash_password == user.password:
                if editpass.validate_on_submit():
                    user.password = hash_new_password
                    db.session.commit()
                    flash("Senha atualizada com sucesso", "success_msg")
                    return redirect(url_for('view.viewUser', user_username=user_username))
                else:
                    flash("Validação falhou", "error_msg")
                    return redirect(url_for("view.viewIndex"))
            else:
                messages = []
                log.info(confirm_password)
                log.info(newPassword)
                if confirm_password != newPassword:
                    messages.append("Senhas não conferem") 
                if user.password != hash_password:
                    messages.append("Senha incorreta")
                if username != user.username:
                    messages.append("Usuário incorreto") 
                for msg in messages:
                    flash(msg, "error_msg")
                return redirect(url_for("view.viewIndex"))
        return render_template("editar_senha.html", form=editpass, action=url_for('edit.editPassword', user_username=user_username), title="Editar Senha", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))
    
@edit.route('/user/<user_username>', methods=['GET', 'POST'])
def editUser(user_username):
    if session.get("user_auth", False) and session.get("user_username", False) == user_username:
        user = User.query.filter_by(username=user_username).first()
        
        if user is None:
            flash("Usuário não existe", "error_msg")
            return redirect(url_for('index'))

        editUser = FormUser()
        if request.method == 'POST':
            newName = request.form.get("name")
            newEmail = request.form.get("email")
            newPhone = request.form.get("phone")
            
            username = request.form.get("username")
            confirm_password = request.form.get("confirm_password")
            password = request.form.get("password")
            hash_password = hashlib.md5(password.encode("utf8")).hexdigest()
            
            if user.password == hash_password and confirm_password == password and user.username == username:
                if editUser.validate_on_submit():
                    user.name = newName
                    user.email = newEmail
                    user.phone = newPhone
                    db.session.commit()
                    flash("Dados do usuário atualizados com Sucesso", "success_msg")
                    return redirect(url_for('view.viewUser', user_username=user_username))
                else:
                    flash("Validação falhou", "error_msg")
                    return redirect(url_for("view.viewIndex"))
            else:
                messages = []
                if confirm_password != password:
                    messages.append("Senhas não conferem") 
                if user.password != hash_password:
                    messages.append("Senha incorreta")
                if username != user.username:
                    messages.append("Usuário incorreto") 
                for msg in messages:
                    flash(msg, "error_msg")
                return redirect(url_for("view.viewIndex"))
        return render_template("editar_usuario.html", user=user, form=editUser, action=url_for('edit.editUser', user_username=user_username), title="Editar Dados", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

@edit.route('/registry/<registry_id>', methods=['GET', 'POST'])
def editRegistry(registry_id):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        registry = Registry.query.filter_by(id=registry_id).first()
        if registry is None:
            flash("Registro não encontrado", "error_msg")
            return redirect(url_for("view.viewIndex"))

        newRegForm = RegForm()
        newRegForm.user_id.choices = [(user.id, user.username) for user in User.query.order_by("username")]
        newRegForm.key_id.choices = [(key.id, key.name) for key in Key.query.order_by("name")]

        if request.method == "POST":
            newUser_id = int(request.form.get("user_id"))
            newKey_id = int(request.form.get("key_id"))
            newName = request.form.get("holder_name")
            newEmail = request.form.get("holder_email")
            
            if newRegForm.validate_on_submit():
                registry.user_id = newUser_id
                registry.key_id = newKey_id
                registry.holder_name = newName
                registry.holder_email = newEmail
                db.session.commit()
                flash("Registro atualizado com Sucesso", "success_msg")
                return redirect(url_for('view.viewReg', reg_id=registry_id))
            else:
                flash("Dados inválidos", "error_msg")
                return redirect(url_for('view.viewIndex'))
        return render_template("editar_registro.html", registry=registry, form=newRegForm, action=url_for('edit.editRegistry', registry_id=registry_id), title="Editar Registro", hidden_footer=True)
    return redirect(url_for('index'))

@edit.route('/news/<news_id>', methods=['GET', 'POST'])
def editNews(news_id):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        news = News.query.filter_by(id=news_id).first()
        if news is None:
            flash("Notícia não encontrada", "error_msg")
            return redirect(url_for('index'))
        
        editForm = NewsForm()

        if request.method == 'POST':
            if editForm.validate_on_submit:
                news.title = request.form.get("title")
                news.content = request.form.get("content")
                db.session.commit()
                flash("Noticia Atualizada com sucesso", "success_msg")
            else:
                flash("Validação falhou", "error_msg")
        else:
            return render_template("forms/cadastrar_noticias.html", news=news, form=editForm, action=url_for('edit.editNews', news_id=news_id), title="Editar Notícia", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

app.register_blueprint(edit)