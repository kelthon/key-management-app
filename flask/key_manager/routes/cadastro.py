from key_manager import app
from key_manager.models import db
from key_manager.models.category import Category
from key_manager.models.key import Key
from key_manager.models.user import User
from key_manager.models.news import News
from key_manager.models.registry import Registry
from key_manager.forms.formUser import FormUser
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

cadastro = Blueprint("cadastro", __name__, url_prefix="/new")

@cadastro.route("/category", methods=["GET", "POST"])
def newCategory():
    catForm = CatForm()
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        if request.method == "POST":
            name = request.form.get("name")
            slug = request.form.get("slug").lower()
            
            if catForm.validate_on_submit():
                newCat = Category(name=name, slug=slug)
                db.session.add(newCat)
                db.session.commit()
                flash("Categoria criada com sucesso", "success_msg")
                return redirect(url_for("admin.admHome"))
            else:
                flash("Falha ao validar dados", "error_msg")
                return redirect(url_for("admin.admHome"))
        return render_template("forms/cadastrar_categoria.html", form=catForm, action=url_for("cadastro.newCategory"), title="Cadastrar Categoria", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

@cadastro.route("/key", methods=["GET", "POST"])
def newKey():
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        keyForm = KeyForm()
        keyForm.key_category_id.choices = [(cat.id, cat.name) for cat in Category.query.order_by("name")]
        if request.method == "POST":
            name = request.form.get("name")
            slug = request.form.get("slug").lower()
            key_avaliable = request.form.get("key_avaliable", False) == 'True'
            key_category_id = int(request.form.get("key_category_id"))
            if keyForm.validate_on_submit():
                newKey = Key(name=name, slug=slug, key_category_id=key_category_id, key_avaliable=key_avaliable)
                db.session.add(newKey)
                db.session.commit()
                flash("Chave criada com sucesso", "success_msg")
                return redirect(url_for("admin.admHome"))
        return render_template("forms/cadastrar_chave.html", form=keyForm, action=url_for('cadastro.newKey'), title="Cadastrar Chave", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))
@cadastro.route("/user", methods=["GET", "POST"])
def newUser():
    if session.get("user_auth", False) == False:
        userform = FormUser()
        if request.method == "POST":
            name = request.form.get("name")
            username = request.form.get("username")
            email = request.form.get("email")
            phone = request.form.get("phone")
            password = request.form.get("password")

            hash_passsword = hashlib.md5(password.encode("utf8")).hexdigest()

            if userform.validate_on_submit():
                newuser = User(name=name, username=username, email=email, phone=phone, password=hash_passsword)
                if newuser is None:
                    db.session.add(newuser)
                    db.session.commit()
                    try:
                        session['user_id'] = newuser.id
                        session['user_username'] = newuser.username
                        session['user_auth'] = True
                        session['user_permission'] = newuser.usertype
                        flash("Usuário cadastrado com Sucesso", "success_msg")
                        return redirect(url_for('index'))
                    except:
                        flash("Falha de autenticação da Sessão", "error_msg")
                        return redirect(url_for('login'))
                else:
                    flash("Usuário já existe", "error_msg")
                return redirect(url_for("view.viewUser",user_username=newuser.username))
            else:
                flash("Falha ao validar dados", "error_msg")
        return render_template("forms/cadastrar_usuario.html", form=userform, action=url_for('cadastro.newUser'), hidden_footer=True, title="Cadastrar Usuário")
    else:
        return redirect(url_for('index'))

@cadastro.route('/registry', methods=['GET', 'POST'])
def newRegistry():
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":   
        regForm = RegForm()
        regForm.user_id.choices = [(user.id, user.username) for user in User.query.order_by("username")]
        regForm.key_id.choices = [(key.id, key.name) for key in Key.query.filter_by(key_avaliable=True).order_by("name")]

        if request.method == "POST":
            user_id = int(request.form.get("user_id"))
            key_id = int(request.form.get("key_id"))
            name = request.form.get("holder_name")
            email = request.form.get("holder_email")
            
            if regForm.validate_on_submit():
                newRegistry = Registry(user_id=user_id, key_id=key_id, holder_name=name, holder_email=email)
                key = Key.query.filter_by(id=newRegistry.key_id)
                key.key_avaliable=False
                db.session.add(newRegistry)
                db.session.commit()
                flash("Registro criado com sucesso", "success_msg")
                return redirect(url_for("view.viewReg", reg_id=newRegistry.id))
            else:
                flash("Falha na validação dos dados", "error_msg")
        return render_template("forms/cadastrar_emprestimo.html", form=regForm, action=url_for('cadastro.newRegistry'), title="Cadastrar Empréstimo", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

@cadastro.route('/news', methods=['GET', 'POST'])
def newNews():
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        newsForm = NewsForm()
        if request.method == 'POST':
            if newsForm.validate_on_submit:
                news = News(title=request.form.get("title"), content=request.form.get("content"))
                db.session.add(news)
                db.session.commit()
                flash("Noticia cadastrada com sucesso", "success_msg")
            else:
                flash("Validação falhou", "error_msg")
        else:
            return render_template("forms/cadastrar_noticias.html", form=newsForm, action=url_for('cadastro.newNews'), title="Cadastrar Notícia", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

app.register_blueprint(cadastro)