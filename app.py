from flask import Flask
from flask import Flask, render_template
import secret
app=Flask(__name__)

@app.route('/table/<nm>')
def table(nm):
    return render_template('table.html', name=nm)  


@app.route('/input/<nm>')
def input(nm):
    return render_template('input.html', name=nm)  

