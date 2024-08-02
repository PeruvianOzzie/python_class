from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello_world.html')

if __name__ == '__main__':
    app.run(debug=True)