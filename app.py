from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
print("Starting Flask app", app.name)
app.run(debug=True)
