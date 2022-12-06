from flask import Flask
from flask import Flask, render_template
import secret
app_final=Flask(__name__)

@app_final.route('/table/<nm>')
def table(nm):
    return render_template('table.html', name=nm)  


@app_final.route('/input/<nm>')
def input(nm):
    return render_template('input.html', name=nm)  

