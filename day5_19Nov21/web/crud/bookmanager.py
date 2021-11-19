# flask web app with sqlalchemy using sqllite
from flask import Flask
from flask import request,redirect
from flask import render_template

from flask_sqlalchemy import SQLAlchemy ### pip3 install flask-sqlalchemy - errored :(
import os

project_dir=os.path.dirname(os.path.abspath(__file__))
dbfile="sqlite:///{}".format(os.path.join(project_dir,"bookdatabase.db")) ## create this db by running the below in /crud 
'''
    .../crud $ python3
    >>> from bookmanager import db
    >>> db.create_all()
'''

app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=dbfile

db=SQLAlchemy(app)

class Book(db.Model):
    title=db.Column(db.String(80),unique=True,nullable=False,primary_key=True)
    def __repr__(self):
        return "<Title: {}>".format(self.title)


@app.route("/",methods=["GET","POST"])
def home():
    books=None
    if request.form:
        try:
            book=Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()  # record saved in db
        except Exception as e:
            print("Failed to add book")
            print(e)
    books=Book.query.all()
    return render_template("home.html",books=books)  #jinja
    
@app.route("/update",methods=["POST"])
def update():
    try:
        newtitle=request.form.get("newtitle")
        oldtitle=request.form.get("oldtitle")
        book=Book.query.filter_by(title=oldtitle).first()
        book.title=newtitle # state is updated
        db.session.commit() # commit to the db
    except Exception as e:
        print("could not update book title")
    return redirect("/")

@app.route("/delete",methods=["POST"])
def delete():
    title=request.form.get("title")
    book=Book.query.filter_by(title=title).first()
    db.session.delete(book) # delete from book where title="angular"
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

    ### getbootstrap.com --> get css from this website