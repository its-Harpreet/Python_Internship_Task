

from flask import Flask, render_template, request, redirect,session,flash,url_for
from requests import Session
from sqlalchemy.orm import sessionmaker
from task1_orm import News
from sqlalchemy import create_engine, delete
from datetime import datetime


app= Flask (__name__)
app.secret_key='thisisasecretkey'

def opendb():
    engine= create_engine('sqlite:///task1__db.sqlite3')
    Session=sessionmaker(bind=engine)
    return Session()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        headline=request.form.get('headline')
        content= request.form.get('content')
        try:
            item= News(headline=headline, content = content)
            sess = opendb()
            sess.add(item)
            sess.commit()
            sess.close()
            return redirect('/')
        except Exception  as e:
            print(e)
            return "There was a problem saving the news"
    return render_template('index.html')

@app.route('/delete/<int:id>')
def delete(id):
    sess=opendb()
    try:
        sess.query(News).filter(News.id==id).delete()
        sess.commit()
        sess.close()
        return redirect('/display')
    except Exception as e:
        return f"There was a problem while deleting {e}"


   
@app.route('/display', methods=["GET","POST"])
def display():
    sess = opendb()
    records = sess.query(News).all()
    sess.close()
    return render_template('display.html',records=records)

if __name__ == '__main__':
    app.run(debug= True)