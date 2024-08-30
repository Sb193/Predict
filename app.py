from flask import Flask, request, jsonify, render_template
from waitress import serve

app = Flask(__name__)

# Route cho trang chủ, trả về file HTML
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80)