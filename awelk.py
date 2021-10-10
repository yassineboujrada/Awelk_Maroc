
from flask import render_template,session,request
from flask_login import LoginManager,login_user,login_required
from werkzeug.utils import redirect
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask_login import LoginManager,login_user,login_required,UserMixin
from werkzeug.utils import secure_filename
import pandas as pd
import os
from flask.helpers import flash, url_for
from random import randint
from flask_login.utils import logout_user
from envoyer import send_email,buy,verif_msg
import pandas as pd


UPLOAD_FOLDER = 'static/images/product/'
site=Flask(__name__)
site.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
site.config['SQLALCHEMY_DATABASE_URI']='sqlite:///DataBaseawelk'
site.secret_key = "secret key"
site.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#site.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
auth_print = Blueprint('auth_print', __name__)
login_manager = LoginManager()
login_manager.login_view = '/login'
login_manager=LoginManager(site)
login_manager.login_view = 'homme'
login_manager.login_message_category = 'info' 

#bcrypt=Bcrypt(site)
db=SQLAlchemy(site)
###############################
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
#######################  DATABASE DE SITE #########################
#@login_manager.user_loader
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(20),unique=True,nullable=False)
    def __repr__(self):
        return f"User('{self.email}','{self.password}')"

class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    title=db.Column(db.String(120),nullable=False)
    prix=db.Column(db.String(320),nullable=False)
    def __repr__(self):
        return f"Img('{self.name}','{self.mimetype}','{self.title}','{self.prix}')"

    
###############################  Accueil Page

@site.route("/",methods=["POST","GET"])
def homme():
    prodect=Img.query.all()
    if prodect :
        return render_template("accueil.html",imgs=prodect)
    else:
        return render_template("accueil.html")
    
###############################    LOGIN PAGE
@site.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        session["user_administrator"]=request.form.get("user_admin")
        session["password_administrator"]=request.form.get("password_admin")
        user=User.query.filter_by(email="bou8027@gmail.com").first()
        print(user)
        if user.email==session["user_administrator"] and user.password==session["password_administrator"]:
           flash("you're login successful","success")
           login_user(user)
           return redirect(url_for("post")) 
        else:
            flash("votre donnees incorrect , ressayer","prob")
            return redirect(url_for("login")) 
    return render_template('login.html')
@site.route("/logout",methods=["POST","GET"])
def logout():
    #if request.method=="POST":
    flash("tu est deconnecter","success")
    logout_user()
    return redirect(url_for('homme'))
    #return render_template("post.html")
##########################
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@site.route("/post",methods=["POST","GET"])
@login_required
def post():
    if request.method=="POST":
        session["titre"]=request.form.get("title_product")
        session["prix"]=request.form.get("price-product")
        f=request.files["img_file"]
        path = os.path.join(site.config['UPLOAD_FOLDER'], f.filename)
        print(allowed_file(f.filename))
        if allowed_file(f.filename):
            try:
                x=int(session["prix"])
                if isinstance(x, int):
                    flash("votre post est creer","success")
                    db.session.add(Img(name='static/images/product/'+f.filename,title=session['titre'],prix=session["prix"]))
                    db.session.commit()
                    f.save(path)
                    return redirect(url_for("post"))
            except ValueError:
                flash("tu est donnees un caractere dans prix","problem")
                return redirect(url_for("post"))
       
        else:
            flash("les type de fichies qui sont acceptable sont {'png', 'jpg', 'jpeg'}","problem")
            return redirect(url_for("post"))
        
    return render_template("post.html")

##########################
######################
@site.route("/forgot",methods=["POST","GET"])
def forgot():
    if request.method=="POST":
        session['mail_check']=request.form.get("check_email")
        print(session['mail_check'])
        user=User.query.filter_by(email=session['mail_check']).first()
        if user:
            global rand
            rand=str(randint(100000,999999))
            verif_msg(rand)
            return redirect(url_for("verif"))
        else:
            flash("Votre compte n'est pas un compte administrator","er_ver")
            return redirect(url_for("forgot"))
    return render_template("forget.html")
##########################
@site.route("/verifier",methods=["POST","GET"])
def verif():
    if request.method=="POST":
        session['nbr_check']=request.form.get("check_number")
        if session['nbr_check']==rand:
            return redirect(url_for("passwd"))
        else:
            flash("code error","al")
            return redirect(url_for("verif"))
    return render_template("verife.html")
##########################
@site.route("/change",methods=["POST","GET"])
def passwd():
    user=User.query.filter_by(email="bou8027@gmail.com").first()
    if request.method=="POST":
        session['new_pass']=request.form.get('nouveau_pass')
        if len(session['new_pass'])>=6 :
            user.password=session['new_pass']
            db.session.commit()
            return redirect(url_for("login"))
        else:
            flash("votre mot de passe est petit",'er_pass')
    return render_template("password_change.html")

