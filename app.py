#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.chdir("C:\\python_project")


# In[7]:


from flask import Flask,render_template,request,session,logging,url_for,redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from passlib.hash import sha256_crypt
import pkg_resources

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(DB_URI.format(
  user ='root',
  password = 'password',
  host = '127.0.0.1',
  db = 'register'),
  connect_args = {'time_zone': '+00:00'}
  )

#engine=create_engine("mysql+pymsql://root:1234567@localhost/register/")
                      #(mysql+pymsql://username:password@localhost/databasename)
    
db=scoped_session(sessionmaker(bind=engine))    
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        username=request.form.get("name")
        password=request.form.get("password")
        
        usernamedata=db.execute("SELECT username FROM users WHERE username:=username",{"username":username}).fetchone()
        passwordata=db.execute("SELECT password FROM users WHERE username:=username",{"username":username}).fetchone()
        
        if usernamedata is None:
            flash("No username","danger")
            return render_template("home.html")
        else:
            for passwor_data in passwordata:
                if sha256_crypt.verify(password,passwor_data):
                    session["log"]=True
                    flash("you are now login")
                    return redirect(url_for('workout'))
                else:
                    flash("incorrect password","danger")
                    return render_template("home.html")
        
    return render_template("home.html")
#register form
@app.route("/register")
def register():
    if request.method=="POST":
        name=request.form.get("name")
        username=request.form.get("username")
        password=request.form.get("password")
        confirm=request.form.get("confirm")
        secure_password=sha256_crypt.encrypt(str(password))
        
        if password==confirm:
            db.execute("INSERT INTO users(name,username,password)VALUES(:name,:username,:password)",{"name":name,"username":username,"password":secure_password})
            db.commit()
            return redirect(url_for('/'))  
        else:
            flash("password does not match","danger")
            render_template("register.html")
    return render_template("register.html")

@app.route("/workout")
def workout():
    return render_template("workout.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You are now logged out")
    return redirect(url_for('/home'))


if __name__ == "__main__":
    app.secret_key="passworddailywebcoding"
    app.run()


# In[ ]:




