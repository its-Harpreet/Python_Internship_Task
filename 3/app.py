

from flask import Flask, render_template, request, redirect,session,flash,url_for

app= Flask (__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/biba', methods=["GET","POST"])
def biba():
    return render_template('biba.html')

@app.route('/titan', methods=["GET","POST"])
def titan():
    return render_template('titan.html')

@app.route('/reliance', methods=["GET","POST"])
def reliance():
    return render_template('reliance.html')

@app.route('/westside', methods=["GET","POST"])
def westside():
    return render_template('westside.html')

@app.route('/redchief', methods=["GET","POST"])
def redchief():
    return render_template('redchief.html')

@app.route('/bigbazar', methods=["GET","POST"])
def bigbazar():
    return render_template('bigbazar.html')

@app.route('/puma', methods=["GET","POST"])
def puma():
    return render_template('puma.html')

@app.route('/roadster', methods=["GET","POST"])
def roadster():
    return render_template('roadster.html')

@app.route('/hnm', methods=["GET","POST"])
def hnm():
    return render_template('hnm.html')

if __name__ == '__main__':
    app.run(debug= True)

