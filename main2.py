from flask import Flask, request, render_template, redirect
import cgi
import string   

app = Flask(__name__)
app.config['DEBUG'] =True

@app.route('/')
def index():
    return render_template("signup.html")

@app.route("/signup.html", methods=["POST", "GET"])
def validate():
    username = request.form['username']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']
    email = request.form['email']

    username_error= ""
    pass_error = ""
    email_error = ""

    
    if not username:
        username_error = "Enter Username"
    
    if " " in username:
        username_error = 'No spaces allowed'

    if len(username) < 3 or len(username) > 20:
        username_error = "Name length must be 4-20 characters"
###password

    if pass1 == "":
        pass_error = "Please enter password"

    if " " in pass1:
        pass_error = "Password can not contain spaces"

    if len(pass1) < 3 or len(pass1) > 20:
        pass_error="Password length must be 4-20 characters"
  ###verify password

    if pass1 != pass2:
        pass_error="Password verifivation invalid"
###email

    if " " in email:
        email_error="Email can not contain spaces"
    if '@' not in email:
        email_error="Email not valid"
    if '.' not in email:
        email_error="Email not valid"
    if len(email) > 0 and (len(email) < 3 or len(email) > 30):
        email_error="Invalid Email length"

    if len(username_error)== 0 and len(pass_error)== 0 and len(email_error)== 0:
        return render_template('welcome.html', username=username)
    else:
        return render_template('signup.html', usename=username, username_error=username_error,
        pass_error=pass_error, email=email, email_error=email_error)



app.run()