###################################### Product Page
@site.route("/nosproduit")
def product():
    return render_template("nosproduit.html")

@site.route("/nosproduit/BUSINESS-SAC-À-DOS-DE-VOYAGE",methods=["POST","GET"])
def product1():
    return render_template("prod1.html")

@site.route("/nosproduit/DAX-3D-THE-HUNTER-SAC-À-DOS",methods=["POST","GET"])
def product2():
    return render_template("prod2.html")

@site.route("/nosproduit/ARCTIC-HUNTER-SAC-A-DOS-MULTI-FONCTION",methods=["POST","GET"])
def product3():
    return render_template("prod3.html")

@site.route("/nosproduit/FOLDABLE-SMART-SAC-À-DOS-VOYAGE-&-BUSINESS",methods=["POST","GET"])
def product4():
    return render_template("prod4.html")

@site.route("/nosproduit/DAX-TEENAGERS-ECOLE-BACKPACK",methods=["POST","GET"])
def product5():
    return render_template("prod5.html")

@site.route("/nosproduit/last-hunter-sac-a-dos",methods=["POST","GET"])
def product6():
    return render_template("prod6.html")

@site.route("/nosproduit/CHEST-&-BACK-SAC-POUR-SORTIE",methods=["POST","GET"])
def product7():
    return render_template("prod7.html")

@site.route("/nosproduit/BUSINESS-SAC-À-DOS-SMART-LAPTOP-CONVERTIBLE",methods=["POST","GET"])
def product8():
    return render_template("prod8.html")

@site.route("/nosproduit/FASHION-STYLE-BACKPACKFASHION-STYLE-BACKPACK",methods=["POST","GET"])
def product9():
    return render_template("prod9.html")

@site.route("/nosproduit/HEWLETT-BACKPACK",methods=["POST","GET"])
def product10():
    return render_template("prod10.html")

@site.route("/nosproduit/MATT-FLAT-SAC-À-DOS",methods=["POST","GET"])
def product11():
    return render_template("prod11.html")

@site.route("/nosproduit/recherche/business",methods=["POST","GET"])
def notfoundproduct1():
    return render_template("recherche.html")

@site.route("/nosproduit/recherche/dax",methods=["POST","GET"])
def notfoundproduct2():
    return render_template("recherche2.html")
####################################  Achat de produit 
@site.route("/nosproduit/achat",methods=["GET","POST"])
def achat():
    session['produit']=request.form.get('product')
    session['color']=request.form.get('color_sac')
    return render_template("achat.html",x=session['produit'],y=session['color'])

@site.route("/nosproduit/achat/demander",methods=["GET","POST"])
def send():
    if request.method=="POST":
        session["user"]=request.form.get("user")
        session["telep"]=request.form.get("numtele")
        session["adr"]=request.form.get("adress")
        session["city"]=request.form.get("ville")
        session["product"]=request.form.get("nbr")
        session['produi']=request.form.get('se')
        session['colo']=request.form.get('co')
        print(session["product"])
        if len(session["telep"]) !=10 :
            flash("votre numéro de téléphone est incorrect",'er')
            return redirect(url_for("achat"))
        elif session["product"] == 0 :
            flash("Sélectionner le nombre de produit",'er2')
            return redirect(url_for("achat"))
        else:
            buy(session["user"],session["product"],session["telep"],session["adr"],session["city"],session['produi'],session['colo'])
            df=pd.read_csv("file.csv")
            x={'name':session["user"],'Numero de telephone':session["telep"],'nombre de produit':session["product"],'adresse':session["adr"],'city':session["city"],'nom de produit':session['produi'],'color':session['colo']}
            df=df.append(x,ignore_index=True)
            df.to_csv(r'file.csv', index = False, header = True)
            print(df)
            flash("Votre demande est bien traité")
            return redirect(url_for("product"))
    return render_template("achat.html")

####################################  contactez nous
@site.route("/Contactez-nous")
def contact():
    return render_template("ContactUs.html")

@site.route("/Contactez-nous/envoie",methods=["GET","POST"])
def envoie(): 
    if request.method=="POST":
        session["email"]=request.form.get("email")
        session["mesg"]=request.form.get("msg")
        session["name"]=request.form.get("nom")
        session["tele"]=request.form.get("tele")
        print(session["mesg"])
        send_email(session["mesg"],session["name"],session["tele"],session["email"])
        return redirect(url_for("contact"))

####################################  A propos de nous
@site.route("/Qui-Somme-Nous")
def quinous():
    return render_template("somme.html")

####################################  Termes et condition
@site.route("/Termes")
def cond():
    return render_template("termes.html")

if __name__ == "__main__":
    site.run(debug=True,host="0.0.0.0")
