from flask import render_template, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import login_user, logout_user, current_user, login_required
@app.route("/") 
@app.route("/index.html")
def index():
	return render_template("index.html")
@app.route("/whatis.html")
def whatis():
	return render_template("whatis.html")
@app.route("/aboutproject.html")
def aboutproject():
	return render_template("aboutproject.html")

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm(), RegistrationForm()
    return render_template('login.html', title='Sign In', form=form)
    swbutton = request.form["swbutton"]
    if swbutton == 'regpage':
        return swbutton
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
    else:
        
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                return('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')

            return redirect(next_page)
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
if __name__ == '__name__':
    app.run()