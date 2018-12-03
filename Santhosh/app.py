

from flask import Flask
from flask.templating import render_template
from flask.globals import request
from requests.sessions import session, Session


app=Flask(__name__)
app.secret_key="Santhoshkumar"


@app.route("/hello/<name>")
def home(name=None):
    return "Good Morning"+name

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="GET":
        return render_template("contact.html")
    elif request.method=="POST":
        name=request.form("username")
        age=request.form("age")
        email=request.form("email")
        phno=request.form("phonenumber")
        address=request.form("paddr")
        
        #session['username']=request.form("username")
    
        return render_template("sucess.html")



if __name__=="__main__":
    app.run("localhost",debug=True,port=1000)