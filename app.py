from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for,  session
from que import que, optionA, optionB, optionC, optionD, optionE
from model import pred_randomforest, logistic_reg
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.app_context().push()
# DATA MODEL


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'user'
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.username}"


print("database running!")


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('home2.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        session['name'] = username = request.form["loginName"]
        print(session['name'])
        user = User.query.filter_by(username=username).first()

        if user:
            if user.check_password(request.form["loginPassword"]):

                return redirect(url_for('forms'))
            else:
                return render_template('login.html', error="Password Incorrect")
        else:
            return render_template('login.html', error="Incorrect Username")

    return render_template('login.html')


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        age = request.form['age']
        user = User(username=username, email=email, age=age)
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        print("commited")

        return redirect(url_for("login"))

    return render_template('signup.html')


@app.route('/questions', methods=['POST', 'GET'])
def forms():
    if session["name"]:

        if request.method == 'POST':
            mcq = []
            items = dict(request.form.items())
            for i in range(10):
                mcq.append(items["{i}".format(i=i)])
            mcq = list(map(lambda x: 1 if int(x) <= 3 else 0, mcq))
            print(mcq, "\n", items)
            return redirect(url_for('result', acct_name=session['name'], rf=pred_randomforest(mcq, items['Age'], items['Sex']), lr=logistic_reg(mcq, items['Age'], items['Sex'])))
        return render_template('qna.html', question=que, optionA=optionA,
                               optionB=optionB, optionC=optionC, optionD=optionD, optionE=optionE, acct_name=session['name'])
    else:
        return "<h1> Not Accsessible </h1>"


@app.route('/result/<rf>/<lr>')
def result(rf, lr):

    if rf == 'True' and lr == 'True':
        result = "Our algorithm used logistic and random forest classification techniques to predict that your child has autism based on the data that you gave."
    else:
        result = "Our algorithm used logistic and random forest classification techniques to predict that your child does not have autism based on the data that you gave."

    return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
